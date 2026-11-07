# Biological rhythms dataset: WebAssembly bindings

WebAssembly build of [biological-rhythms-dataset](https://github.com/chethandvg/biological-rhythms-dataset) for browsers and Node. Function names and results are identical to the Rust crate; the shared golden vectors check it in CI.

```bash
npm install
npm run build   # pkg/web for browsers, pkg/node for Node
npm test
```

Building needs Rust with the `wasm32-unknown-unknown` target and the `wasm-bindgen` CLI at the version pinned in `Cargo.toml`.
