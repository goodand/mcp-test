# Subtree Module Inventory v0.2

## Purpose

This document records third-party module boundary decisions.

Import modes:

- `whole_repo`
- `split_subdir`
- `package_dependency`
- `sync_reference`
- `reference_only`

Decision states:

- `reference_only_now`
- `subtree_candidate`
- `subtree_ready`
- `adopt_subtree`
- `package_dependency_now`
- `defer`
- `reject`

`reference_only_now` is **not** a terminal state.
It is a scouting state for future subtree adoption.

---

## pixelmatch

- upstream: `mapbox/pixelmatch`
- role: pixel-level validation core
- working boundary: repo root
- entrypoint: `index.js`
- tests: `test/test.js`
- decision: `adopt_subtree`
- import_mode: `whole_repo`
- subtree_prefix: `third_party/subtrees/pixelmatch`

Why:
- small root package
- deterministic comparator
- clear package/build/test boundary

---

## odiff-bin

- upstream: `dmtrKovalenko/odiff`
- role: high-performance diff backend
- working boundary: `npm_packages/odiff-bin`
- entrypoint: `npm_packages/odiff-bin/odiff.js`
- decision: `adopt_subtree`
- import_mode: `split_subdir`
- subtree_prefix: `third_party/subtrees/odiff-bin`

Why:
- upstream root is a private monorepo
- real runtime boundary is the `odiff-bin` workspace package

---

## looks-same

- upstream: `gemini-testing/looks-same`
- role: perceptual PNG diff backend
- working boundary: repo root
- entrypoint: `index.js`
- decision: `package_dependency_now`
- import_mode: `package_dependency`

Why:
- clean root package
- useful alternative comparator
- overlaps enough with `pixelmatch` that subtree is unnecessary for now

---

## dom-to-pptx

- upstream: `atharva9167j/dom-to-pptx`
- role: HTML/DOM to PPT mapping reference / candidate
- working boundary: repo root
- effective source entrypoint: `src/index.js`
- build entrypoint: `rollup.config.js -> src/index.js`
- decision: `defer`
- import_mode: `whole_repo`
- subtree_prefix: `third_party/subtrees/dom-to-pptx`

Why:
- official upstream package boundary is root package
- internal modules are tightly coupled
- if patched later, vendoring the whole package is safer than splitting

---

## opendataloader-pdf

- upstream: `opendataloader-project/opendataloader-pdf`
- current status: `reference_only_now`
- import_mode: `sync_reference`

Immediate reference assets:

- `schema.json`
- `options.json`
- processor design from `DocumentProcessor`
- semantic writer pattern from `HtmlGenerator`

Subtree scouting:

- candidate_source_paths:
  - `java/opendataloader-pdf-core`
  - `node/opendataloader-pdf`
- current_blockers:
  - root is a workspace, not a small runtime package
  - node package is a Java CLI wrapper, not parser core
  - immediate need is schema/options, not runtime embedding
- subtree_trigger:
  - local patching of processor-chain logic is needed
  - Java processor code must be adapted locally
- next_review_step:
  - inspect `java/opendataloader-pdf-core` as a future `split_subdir` candidate

---

## docling

- upstream: `docling-project/docling`
- current status: `reference_only_now`
- import_mode: `reference_only`

Immediate references:

- `DocumentConverter`
- `DoclingDocument`
- `ConversionResult`
- `StandardPdfPipeline`
- `models/plugins/defaults.py`

Subtree scouting:

- candidate_source_paths:
  - `docling/`
  - whole repo
- current_blockers:
  - broad package boundary
  - large pipeline/model/plugin surface
  - current use is architectural reference, not runtime embedding
- subtree_trigger:
  - local patching of pipeline internals is needed
  - package dependency becomes insufficient
- next_review_step:
  - inspect `docling/` package-only viability versus whole-repo subtree

---

## BackstopJS

- current status: `reference_only_now`
- import_mode: `reference_only`
- subtree scouting:
  - candidate_source_paths:
    - `compare/`
    - `core/`
    - `cli/`
  - current_blockers:
    - full CLI app, not a small reusable comparator module
  - next_review_step:
    - inspect whether any compare-only sub-boundary is worth extracting

---

## table-transformer

- current status: `reference_only_now`
- import_mode: `reference_only`
- subtree scouting:
  - candidate_source_paths:
    - `src/` inference path
  - current_blockers:
    - research/training/inference repo
    - large model/runtime footprint
  - next_review_step:
    - inspect inference-only boundary as a future service/module candidate
