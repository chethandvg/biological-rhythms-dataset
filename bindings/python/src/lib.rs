// SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
// SPDX-FileCopyrightText: 2026 Chethan Dandebala Venkatarama

//! Python bindings for `biological-rhythms-dataset`. Every function keeps the Rust name, so the
//! golden vectors can call it by name. Records are dicts with the same fields as
//! `data/rhythms.json`; an unknown id raises `KeyError` and any other invalid input `ValueError`.

use biological_rhythms_dataset_rs as imp;
use pyo3::exceptions::{PyKeyError, PyValueError};
use pyo3::prelude::*;

fn error(e: imp::Error) -> PyErr {
    match e {
        imp::Error::UnknownId(_) => PyKeyError::new_err(e.to_string()),
        _ => PyValueError::new_err(e.to_string()),
    }
}

/// Parses JSON written by the Rust core into Python objects.
fn from_json<'py>(py: Python<'py>, text: &str) -> PyResult<Bound<'py, PyAny>> {
    py.import("json")?.call_method1("loads", (text,))
}

/// Every record, as a list of dicts in the order of `data/rhythms.yaml`.
#[pyfunction]
fn rhythms(py: Python<'_>) -> PyResult<Bound<'_, PyAny>> {
    from_json(py, &imp::rhythms_json())
}

/// The record with this claim id, as a dict.
#[pyfunction]
fn get<'py>(py: Python<'py>, id: &str) -> PyResult<Bound<'py, PyAny>> {
    from_json(py, &imp::get(id).map_err(error)?.to_json())
}

/// The (lowest, highest) frequency in Hz of a period, frequency or rate.
#[pyfunction]
fn frequency_hz(id: &str) -> PyResult<(f64, f64)> {
    imp::frequency_hz(id)
        .map(|hz| (hz.min, hz.max))
        .map_err(error)
}

/// Median human embryonic heart rate in bpm at `weeks` of gestation (6.5 to 10.5; each weekly median sits at mid-week, bio:HEART-RATE-WEEK-PLACEMENT).
#[pyfunction]
fn heart_rate_at(weeks: f64) -> PyResult<f64> {
    imp::heart_rate_at(weeks).map_err(error)
}

/// Cells in the mean human embryo `hours` after insemination (0 to t8).
#[pyfunction]
fn cell_count_at(hours: f64) -> PyResult<u32> {
    imp::cell_count_at(hours).map_err(error)
}

#[pymodule]
fn biological_rhythms_dataset(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;
    m.add_function(wrap_pyfunction!(rhythms, m)?)?;
    m.add_function(wrap_pyfunction!(get, m)?)?;
    m.add_function(wrap_pyfunction!(frequency_hz, m)?)?;
    m.add_function(wrap_pyfunction!(heart_rate_at, m)?)?;
    m.add_function(wrap_pyfunction!(cell_count_at, m)?)?;
    Ok(())
}
