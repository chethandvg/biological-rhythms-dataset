// SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
// SPDX-FileCopyrightText: 2026 Chethan Dandebala Venkatarama

//! WebAssembly bindings for `biological-rhythms-dataset`. Every function keeps the Rust name, so
//! the golden vectors can call it by name. Records are plain objects with the same fields as
//! `data/rhythms.json`; invalid input throws a JS `Error`.

use biological_rhythms_dataset_rs as imp;
use wasm_bindgen::prelude::*;

fn error(e: imp::Error) -> JsError {
    JsError::new(&e.to_string())
}

/// Parses JSON written by the Rust core into JavaScript values.
fn from_json(text: &str) -> Result<JsValue, JsError> {
    js_sys::JSON::parse(text).map_err(|_| JsError::new("the dataset JSON did not parse"))
}

/// The crate version.
#[wasm_bindgen]
pub fn version() -> String {
    env!("CARGO_PKG_VERSION").to_owned()
}

/// Every record, as an array of objects in the order of `data/rhythms.yaml`.
#[wasm_bindgen]
pub fn rhythms() -> Result<JsValue, JsError> {
    from_json(&imp::rhythms_json())
}

/// The record with this claim id.
#[wasm_bindgen]
pub fn get(id: &str) -> Result<JsValue, JsError> {
    from_json(&imp::get(id).map_err(error)?.to_json())
}

/// The [lowest, highest] frequency in Hz of a period, frequency or rate.
#[wasm_bindgen]
pub fn frequency_hz(id: &str) -> Result<Vec<f64>, JsError> {
    imp::frequency_hz(id)
        .map(|hz| vec![hz.min, hz.max])
        .map_err(error)
}

/// Median human embryonic heart rate in bpm at `weeks` of gestation (6.5 to 10.5; each weekly median sits at mid-week, bio:HEART-RATE-WEEK-PLACEMENT).
#[wasm_bindgen]
pub fn heart_rate_at(weeks: f64) -> Result<f64, JsError> {
    imp::heart_rate_at(weeks).map_err(error)
}

/// Cells in the mean human embryo `hours` after insemination (0 to t8).
#[wasm_bindgen]
pub fn cell_count_at(hours: f64) -> Result<u32, JsError> {
    imp::cell_count_at(hours).map_err(error)
}
