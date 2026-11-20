"""Structural checks for the committed numerical regression snapshots."""

import json
from pathlib import Path

import numpy as np
import pytest

REFERENCE_DIR = Path(__file__).resolve().parent
PHYSICS_MODES = ("default", "legacy", "diff", "uni", "casim", "sim", "kqp")
METRICS = (
    "kerma",
    "flu",
    "emean",
    "hvl_1_al",
    "hvl_2_al",
    "hc_al",
    "eeff_al",
    "hvl_1_cu",
    "hvl_2_cu",
    "hc_cu",
    "eeff_cu",
)


@pytest.mark.parametrize("physics", PHYSICS_MODES)
def test_reference_spectrum_snapshot_is_complete(physics: str) -> None:
    """Ensure accidentally truncated/altered baselines fail before model comparison."""
    path = REFERENCE_DIR / f"{physics}_values_for_get_std_results.json"
    snapshot = json.loads(path.read_text(encoding="utf-8"))

    assert set(snapshot) == {"k", "spk", *METRICS}
    energy = np.asarray(snapshot["k"], dtype=float)
    spectrum = np.asarray(snapshot["spk"], dtype=float)

    assert energy.ndim == 1 and len(energy) > 1
    assert spectrum.shape == energy.shape
    assert np.isfinite(energy).all()
    assert np.isfinite(spectrum).all()
    assert np.all(np.diff(energy) > 0)
    assert np.all(spectrum >= 0)
    assert all(np.isfinite(snapshot[metric]) for metric in METRICS)
