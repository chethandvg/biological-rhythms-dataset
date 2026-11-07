# Biological rhythms dataset

**Measured frequencies and timings of early life, from sperm tail beat to embryonic heart rate, each value with its species, method and DOI.**

[![CI](https://github.com/chethandvg/biological-rhythms-dataset/actions/workflows/ci.yml/badge.svg)](https://github.com/chethandvg/biological-rhythms-dataset/actions/workflows/ci.yml)
[![Proofs](https://github.com/chethandvg/biological-rhythms-dataset/actions/workflows/proofs.yml/badge.svg)](https://github.com/chethandvg/biological-rhythms-dataset/actions/workflows/proofs.yml)
[![Code licence](https://img.shields.io/badge/code-PolyForm--Noncommercial--1.0.0-blue)](LICENSE)
[![Data licence](https://img.shields.io/badge/data-CC_BY--NC_4.0-blue)](LICENSES/CC-BY-NC-4.0.txt)

Part of **[Frequencies of Life](https://chethandvg.github.io/frequencies-of-life/)**, open code for the rhythms of life in which every claim says how it is known: proved, verified, tested, referenced or assumed.

## About the dataset

A versioned, citable dataset of 40 measured rhythms and timings from the beginning of life in humans (*Homo sapiens*) and mice (*Mus musculus*): calcium spikes and zinc sparks when an egg is activated, the beat of the sperm tail, the cilia of the fallopian tube, uterine contractions, the timing of the first cell divisions and of the blastocyst, embryonic heart rate, the segmentation clock that lays down the vertebrae, and the stage at which the embryo's own genes switch on.

Every record is one measurement in one species. It gives the value or range with its unit and statistic (mean, median or range), the developmental stage, the measurement method, the sample size where the source reports it, and at least one peer-reviewed source with a DOI or PubMed ID. Human and mouse values are kept apart, and values that later work disputes or revises are flagged.

- **Variables:** `id`, `version`, `topic`, `quantity`, `species`, `kind` (period, frequency, rate, duration, time, stage or count), `value` or `min` and `max`, `unit`, `statistic`, `stage`, `method`, `n` and `n_unit`, `series` and `at` (for the records a helper reads: the series and the record's place in it, such as a gestational week), `notes`, `contested`, and `sources` (citation, title, DOI, PMID). The JSON also describes each series: what its `at` means and the offset a helper adds to it.
- **Files:** [`data/rhythms.yaml`](data/rhythms.yaml) (the hand-edited source) and [`data/sources.yaml`](data/sources.yaml) (the references), from which [`data/rhythms.json`](data/rhythms.json) and [`data/rhythms.csv`](data/rhythms.csv) are generated. JSON Schemas are in [`schema/`](schema). The CSV is UTF-8 without a byte-order mark: pandas and R read it as it is, but Excel shows characters such as µ and ζ correctly only if you import it with Data > From Text/CSV.
- **Sources:** 20 references (19 articles published from 1988 to 2026, and one author correction). Each DOI was checked against Crossref and each PMID against PubMed, and CI checks them again every week.
- **Licence:** data CC BY-NC 4.0; code PolyForm Noncommercial 1.0.0.
- **Version:** 0.1.0. Cite it with [CITATION.cff](CITATION.cff).

## Measurements

The value column gives the statistic in brackets; n is the sample size as the source reports it. ⚑ marks a value that later work disputes or revises.

<!-- rhythms-table:start -->
### Egg activation

| Claim | Measurement | Species | Value | n | Sources |
|---|---|---|---|---|---|
| `bio:HUMAN-CA-SPIKE-INTERVAL` | Interval between Ca2+ spikes in human eggs at fertilisation | *Homo sapiens* | 10–35 min (range) | 10 eggs with Ca2+ transients, of 26 inseminated | [Taylor et al. 1993, Human Reproduction](https://doi.org/10.1093/oxfordjournals.humrep.a137999) |
| `bio:HUMAN-CA-SPIKE-DURATION` | Duration of each Ca2+ spike in human eggs at fertilisation | *Homo sapiens* | 120 s (approximate) | 10 eggs with Ca2+ transients, of 26 inseminated | [Taylor et al. 1993, Human Reproduction](https://doi.org/10.1093/oxfordjournals.humrep.a137999) |
| `bio:MOUSE-CA-SPIKE-INTERVAL` | Interval between Ca2+ transients in mouse eggs at fertilisation | *Mus musculus* | 3.4 min (mean) |  | [Kline & Kline 1992, Developmental Biology](https://doi.org/10.1016/0012-1606(92)90265-i) |
| `bio:MOUSE-CA-FIRST-TRANSIENT-DURATION` | Duration of the first Ca2+ transient in mouse eggs at fertilisation | *Mus musculus* | 2.3 min (mean) |  | [Kline & Kline 1992, Developmental Biology](https://doi.org/10.1016/0012-1606(92)90265-i) |
| `bio:MOUSE-CA-SPIKE-DURATION` | Duration of each later Ca2+ transient in mouse eggs at fertilisation | *Mus musculus* | 0.5 min (mean) |  | [Kline & Kline 1992, Developmental Biology](https://doi.org/10.1016/0012-1606(92)90265-i) |
| `bio:MOUSE-ZINC-SPARK-INTERVAL` | Interval between zinc sparks in activated mouse eggs | *Mus musculus* | 9.5 min (mean) | 36 intervals between sparks | [Kim et al. 2011, ACS Chemical Biology](https://doi.org/10.1021/cb200084y) |
| `bio:MOUSE-EGG-ZINC-VESICLES` | Number of zinc-loaded cortical vesicles in a mouse egg | *Mus musculus* | 8,000 vesicles (estimate) |  | [Que et al. 2015, Nature Chemistry](https://doi.org/10.1038/nchem.2133) |
| `bio:MOUSE-ZINC-VESICLE-ATOMS` | Zinc atoms in one cortical vesicle of a mouse egg | *Mus musculus* | 1,000,000 atoms (approximate) |  | [Que et al. 2015, Nature Chemistry](https://doi.org/10.1038/nchem.2133) |
| `bio:HUMAN-ZINC-SPARKS-PER-EGG` | Number of zinc sparks in a human egg activated with PLCζ | *Homo sapiens* | 1 spark (observed) | 2 eggs that sparked, of 5 injected with hPLCζ cRNA | [Duncan et al. 2016, Scientific Reports](https://doi.org/10.1038/srep24737); [Que et al. 2019, Theriogenology](https://doi.org/10.1016/j.theriogenology.2018.12.031) |

### Sperm

| Claim | Measurement | Species | Value | n | Sources |
|---|---|---|---|---|---|
| `bio:HUMAN-SPERM-BEAT-DILUTED-SEMEN` | Flagellar beat frequency of human sperm swimming in diluted semen | *Homo sapiens* | 19 Hz (median) | 205 cells | [Gallagher et al. 2019, Human Reproduction](https://doi.org/10.1093/humrep/dez056) |
| `bio:HUMAN-SPERM-BEAT-VISCOUS` | Flagellar beat frequency of human sperm swimming in a high-viscosity medium | *Homo sapiens* | 10 Hz (median) | 119 cells | [Gallagher et al. 2019, Human Reproduction](https://doi.org/10.1093/humrep/dez056) |
| `bio:HUMAN-SPERM-BEAT-ADHERED` | Flagellar beat frequency of head-adhered human sperm before stimulation | *Homo sapiens* | 18.9 Hz (median) | 34 cells from 4 donors | [Ooi et al. 2014, Royal Society Open Science](https://doi.org/10.1098/rsos.140230) |
| `bio:HUMAN-SPERM-BEAT-HYPERACTIVATED` | Flagellar beat frequency of head-adhered human sperm hyperactivated with 4-AP | *Homo sapiens* | 11.7 Hz (median) | 34 cells from 4 donors | [Ooi et al. 2014, Royal Society Open Science](https://doi.org/10.1098/rsos.140230) |

### Oviduct

| Claim | Measurement | Species | Value | n | Sources |
|---|---|---|---|---|---|
| `bio:HUMAN-OVIDUCT-CILIA-BEAT` | Ciliary beat frequency in the human fallopian tube | *Homo sapiens* | 5.3 Hz (mean) ⚑ | 26 women (14 in the proliferative, 12 in the secretory phase) | [Lyons et al. 2002, Human Reproduction](https://doi.org/10.1093/humrep/17.3.584); [Bylander et al. 2010, Reproductive Biology and Endocrinology](https://doi.org/10.1186/1477-7827-8-48) |
| `bio:MOUSE-OVIDUCT-CILIA-BEAT` | Ciliary beat frequency in the mouse fallopian tube | *Mus musculus* | 23.3 Hz (mean) | 19 mice | [Bylander et al. 2010, Reproductive Biology and Endocrinology](https://doi.org/10.1186/1477-7827-8-48) |

### Uterus

| Claim | Measurement | Species | Value | n | Sources |
|---|---|---|---|---|---|
| `bio:HUMAN-UTERINE-CONTRACTIONS-LATE-FOLLICULAR` | Human uterine contraction frequency in the late follicular phase | *Homo sapiens* | 1.61 per min (as reported) | 70 recordings analysed across all phases together, of 96 from 64 healthy women with natural cycles; the number in each phase is not recorded here | [Rees et al. 2023, Reproductive BioMedicine Online](https://doi.org/10.1016/j.rbmo.2022.08.104) |
| `bio:HUMAN-UTERINE-CONTRACTIONS-MENSTRUAL` | Human uterine contraction frequency in the menstrual phase | *Homo sapiens* | 1.31 per min (as reported) | 70 recordings analysed across all phases together, of 96 from 64 healthy women with natural cycles; the number in each phase is not recorded here | [Rees et al. 2023, Reproductive BioMedicine Online](https://doi.org/10.1016/j.rbmo.2022.08.104) |
| `bio:HUMAN-UTERINE-CONTRACTIONS-LATE-LUTEAL` | Human uterine contraction frequency in the late luteal phase | *Homo sapiens* | 1.35 per min (as reported) | 70 recordings analysed across all phases together, of 96 from 64 healthy women with natural cycles; the number in each phase is not recorded here | [Rees et al. 2023, Reproductive BioMedicine Online](https://doi.org/10.1016/j.rbmo.2022.08.104) |

### Preimplantation development

| Claim | Measurement | Species | Value | n | Sources |
|---|---|---|---|---|---|
| `bio:HUMAN-EMBRYO-T2` | Time from insemination to the 2-cell stage (t2) in human embryos | *Homo sapiens* | 27.48 h (mean) | 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here) | [Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction](https://doi.org/10.5935/1518-0557.20260005) |
| `bio:HUMAN-EMBRYO-T3` | Time from insemination to the 3-cell stage (t3) in human embryos | *Homo sapiens* | 37.78 h (mean) | 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here) | [Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction](https://doi.org/10.5935/1518-0557.20260005) |
| `bio:HUMAN-EMBRYO-T4` | Time from insemination to the 4-cell stage (t4) in human embryos | *Homo sapiens* | 40.4 h (mean) | 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here) | [Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction](https://doi.org/10.5935/1518-0557.20260005) |
| `bio:HUMAN-EMBRYO-T5` | Time from insemination to the 5-cell stage (t5) in human embryos | *Homo sapiens* | 51.04 h (mean) | 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here) | [Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction](https://doi.org/10.5935/1518-0557.20260005) |
| `bio:HUMAN-EMBRYO-T6` | Time from insemination to the 6-cell stage (t6) in human embryos | *Homo sapiens* | 54.25 h (mean) | 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here) | [Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction](https://doi.org/10.5935/1518-0557.20260005) |
| `bio:HUMAN-EMBRYO-T7` | Time from insemination to the 7-cell stage (t7) in human embryos | *Homo sapiens* | 57.57 h (mean) | 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here) | [Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction](https://doi.org/10.5935/1518-0557.20260005) |
| `bio:HUMAN-EMBRYO-T8` | Time from insemination to the 8-cell stage (t8) in human embryos | *Homo sapiens* | 61.51 h (mean) | 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here) | [Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction](https://doi.org/10.5935/1518-0557.20260005) |
| `bio:HUMAN-EMBRYO-TM` | Time from insemination to compaction (tM, morula) in human embryos | *Homo sapiens* | 87.75 h (mean) | 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here) | [Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction](https://doi.org/10.5935/1518-0557.20260005) |
| `bio:HUMAN-EMBRYO-TSB` | Time from insemination to the start of blastulation (tSB) in human embryos | *Homo sapiens* | 99.18 h (mean) | 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here) | [Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction](https://doi.org/10.5935/1518-0557.20260005) |
| `bio:HUMAN-EMBRYO-TB` | Time from insemination to the full blastocyst (tB) in human embryos | *Homo sapiens* | 104.5 h (mean) | 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here) | [Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction](https://doi.org/10.5935/1518-0557.20260005) |
| `bio:HUMAN-EMBRYO-TEB` | Time from insemination to the expanded blastocyst (tEB) in human embryos | *Homo sapiens* | 110.82 h (mean) | 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here) | [Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction](https://doi.org/10.5935/1518-0557.20260005) |

### Embryonic heart

| Claim | Measurement | Species | Value | n | Sources |
|---|---|---|---|---|---|
| `bio:HUMAN-EHR-6W` | Median human embryonic heart rate at 6 weeks of gestation | *Homo sapiens* | 117 bpm (median) | 20,272 pregnancies measured in this gestational week (Table 3 of the paper; 30,416 across weeks 6-10) | [Ouyang et al. 2020, BMC Pregnancy and Childbirth](https://doi.org/10.1186/s12884-020-03186-2) |
| `bio:HUMAN-EHR-7W` | Median human embryonic heart rate at 7 weeks of gestation | *Homo sapiens* | 146 bpm (median) | 2,969 pregnancies measured in this gestational week (Table 3 of the paper; 30,416 across weeks 6-10) | [Ouyang et al. 2020, BMC Pregnancy and Childbirth](https://doi.org/10.1186/s12884-020-03186-2) |
| `bio:HUMAN-EHR-8W` | Median human embryonic heart rate at 8 weeks of gestation | *Homo sapiens* | 174 bpm (median) | 4,109 pregnancies measured in this gestational week (Table 3 of the paper; 30,416 across weeks 6-10) | [Ouyang et al. 2020, BMC Pregnancy and Childbirth](https://doi.org/10.1186/s12884-020-03186-2) |
| `bio:HUMAN-EHR-9W` | Median human embryonic heart rate at 9 weeks of gestation | *Homo sapiens* | 176 bpm (median) | 2,267 pregnancies measured in this gestational week (Table 3 of the paper; 30,416 across weeks 6-10) | [Ouyang et al. 2020, BMC Pregnancy and Childbirth](https://doi.org/10.1186/s12884-020-03186-2) |
| `bio:HUMAN-EHR-10W` | Median human embryonic heart rate at 10 weeks of gestation | *Homo sapiens* | 174 bpm (median) | 799 pregnancies measured in this gestational week (Table 3 of the paper; 30,416 across weeks 6-10) | [Ouyang et al. 2020, BMC Pregnancy and Childbirth](https://doi.org/10.1186/s12884-020-03186-2) |

### Segmentation clock

| Claim | Measurement | Species | Value | n | Sources |
|---|---|---|---|---|---|
| `bio:HUMAN-SEGMENTATION-CLOCK-PERIOD` | Period of the human segmentation clock in presomitic mesoderm cells derived in vitro | *Homo sapiens* | 5 h (approximate) ⚑ |  | [Matsuda et al. 2020, Nature](https://doi.org/10.1038/s41586-020-2144-9); [Diaz-Cuadros et al. 2020, Nature](https://doi.org/10.1038/s41586-019-1885-9); [Matsuda et al. 2020, Science](https://doi.org/10.1126/science.aba7668); [Diaz-Cuadros et al. 2026, Nature (Author Correction)](https://doi.org/10.1038/s41586-026-10651-z) |
| `bio:MOUSE-SEGMENTATION-CLOCK-PERIOD` | Period of the mouse segmentation clock in presomitic mesoderm cells derived in vitro | *Mus musculus* | 2–3 h (range) |  | [Matsuda et al. 2020, Science](https://doi.org/10.1126/science.aba7668); [Diaz-Cuadros et al. 2020, Nature](https://doi.org/10.1038/s41586-019-1885-9); [Diaz-Cuadros et al. 2026, Nature (Author Correction)](https://doi.org/10.1038/s41586-026-10651-z) |

### Genome activation

| Claim | Measurement | Species | Value | n | Sources |
|---|---|---|---|---|---|
| `bio:HUMAN-MAJOR-ZGA-STAGE` | Cell stage of major embryonic genome activation in human embryos | *Homo sapiens* | 4–8 cells (range) ⚑ |  | [Braude et al. 1988, Nature](https://doi.org/10.1038/332459a0); [Asami et al. 2022, Cell Stem Cell](https://doi.org/10.1016/j.stem.2021.11.012) |
| `bio:HUMAN-MINOR-ZGA-STAGE` | Cell stage at which human embryonic transcription begins (minor genome activation) | *Homo sapiens* | 1 cell (observed) |  | [Asami et al. 2022, Cell Stem Cell](https://doi.org/10.1016/j.stem.2021.11.012) |
| `bio:MOUSE-MAJOR-ZGA-STAGE` | Cell stage of major zygotic genome activation in mouse embryos | *Mus musculus* | 2 cells (as reported) |  | [Aoki 2022, Journal of Reproduction and Development](https://doi.org/10.1262/jrd.2021-129); [Braude et al. 1988, Nature](https://doi.org/10.1038/332459a0) |
| `bio:MOUSE-MINOR-ZGA-STAGE` | Cell stage of minor zygotic genome activation in mouse embryos | *Mus musculus* | 1 cell (as reported) |  | [Aoki 2022, Journal of Reproduction and Development](https://doi.org/10.1262/jrd.2021-129) |

⚑ **Contested or revised values**

- `bio:HUMAN-OVIDUCT-CILIA-BEAT`: Bylander et al. 2010, a mouse study, quote 5-20 Hz for the human tube, citing older human studies by Mahmood et al. (1998) and Westrom et al.; this direct measurement lies at the low end of that range.
- `bio:HUMAN-SEGMENTATION-CLOCK-PERIOD`: Diaz-Cuadros et al. 2020 carries an Editor's Note (February 2024) about cell-tracking errors; its Author Correction (Nature 654:E13, 2026) states that the conclusions still hold.
- `bio:HUMAN-MAJOR-ZGA-STAGE`: Revised in part: low-level transcription begins earlier, at the one-cell stage (Asami et al. 2022; bio:HUMAN-MINOR-ZGA-STAGE). The major wave is still placed at 4-8 cells.
<!-- rhythms-table:end -->

## Claims and evidence

Only the two P claims are proved, and they are about interpolation, not biology. The measurements are R claims: referenced, not proved. The one M claim, `bio:HEART-RATE-WEEK-PLACEMENT`, is the assumption `heart_rate_at` makes about where in each gestational week a weekly median belongs.

<!-- claims-table:start -->
| Claim | Level | Statement | Evidence |
|---|---|---|---|
| `bio:INTERPOLATION-AT-MEASUREMENTS` | P | Linear interpolation between two measurements taken at different times returns each measurement exactly at its own time. | [`BiologicalRhythmsDataset.lerp_at_ends`](proofs/BiologicalRhythmsDataset/Interpolation.lean) |
| `bio:INTERPOLATION-BOUNDED` | P | Between two measurements, linear interpolation never leaves the range they span: it is at least the smaller measured value and at most the larger. | [`BiologicalRhythmsDataset.lerp_between`](proofs/BiologicalRhythmsDataset/Interpolation.lean) |
| `bio:HEART-RATE-WEEK-PLACEMENT` | M | heart_rate_at places the Ouyang et al. 2020 median for gestational week w at w + 0.5 weeks, the middle of that week. | assumption: Each weekly median summarises the pregnancies scanned during completed week w, the usual way of reporting gestational age, and the middle of the week represents them. The 0.5 treats gestational age as continuous within the week, from w to w+1; if age is counted in whole days, w+0 to w+6, the middle is w + 3/7 (about w + 0.43) weeks, half a day earlier, which would move heart_rate_at by at most about 2 bpm (its steepest segment rises 29 bpm a week). The full text (PMC7488996, Methods) obtains GW by dividing the gestational day by 7 and computes the percentiles 'for each time point', but states no rule (rounding or truncation) for assigning scans to whole weeks; the abstract gives the same fit in days and in weeks. The paper's own fit, HR = -350.410 + 107.788 GW - 5.488 GW^2, agrees with every weekly median to within 5 bpm at w + 0.5 (118, 149, 169, 178 and 176 bpm at 6.5 to 10.5 weeks, against medians of 117, 146, 174, 176 and 174); at w + 3/7 its largest miss is 5.8 bpm (168 against 174 at 8 weeks), and at the whole week it is 18 bpm (99 bpm at 6.0 weeks, against 117). Placing the medians at the whole week would shift the curve half a week early. |
| `bio:HEART-RATE-AT` | T | heart_rate_at(w) returns each Ouyang et al. 2020 weekly median exactly at the middle of its week (6.5, 7.5, 8.5, 9.5 and 10.5 weeks; bio:HEART-RATE-WEEK-PLACEMENT), interpolates linearly between neighbouring medians to within 1e-15 relative of an exact rational oracle, stays between the two bracketing medians in floating point too, and rejects weeks outside [6.5, 10.5]. | [`vectors/heart_rate.json`](vectors/heart_rate.json), [`src/lib.rs`](src/lib.rs) |
| `bio:CELL-COUNT-AT` | T | cell_count_at(h) is 1 before t2 and k from the mean time tk until the next division (k = 2 to 8), using the Lorenzo Rodríguez et al. 2026 means, and rejects hours below 0 or after t8, where the dataset has no division times. | [`vectors/cell_count.json`](vectors/cell_count.json), [`src/lib.rs`](src/lib.rs) |
| `bio:FREQUENCY-HZ` | T | frequency_hz(id) converts every period, frequency and rate in the dataset to its range in hertz with rhythm-units (f = 1/T for a period, bpm/60 for a rate), matching an exact rational oracle to within 1e-15 relative, and rejects durations, time points, stages and counts. | [`vectors/frequency.json`](vectors/frequency.json), [`src/lib.rs`](src/lib.rs) |
| `bio:DATASET-CONSISTENT` | T | data/rhythms.yaml matches its JSON Schema; every entry is one species, named in its id and its description, with a method and at least one source that has a DOI or PMID; and data/rhythms.json, data/rhythms.csv, the R claims in this ledger and the README tables are exactly what scripts/build.py generates from it, which CI checks on every push. | [`scripts/build.py`](scripts/build.py), [`schema/rhythms.schema.json`](schema/rhythms.schema.json), [`schema/sources.schema.json`](schema/sources.schema.json), [`.github/workflows/ci.yml`](.github/workflows/ci.yml) |
| `bio:IMPLEMENTATIONS-AGREE` | T | The Rust crate, the Python bindings and the WebAssembly bindings return the same records, unchanged from data/rhythms.json, and the same helper results on every shared golden vector. | [`vectors/records.json`](vectors/records.json), [`vectors/frequency.json`](vectors/frequency.json), [`vectors/heart_rate.json`](vectors/heart_rate.json), [`vectors/cell_count.json`](vectors/cell_count.json), [`tests/vectors.rs`](tests/vectors.rs), [`bindings/python/tests/test_vectors.py`](bindings/python/tests/test_vectors.py), [`bindings/wasm/tests/vectors.test.mjs`](bindings/wasm/tests/vectors.test.mjs) |
| `bio:HUMAN-CA-SPIKE-INTERVAL` | R | Interval between Ca2+ spikes in human eggs at fertilisation: 10–35 min (range; n = 10 eggs with Ca2+ transients, of 26 inseminated). | Taylor et al. 1993, Human Reproduction 8(12):2174-2179 ([doi:10.1093/oxfordjournals.humrep.a137999](https://doi.org/10.1093/oxfordjournals.humrep.a137999), [PMID 8150920](https://pubmed.ncbi.nlm.nih.gov/8150920/)) |
| `bio:HUMAN-CA-SPIKE-DURATION` | R | Duration of each Ca2+ spike in human eggs at fertilisation: 120 s (approximate; n = 10 eggs with Ca2+ transients, of 26 inseminated). | Taylor et al. 1993, Human Reproduction 8(12):2174-2179 ([doi:10.1093/oxfordjournals.humrep.a137999](https://doi.org/10.1093/oxfordjournals.humrep.a137999), [PMID 8150920](https://pubmed.ncbi.nlm.nih.gov/8150920/)) |
| `bio:MOUSE-CA-SPIKE-INTERVAL` | R | Interval between Ca2+ transients in mouse eggs at fertilisation: 3.4 min (mean). | Kline & Kline 1992, Developmental Biology 149(1):80-89 ([doi:10.1016/0012-1606(92)90265-i](https://doi.org/10.1016/0012-1606%2892%2990265-i), [PMID 1728596](https://pubmed.ncbi.nlm.nih.gov/1728596/)) |
| `bio:MOUSE-CA-FIRST-TRANSIENT-DURATION` | R | Duration of the first Ca2+ transient in mouse eggs at fertilisation: 2.3 min (mean). | Kline & Kline 1992, Developmental Biology 149(1):80-89 ([doi:10.1016/0012-1606(92)90265-i](https://doi.org/10.1016/0012-1606%2892%2990265-i), [PMID 1728596](https://pubmed.ncbi.nlm.nih.gov/1728596/)) |
| `bio:MOUSE-CA-SPIKE-DURATION` | R | Duration of each later Ca2+ transient in mouse eggs at fertilisation: 0.5 min (mean). | Kline & Kline 1992, Developmental Biology 149(1):80-89 ([doi:10.1016/0012-1606(92)90265-i](https://doi.org/10.1016/0012-1606%2892%2990265-i), [PMID 1728596](https://pubmed.ncbi.nlm.nih.gov/1728596/)) |
| `bio:MOUSE-ZINC-SPARK-INTERVAL` | R | Interval between zinc sparks in activated mouse eggs: 9.5 min (mean; n = 36 intervals between sparks). | Kim et al. 2011, ACS Chemical Biology 6(7):716-723 ([doi:10.1021/cb200084y](https://doi.org/10.1021/cb200084y), [PMID 21526836](https://pubmed.ncbi.nlm.nih.gov/21526836/)) |
| `bio:MOUSE-EGG-ZINC-VESICLES` | R | Number of zinc-loaded cortical vesicles in a mouse egg: 8,000 vesicles (estimate). | Que et al. 2015, Nature Chemistry 7(2):130-139 ([doi:10.1038/nchem.2133](https://doi.org/10.1038/nchem.2133), [PMID 25615666](https://pubmed.ncbi.nlm.nih.gov/25615666/)) |
| `bio:MOUSE-ZINC-VESICLE-ATOMS` | R | Zinc atoms in one cortical vesicle of a mouse egg: 1,000,000 atoms (approximate). | Que et al. 2015, Nature Chemistry 7(2):130-139 ([doi:10.1038/nchem.2133](https://doi.org/10.1038/nchem.2133), [PMID 25615666](https://pubmed.ncbi.nlm.nih.gov/25615666/)) |
| `bio:HUMAN-ZINC-SPARKS-PER-EGG` | R | Number of zinc sparks in a human egg activated with PLCζ: 1 spark (observed; n = 2 eggs that sparked, of 5 injected with hPLCζ cRNA). | Duncan et al. 2016, Scientific Reports 6:24737 ([doi:10.1038/srep24737](https://doi.org/10.1038/srep24737), [PMID 27113677](https://pubmed.ncbi.nlm.nih.gov/27113677/)); Que et al. 2019, Theriogenology 127:41-48 ([doi:10.1016/j.theriogenology.2018.12.031](https://doi.org/10.1016/j.theriogenology.2018.12.031), [PMID 30639695](https://pubmed.ncbi.nlm.nih.gov/30639695/)) |
| `bio:HUMAN-SPERM-BEAT-DILUTED-SEMEN` | R | Flagellar beat frequency of human sperm swimming in diluted semen: 19 Hz (median; n = 205 cells). | Gallagher et al. 2019, Human Reproduction 34(7):1173-1185 ([doi:10.1093/humrep/dez056](https://doi.org/10.1093/humrep/dez056), [PMID 31170729](https://pubmed.ncbi.nlm.nih.gov/31170729/)) |
| `bio:HUMAN-SPERM-BEAT-VISCOUS` | R | Flagellar beat frequency of human sperm swimming in a high-viscosity medium: 10 Hz (median; n = 119 cells). | Gallagher et al. 2019, Human Reproduction 34(7):1173-1185 ([doi:10.1093/humrep/dez056](https://doi.org/10.1093/humrep/dez056), [PMID 31170729](https://pubmed.ncbi.nlm.nih.gov/31170729/)) |
| `bio:HUMAN-SPERM-BEAT-ADHERED` | R | Flagellar beat frequency of head-adhered human sperm before stimulation: 18.9 Hz (median; n = 34 cells from 4 donors). | Ooi et al. 2014, Royal Society Open Science 1(2):140230 ([doi:10.1098/rsos.140230](https://doi.org/10.1098/rsos.140230), [PMID 26064546](https://pubmed.ncbi.nlm.nih.gov/26064546/)) |
| `bio:HUMAN-SPERM-BEAT-HYPERACTIVATED` | R | Flagellar beat frequency of head-adhered human sperm hyperactivated with 4-AP: 11.7 Hz (median; n = 34 cells from 4 donors). | Ooi et al. 2014, Royal Society Open Science 1(2):140230 ([doi:10.1098/rsos.140230](https://doi.org/10.1098/rsos.140230), [PMID 26064546](https://pubmed.ncbi.nlm.nih.gov/26064546/)) |
| `bio:HUMAN-OVIDUCT-CILIA-BEAT` | R | Ciliary beat frequency in the human fallopian tube: 5.3 Hz (mean; n = 26 women (14 in the proliferative, 12 in the secretory phase)). | Lyons et al. 2002, Human Reproduction 17(3):584-588 ([doi:10.1093/humrep/17.3.584](https://doi.org/10.1093/humrep/17.3.584), [PMID 11870107](https://pubmed.ncbi.nlm.nih.gov/11870107/)); Bylander et al. 2010, Reproductive Biology and Endocrinology 8:48 ([doi:10.1186/1477-7827-8-48](https://doi.org/10.1186/1477-7827-8-48), [PMID 20470431](https://pubmed.ncbi.nlm.nih.gov/20470431/)) |
| `bio:MOUSE-OVIDUCT-CILIA-BEAT` | R | Ciliary beat frequency in the mouse fallopian tube: 23.3 Hz (mean; n = 19 mice). | Bylander et al. 2010, Reproductive Biology and Endocrinology 8:48 ([doi:10.1186/1477-7827-8-48](https://doi.org/10.1186/1477-7827-8-48), [PMID 20470431](https://pubmed.ncbi.nlm.nih.gov/20470431/)) |
| `bio:HUMAN-UTERINE-CONTRACTIONS-LATE-FOLLICULAR` | R | Human uterine contraction frequency in the late follicular phase: 1.61 per min (as reported; n = 70 recordings analysed across all phases together, of 96 from 64 healthy women with natural cycles; the number in each phase is not recorded here). | Rees et al. 2023, Reproductive BioMedicine Online 46(1):115-122 ([doi:10.1016/j.rbmo.2022.08.104](https://doi.org/10.1016/j.rbmo.2022.08.104), [PMID 36244894](https://pubmed.ncbi.nlm.nih.gov/36244894/)) |
| `bio:HUMAN-UTERINE-CONTRACTIONS-MENSTRUAL` | R | Human uterine contraction frequency in the menstrual phase: 1.31 per min (as reported; n = 70 recordings analysed across all phases together, of 96 from 64 healthy women with natural cycles; the number in each phase is not recorded here). | Rees et al. 2023, Reproductive BioMedicine Online 46(1):115-122 ([doi:10.1016/j.rbmo.2022.08.104](https://doi.org/10.1016/j.rbmo.2022.08.104), [PMID 36244894](https://pubmed.ncbi.nlm.nih.gov/36244894/)) |
| `bio:HUMAN-UTERINE-CONTRACTIONS-LATE-LUTEAL` | R | Human uterine contraction frequency in the late luteal phase: 1.35 per min (as reported; n = 70 recordings analysed across all phases together, of 96 from 64 healthy women with natural cycles; the number in each phase is not recorded here). | Rees et al. 2023, Reproductive BioMedicine Online 46(1):115-122 ([doi:10.1016/j.rbmo.2022.08.104](https://doi.org/10.1016/j.rbmo.2022.08.104), [PMID 36244894](https://pubmed.ncbi.nlm.nih.gov/36244894/)) |
| `bio:HUMAN-EMBRYO-T2` | R | Time from insemination to the 2-cell stage (t2) in human embryos: 27.48 h (mean; n = 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here)). | Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction 30(2):258-267 ([doi:10.5935/1518-0557.20260005](https://doi.org/10.5935/1518-0557.20260005), [PMID 41842690](https://pubmed.ncbi.nlm.nih.gov/41842690/)) |
| `bio:HUMAN-EMBRYO-T3` | R | Time from insemination to the 3-cell stage (t3) in human embryos: 37.78 h (mean; n = 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here)). | Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction 30(2):258-267 ([doi:10.5935/1518-0557.20260005](https://doi.org/10.5935/1518-0557.20260005), [PMID 41842690](https://pubmed.ncbi.nlm.nih.gov/41842690/)) |
| `bio:HUMAN-EMBRYO-T4` | R | Time from insemination to the 4-cell stage (t4) in human embryos: 40.4 h (mean; n = 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here)). | Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction 30(2):258-267 ([doi:10.5935/1518-0557.20260005](https://doi.org/10.5935/1518-0557.20260005), [PMID 41842690](https://pubmed.ncbi.nlm.nih.gov/41842690/)) |
| `bio:HUMAN-EMBRYO-T5` | R | Time from insemination to the 5-cell stage (t5) in human embryos: 51.04 h (mean; n = 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here)). | Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction 30(2):258-267 ([doi:10.5935/1518-0557.20260005](https://doi.org/10.5935/1518-0557.20260005), [PMID 41842690](https://pubmed.ncbi.nlm.nih.gov/41842690/)) |
| `bio:HUMAN-EMBRYO-T6` | R | Time from insemination to the 6-cell stage (t6) in human embryos: 54.25 h (mean; n = 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here)). | Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction 30(2):258-267 ([doi:10.5935/1518-0557.20260005](https://doi.org/10.5935/1518-0557.20260005), [PMID 41842690](https://pubmed.ncbi.nlm.nih.gov/41842690/)) |
| `bio:HUMAN-EMBRYO-T7` | R | Time from insemination to the 7-cell stage (t7) in human embryos: 57.57 h (mean; n = 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here)). | Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction 30(2):258-267 ([doi:10.5935/1518-0557.20260005](https://doi.org/10.5935/1518-0557.20260005), [PMID 41842690](https://pubmed.ncbi.nlm.nih.gov/41842690/)) |
| `bio:HUMAN-EMBRYO-T8` | R | Time from insemination to the 8-cell stage (t8) in human embryos: 61.51 h (mean; n = 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here)). | Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction 30(2):258-267 ([doi:10.5935/1518-0557.20260005](https://doi.org/10.5935/1518-0557.20260005), [PMID 41842690](https://pubmed.ncbi.nlm.nih.gov/41842690/)) |
| `bio:HUMAN-EMBRYO-TM` | R | Time from insemination to compaction (tM, morula) in human embryos: 87.75 h (mean; n = 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here)). | Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction 30(2):258-267 ([doi:10.5935/1518-0557.20260005](https://doi.org/10.5935/1518-0557.20260005), [PMID 41842690](https://pubmed.ncbi.nlm.nih.gov/41842690/)) |
| `bio:HUMAN-EMBRYO-TSB` | R | Time from insemination to the start of blastulation (tSB) in human embryos: 99.18 h (mean; n = 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here)). | Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction 30(2):258-267 ([doi:10.5935/1518-0557.20260005](https://doi.org/10.5935/1518-0557.20260005), [PMID 41842690](https://pubmed.ncbi.nlm.nih.gov/41842690/)) |
| `bio:HUMAN-EMBRYO-TB` | R | Time from insemination to the full blastocyst (tB) in human embryos: 104.5 h (mean; n = 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here)). | Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction 30(2):258-267 ([doi:10.5935/1518-0557.20260005](https://doi.org/10.5935/1518-0557.20260005), [PMID 41842690](https://pubmed.ncbi.nlm.nih.gov/41842690/)) |
| `bio:HUMAN-EMBRYO-TEB` | R | Time from insemination to the expanded blastocyst (tEB) in human embryos: 110.82 h (mean; n = 2,523 correctly fertilised oocytes in the fresh-sperm group (the group size, not the number of embryos timed at each stage, which is not recorded here)). | Lorenzo Rodríguez et al. 2026, JBRA Assisted Reproduction 30(2):258-267 ([doi:10.5935/1518-0557.20260005](https://doi.org/10.5935/1518-0557.20260005), [PMID 41842690](https://pubmed.ncbi.nlm.nih.gov/41842690/)) |
| `bio:HUMAN-EHR-6W` | R | Median human embryonic heart rate at 6 weeks of gestation: 117 bpm (median; n = 20,272 pregnancies measured in this gestational week (Table 3 of the paper; 30,416 across weeks 6-10)). | Ouyang et al. 2020, BMC Pregnancy and Childbirth 20:533 ([doi:10.1186/s12884-020-03186-2](https://doi.org/10.1186/s12884-020-03186-2), [PMID 32928137](https://pubmed.ncbi.nlm.nih.gov/32928137/)) |
| `bio:HUMAN-EHR-7W` | R | Median human embryonic heart rate at 7 weeks of gestation: 146 bpm (median; n = 2,969 pregnancies measured in this gestational week (Table 3 of the paper; 30,416 across weeks 6-10)). | Ouyang et al. 2020, BMC Pregnancy and Childbirth 20:533 ([doi:10.1186/s12884-020-03186-2](https://doi.org/10.1186/s12884-020-03186-2), [PMID 32928137](https://pubmed.ncbi.nlm.nih.gov/32928137/)) |
| `bio:HUMAN-EHR-8W` | R | Median human embryonic heart rate at 8 weeks of gestation: 174 bpm (median; n = 4,109 pregnancies measured in this gestational week (Table 3 of the paper; 30,416 across weeks 6-10)). | Ouyang et al. 2020, BMC Pregnancy and Childbirth 20:533 ([doi:10.1186/s12884-020-03186-2](https://doi.org/10.1186/s12884-020-03186-2), [PMID 32928137](https://pubmed.ncbi.nlm.nih.gov/32928137/)) |
| `bio:HUMAN-EHR-9W` | R | Median human embryonic heart rate at 9 weeks of gestation: 176 bpm (median; n = 2,267 pregnancies measured in this gestational week (Table 3 of the paper; 30,416 across weeks 6-10)). | Ouyang et al. 2020, BMC Pregnancy and Childbirth 20:533 ([doi:10.1186/s12884-020-03186-2](https://doi.org/10.1186/s12884-020-03186-2), [PMID 32928137](https://pubmed.ncbi.nlm.nih.gov/32928137/)) |
| `bio:HUMAN-EHR-10W` | R | Median human embryonic heart rate at 10 weeks of gestation: 174 bpm (median; n = 799 pregnancies measured in this gestational week (Table 3 of the paper; 30,416 across weeks 6-10)). | Ouyang et al. 2020, BMC Pregnancy and Childbirth 20:533 ([doi:10.1186/s12884-020-03186-2](https://doi.org/10.1186/s12884-020-03186-2), [PMID 32928137](https://pubmed.ncbi.nlm.nih.gov/32928137/)) |
| `bio:HUMAN-SEGMENTATION-CLOCK-PERIOD` | R | Period of the human segmentation clock in presomitic mesoderm cells derived in vitro: 5 h (approximate). | Matsuda et al. 2020, Nature 580:124-129 ([doi:10.1038/s41586-020-2144-9](https://doi.org/10.1038/s41586-020-2144-9), [PMID 32238941](https://pubmed.ncbi.nlm.nih.gov/32238941/)); Diaz-Cuadros et al. 2020, Nature 580:113-118 ([doi:10.1038/s41586-019-1885-9](https://doi.org/10.1038/s41586-019-1885-9), [PMID 31915384](https://pubmed.ncbi.nlm.nih.gov/31915384/)); Matsuda et al. 2020, Science 369:1450-1455 ([doi:10.1126/science.aba7668](https://doi.org/10.1126/science.aba7668), [PMID 32943519](https://pubmed.ncbi.nlm.nih.gov/32943519/)); Diaz-Cuadros et al. 2026, Nature 654:E13 (Author Correction) ([doi:10.1038/s41586-026-10651-z](https://doi.org/10.1038/s41586-026-10651-z)) |
| `bio:MOUSE-SEGMENTATION-CLOCK-PERIOD` | R | Period of the mouse segmentation clock in presomitic mesoderm cells derived in vitro: 2–3 h (range). | Matsuda et al. 2020, Science 369:1450-1455 ([doi:10.1126/science.aba7668](https://doi.org/10.1126/science.aba7668), [PMID 32943519](https://pubmed.ncbi.nlm.nih.gov/32943519/)); Diaz-Cuadros et al. 2020, Nature 580:113-118 ([doi:10.1038/s41586-019-1885-9](https://doi.org/10.1038/s41586-019-1885-9), [PMID 31915384](https://pubmed.ncbi.nlm.nih.gov/31915384/)); Diaz-Cuadros et al. 2026, Nature 654:E13 (Author Correction) ([doi:10.1038/s41586-026-10651-z](https://doi.org/10.1038/s41586-026-10651-z)) |
| `bio:HUMAN-MAJOR-ZGA-STAGE` | R | Cell stage of major embryonic genome activation in human embryos: 4–8 cells (range). | Braude et al. 1988, Nature 332:459-461 ([doi:10.1038/332459a0](https://doi.org/10.1038/332459a0), [PMID 3352746](https://pubmed.ncbi.nlm.nih.gov/3352746/)); Asami et al. 2022, Cell Stem Cell 29(2):209-216 ([doi:10.1016/j.stem.2021.11.012](https://doi.org/10.1016/j.stem.2021.11.012), [PMID 34936886](https://pubmed.ncbi.nlm.nih.gov/34936886/)) |
| `bio:HUMAN-MINOR-ZGA-STAGE` | R | Cell stage at which human embryonic transcription begins (minor genome activation): 1 cell (observed). | Asami et al. 2022, Cell Stem Cell 29(2):209-216 ([doi:10.1016/j.stem.2021.11.012](https://doi.org/10.1016/j.stem.2021.11.012), [PMID 34936886](https://pubmed.ncbi.nlm.nih.gov/34936886/)) |
| `bio:MOUSE-MAJOR-ZGA-STAGE` | R | Cell stage of major zygotic genome activation in mouse embryos: 2 cells (as reported). | Aoki 2022, Journal of Reproduction and Development 68(2):79-84 ([doi:10.1262/jrd.2021-129](https://doi.org/10.1262/jrd.2021-129), [PMID 35034936](https://pubmed.ncbi.nlm.nih.gov/35034936/)); Braude et al. 1988, Nature 332:459-461 ([doi:10.1038/332459a0](https://doi.org/10.1038/332459a0), [PMID 3352746](https://pubmed.ncbi.nlm.nih.gov/3352746/)) |
| `bio:MOUSE-MINOR-ZGA-STAGE` | R | Cell stage of minor zygotic genome activation in mouse embryos: 1 cell (as reported). | Aoki 2022, Journal of Reproduction and Development 68(2):79-84 ([doi:10.1262/jrd.2021-129](https://doi.org/10.1262/jrd.2021-129), [PMID 35034936](https://pubmed.ncbi.nlm.nih.gov/35034936/)) |
<!-- claims-table:end -->

Levels: **P** machine-checked proof (Lean 4) · **V** verified numerics · **T** tested · **R** referenced (DOI or PMID) · **M** model assumption.

## Use

**Rust**

```toml
[dependencies]
biological-rhythms-dataset = { git = "https://github.com/chethandvg/biological-rhythms-dataset", tag = "v0.1.0" }
```

```rust
use biological_rhythms_dataset::{cell_count_at, frequency_hz, get, heart_rate_at};

let ca = get("bio:HUMAN-CA-SPIKE-INTERVAL")?;
println!("{}: {:?}-{:?} min, {}", ca.quantity, ca.min, ca.max, ca.sources[0].cite);

let hz = frequency_hz("bio:HUMAN-CA-SPIKE-INTERVAL")?; // 1/2100 to 1/600 Hz
let bpm = heart_rate_at(8.0)?; // 160.0, halfway between the 7- and 8-week medians, placed at 7.5 and 8.5
let cells = cell_count_at(48.0)?; // 4: after t4 (40.4 h), before t5 (51.04 h)
```

**Python** (builds the Rust core with maturin)

```bash
pip install "git+https://github.com/chethandvg/biological-rhythms-dataset@v0.1.0#subdirectory=bindings/python"
```

```python
import biological_rhythms_dataset as bio

beat = bio.get("bio:HUMAN-SPERM-BEAT-VISCOUS")
beat["value"], beat["unit"], beat["n"]  # (10.0, 'Hz', 119)
bio.frequency_hz("bio:HUMAN-EHR-9W")  # (2.933..., 2.933...): 176 bpm
bio.heart_rate_at(8.0)  # 160.0
bio.cell_count_at(48.0)  # 4
len(bio.rhythms())  # 40
```

**JavaScript / WebAssembly** (see [bindings/wasm](bindings/wasm))

```js
const bio = require("./pkg/node/biological_rhythms_dataset_wasm.js");

bio.get("bio:MOUSE-CA-SPIKE-INTERVAL").value; // 3.4 (minutes)
bio.frequency_hz("bio:HUMAN-CA-SPIKE-INTERVAL"); // Float64Array [0.000476..., 0.001666...]
bio.heart_rate_at(9.0); // 175, halfway between the 8- and 9-week medians
```

Every function has the same name in all three languages. Lookups of an unknown id raise `KeyError` in Python; any other invalid input raises `ValueError` in Python and throws an `Error` in JavaScript.

| Function | Returns |
|---|---|
| `rhythms()` | Every record, in the order of `data/rhythms.yaml`. |
| `get(id)` | The record with this claim id. |
| `frequency_hz(id)` | The frequency range in hertz of a period, frequency or rate, converted with [rhythm-units](https://github.com/chethandvg/rhythm-units). Durations, time points, stages and counts are rejected. |
| `heart_rate_at(weeks)` | Median human embryonic heart rate in bpm. The median of gestational week w is placed at w + 0.5, the middle of the week (an assumption: `bio:HEART-RATE-WEEK-PLACEMENT`), and the rate is interpolated linearly between neighbouring medians; weeks outside 6.5 to 10.5 are rejected. |
| `cell_count_at(hours)` | Cells in the mean human embryo that many hours after insemination, as a step function over t2 to t8; hours below 0 or after t8 are rejected. |

## How it is verified

- **Sources:** every value was taken from the project's fact-checked research notes, which read the papers; values that appear in an abstract were checked against it again, each DOI was checked against Crossref and each PMID against PubMed. The weekly `hygiene` workflow runs `ek resolve`, which fails if any cited paper is retracted or withdrawn; corrections and other notices registered with Crossref are listed without failing.
- **Data:** [`scripts/build.py --check`](scripts/build.py) runs in CI. It validates `data/rhythms.yaml` and `data/sources.yaml` against their JSON Schemas, checks that each record's id and description name one species and that every source key exists, and fails if the JSON, the CSV, the R claims or the tables above differ from what the YAML generates.
- **Proofs:** the Lean 4 file [`proofs/BiologicalRhythmsDataset/Interpolation.lean`](proofs/BiologicalRhythmsDataset/Interpolation.lean) proves that linear interpolation returns each measurement at its own week and stays between the two measurements around it. CI rebuilds it with Mathlib, rejects `sorry`, and allows only the standard axioms (`propext`, `Classical.choice`, `Quot.sound`).
- **Implementation:** one Rust implementation, compiled to Python (PyO3) and WebAssembly. The golden vectors in [`vectors/`](vectors) come from an independent Python oracle that reads `data/rhythms.yaml` and computes every helper result with exact fractions; all three implementations must reproduce them. CI tests Rust and Python on Linux and Windows, and WebAssembly on Linux only.
- **What this does not cover:** the proofs are about exact real numbers, not the biology, and not floating point; Rust's rounding is checked by the golden-vector tolerances, and its interpolation is clamped so it cannot leave the bracketing medians. No test can show that a paper measured the right thing. Each value is only as good as its source: several come from small samples, from eggs activated without sperm, or from cells grown in a dish, and the notes say so. The helpers describe the mean embryo; individual embryos vary by hours. `heart_rate_at` also rests on an assumption, the M claim `bio:HEART-RATE-WEEK-PLACEMENT`: Ouyang et al. use the gestational day divided by 7 as the gestational week, but their methods state no rule for assigning scans to whole weeks, and the dataset places each weekly median at mid-week because the paper's own fitted curve matches the medians there (within 5 bpm) but not at the whole week (up to 18 bpm off).

## Cite

If you use this work, please cite it. GitHub's **Cite this repository** button gives APA and BibTeX from [CITATION.cff](CITATION.cff). When you use a value, please also cite the paper it comes from, listed with each record.

## Licence

Code: free for non-commercial use under the PolyForm Noncommercial License 1.0.0 ([LICENSE](LICENSE)). For commercial use, see [COMMERCIAL.md](COMMERCIAL.md). Data (`data/`, `schema/` and the generated files), articles, figures and audio: CC BY-NC 4.0 ([LICENSES/CC-BY-NC-4.0.txt](LICENSES/CC-BY-NC-4.0.txt)). The measurements themselves are facts reported in the cited papers; the licence covers this compilation. Copyright notices are in [NOTICE](NOTICE).
