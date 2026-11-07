// SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
// SPDX-FileCopyrightText: 2026 Chethan Dandebala Venkatarama

//! Golden-vector tests. The Python and WebAssembly bindings check the same
//! `vectors/*.json` cases, so all three implementations give the same answers.

use biological_rhythms_dataset as bio;
use golden_vectors::{Outcome, f64_arg, str_arg};
use serde_json::Value;

fn record(r: &bio::Rhythm) -> Value {
    serde_json::to_value(r).expect("records serialise")
}

/// Maps each vector's `fn` name to this crate's implementation.
fn dispatch(name: &str, args: &[Value]) -> Outcome {
    match name {
        "rhythms" => Outcome::value(bio::rhythms().iter().map(record).collect::<Vec<_>>()),
        "get" => Outcome::from(bio::get(str_arg(args, 0)).map(record)),
        "frequency_hz" => {
            Outcome::from(bio::frequency_hz(str_arg(args, 0)).map(|hz| vec![hz.min, hz.max]))
        }
        "heart_rate_at" => Outcome::from(bio::heart_rate_at(f64_arg(args, 0))),
        "cell_count_at" => Outcome::from(bio::cell_count_at(f64_arg(args, 0))),
        _ => Outcome::unknown(name, args),
    }
}

#[test]
fn golden_vectors() {
    golden_vectors::check_dir(concat!(env!("CARGO_MANIFEST_DIR"), "/vectors"), dispatch);
}
