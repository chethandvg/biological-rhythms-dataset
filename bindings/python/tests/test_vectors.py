# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
# SPDX-FileCopyrightText: 2026 Chethan Dandebala Venkatarama
"""The shared golden vectors, checked against the Python bindings."""

from pathlib import Path

import biological_rhythms_dataset
from evidence_kernel.vectors import check_dir

VECTORS = Path(__file__).resolve().parents[3] / "vectors"


def test_golden_vectors():
    assert check_dir(VECTORS, biological_rhythms_dataset) > 0
