# Changelog

All notable changes are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2026-11-07

### Fixed

- Zenodo could not archive 0.1.0: its CITATION.cff importer reads `license` as a single string, and this repository lists two (PolyForm Noncommercial for the code, CC BY-NC 4.0 for the data). `scripts/build.py` now also generates `.zenodo.json` from CITATION.cff, which Zenodo reads instead; it carries the data licence and a note naming the code licence. The data, code and claims are unchanged.

## [0.1.0] - 2026-11-07

### Added

- The dataset: 40 measurements of the rhythms and timings of early life in humans and mice (Ca2+ spikes and zinc sparks at egg activation, sperm flagellar beat, oviduct cilia, uterine contractions, preimplantation timings t2 to tEB, embryonic heart rate at 6 to 10 weeks, the segmentation clock and the stage of genome activation), each with its species, unit, statistic, stage, method, sample size where reported, and sources with a DOI or PMID. Hand-edited in `data/rhythms.yaml` and `data/sources.yaml`, with JSON Schemas in `schema/`.
- `scripts/build.py`, which generates `data/rhythms.json`, `data/rhythms.csv`, the 40 R claims in `claims.yaml` and the README measurement tables, and with `--check` fails CI when any of them is stale.
- Rust functions `rhythms`, `get`, `frequency_hz` (converted with rhythm-units), `heart_rate_at` and `cell_count_at`, with the dataset embedded in the crate.
- The model assumption `bio:HEART-RATE-WEEK-PLACEMENT`: `heart_rate_at` places each weekly heart-rate median at the middle of its gestational week, so it answers for 6.5 to 10.5 weeks.
- Python (PyO3) and WebAssembly bindings with the same function names.
- 89 golden vectors from an independent oracle that reads the YAML and computes exactly with fractions, checked in all three implementations.
- Lean 4 proofs that linear interpolation returns each measurement at its own week and stays between the two bracketing measurements.
