# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
# SPDX-FileCopyrightText: 2026 Chethan Dandebala Venkatarama
"""Write the golden vectors for biological-rhythms-dataset from an independent oracle.

The oracle reads the measurements straight from data/rhythms.yaml (not from the
generated JSON that the Rust crate embeds) and computes every helper result
exactly with fractions.Fraction from the double-precision inputs, then rounds
once to the nearest double. The record vectors check that each implementation
returns data/rhythms.json unchanged. Run:

    python vectors/generate.py
"""

import itertools
import json
from fractions import Fraction as F
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
DOC = yaml.safe_load((DATA / "rhythms.yaml").read_text(encoding="utf-8"))
ENTRIES = DOC["rhythms"]
RECORDS = json.loads((DATA / "rhythms.json").read_text(encoding="utf-8"))["rhythms"]

# The reference implementation, in exact rational arithmetic.
SECONDS = {"s": 1, "min": 60, "h": 3600}
PER_SECOND = {"bpm": F(1, 60), "/min": F(1, 60)}


def hz(entry: dict, x: F) -> F:
    """A period's frequency is 1 / T; a rate per minute is b / 60; hertz stay as they are."""
    kind, unit = entry["kind"], entry["unit"]
    if kind == "period":
        return 1 / (x * SECONDS[unit])
    if kind == "rate":
        return x * PER_SECOND[unit]
    if kind == "frequency":
        return x
    raise ValueError(f"{entry['id']} is a {kind}")


def frequency_hz(entry: dict) -> list[float]:
    ends = [entry["value"]] * 2 if "value" in entry else [entry["min"], entry["max"]]
    return sorted(float(hz(entry, F(float(x)))) for x in ends)


def series(name: str) -> list[tuple[F, F]]:
    """(position, value) of each entry: its `at` plus the series offset, exactly."""
    offset = F(float(DOC["series"][name].get("offset", 0)))
    return sorted(
        (F(float(e["at"])) + offset, F(float(e["value"])))
        for e in ENTRIES
        if e.get("series") == name
    )


HEART = series("human-heart-rate")  # (week the median is placed at, median bpm)
CLEAVAGE = sorted(
    (t, int(cells)) for cells, t in series("human-cleavage")
)  # (hours, cells)


def heart_rate_at(weeks: float) -> float:
    x = F(weeks)
    if not HEART[0][0] <= x <= HEART[-1][0]:
        raise ValueError("outside the measured weeks")
    (w0, b0), (w1, b1) = next(
        (p, q) for p, q in itertools.pairwise(HEART) if p[0] <= x <= q[0]
    )
    return float(b0 + (x - w0) * (b1 - b0) / (w1 - w0))


def cell_count_at(hours: float) -> int:
    x = F(hours)
    if not 0 <= x <= CLEAVAGE[-1][0]:
        raise ValueError("outside the measured times")
    return max([1] + [cells for t, cells in CLEAVAGE if t <= x])


# Tolerances. The Rust helpers round at most three times in IEEE double precision, each
# time with relative error at most u = 2^-53 (about 1.1e-16): a period in hours becomes
# 1 / (60 * (60 * T)), a period in minutes 1 / (60 * T), a rate b / 60, and an interpolated
# heart rate b0 + (x - w0) * (b1 - b0) / (w1 - w0), where x - w0 is exact (Sterbenz's lemma,
# as w0 <= x <= 2 * w0), b1 - b0 and w1 - w0 are exact (whole-number medians one week apart),
# and the clamp can only move the result towards the exact value. So each Rust result is
# within about 3u of the exact value, the oracle's single rounding within u, and the two
# within about 4u = 4.4e-16 of each other, relative: below REL. Cell counts are integers
# found by comparing doubles, with no arithmetic, so they must match exactly.
REL = 1e-15


