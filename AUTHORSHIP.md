# Authorship record

This file records the human design and review decisions behind this repository and the project it belongs to. Its author is Chethan Dandebala Venkatarama.

## Project decisions

These decisions by the author shape every Frequencies of Life repository.

| Date | Decision |
|---|---|
| 2026-10-24 | Designed the layered structure: Layer 0 repositories establish foundations, proved mathematically where possible and otherwise backed by references; each higher layer reuses the layers below it, up to contributions to music, computer science and biology. |
| 2026-10-24 | Required that the code be mathematically proved where possible and that every other claim carry an appropriate reference. |
| 2026-10-24 | Chose open-core licensing: Apache-2.0 for foundations, PolyForm Noncommercial for models and applications, and CC BY-NC for data and media. |
| 2026-10-24 | Chose free hosting on GitHub Pages under a personal account, with a later move to a custom domain. |
| 2026-11-07 | Chose to build at full scope in sprints and to publish one article a day, under the series name Frequencies of Life. |

## Decisions for this repository

| Date | Decision |
|---|---|
| 2026-11-07 | `heart_rate_at` places each Ouyang et al. 2020 weekly median at the middle of its gestational week (`bio:HEART-RATE-WEEK-PLACEMENT`, offset 0.5), where the paper's own fitted curve agrees with the medians. |
| 2026-11-07 | Package metadata (Cargo, PyPI, npm) declares the code licence only; the data licence, CC BY-NC 4.0, is stated in the README and in `LICENSES/`. |
| 2026-11-07 | The Zenodo record shows the data licence, CC BY-NC 4.0, with a note naming the code licence, because Zenodo records one licence. |

## Review log

| Date | What was reviewed | Outcome |
|---|---|---|