def write(name: str, description: str, cases: list[dict], rel: float = 0.0) -> None:
    doc = {
        "schema": "golden-vectors@1",
        "description": description,
        "tolerance": {"rel": rel, "abs": 0.0},
        "cases": cases,
    }
    (HERE / f"{name}.json").write_text(
        json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"wrote {len(cases)} cases to vectors/{name}.json")


def case(claim: str, fn: str, args: list, oracle, note: str = "") -> dict:
    """The expected value from the oracle, or an error case if the oracle rejects the input."""
    out = {"claim": claim, "fn": fn, "args": args}
    try:
        out["expected"] = oracle(*args)
    except (ValueError, KeyError):
        out["error"] = True
    return {**out, "note": note} if note else out


BY_ID = {e["id"]: e for e in ENTRIES}
RECORD = {r["id"]: r for r in RECORDS}


def record(rid: str) -> dict:
    return RECORD[rid]


if __name__ == "__main__":
    agree = "bio:IMPLEMENTATIONS-AGREE"
    write(
        "records",
        "Every record, returned unchanged from data/rhythms.json.",
        [
            case(
                agree,
                "rhythms",
                [],
                lambda: RECORDS,
                "all records, in the order of data/rhythms.yaml",
            ),
            case(
                agree, "get", ["bio:HUMAN-CA-SPIKE-INTERVAL"], record, "a range, with n"
            ),
            case(
                agree,
                "get",
                ["bio:HUMAN-SEGMENTATION-CLOCK-PERIOD"],
                record,
                "four sources and a contested note",
            ),
            case(agree, "get", ["bio:HUMAN-EHR-9W"], record, "a member of a series"),
            case(agree, "get", ["bio:HUMAN-CA-SPIKE"], record, "unknown id"),
            case(
                agree,
                "get",
                ["HUMAN-CA-SPIKE-INTERVAL"],
                record,
                "the prefix is part of the id",
            ),
        ],
    )
    write(
        "frequency",
        "frequency_hz for every record: periods, frequencies and rates in hertz; everything else rejected.",
        [
            case(
                "bio:FREQUENCY-HZ",
                "frequency_hz",
                [e["id"]],
                lambda rid: frequency_hz(BY_ID[rid]),
                e["kind"],
            )
            for e in ENTRIES
        ]
        + [
            case(
                "bio:FREQUENCY-HZ",
                "frequency_hz",
                ["bio:NOT-A-RECORD"],
                lambda rid: frequency_hz(BY_ID[rid]),
                "unknown id",
            )
        ],
        rel=REL,
    )
    weeks = [6.5, 6.75, 7.0, 7.5, 7.8, 8.0, 8.5, 8 + 5 / 6, 9.0, 9.5, 9.6, 10.25, 10.5]
    write(
        "heart_rate",
        "heart_rate_at: exact at each weekly median, placed at mid-week (6.5 to 10.5 weeks), linear in between, rejected outside 6.5-10.5 weeks.",
        [case("bio:HEART-RATE-AT", "heart_rate_at", [w], heart_rate_at) for w in weeks]
        + [
            case(
                "bio:HEART-RATE-AT", "heart_rate_at", [w], heart_rate_at, "not measured"
            )
            for w in (6.0, 6.499, 10.501, 12.0, -1.0)
        ],
        rel=REL,
    )
    times = sorted(
        {0.0, 12.0, 30.0, 39.0, 45.0, 60.0, *(float(t) for t, _ in CLEAVAGE)}
        | {float(t) - 0.01 for t, _ in CLEAVAGE}
    )
    write(
        "cell_count",
        "cell_count_at: the step function over the mean division times t2-t8, rejected outside 0-t8.",
        [case("bio:CELL-COUNT-AT", "cell_count_at", [h], cell_count_at) for h in times]
        + [
            case(
                "bio:CELL-COUNT-AT", "cell_count_at", [h], cell_count_at, "not measured"
            )
            for h in (-0.5, 61.52, 87.75, 110.0)
        ],
    )
