# Third-Party Strategy Plan v0.2

## Goal

Move from a clone-only third-party workflow to a mixed integration strategy aligned with the HTML-source-of-truth architecture.

## Core policy

- use `clone` for full-read analysis
- use `git subtree` for adopted runtime modules with a stable working boundary
- use package dependencies when upstream packaging is cleaner than vendoring
- use sync/reference for schemas, options, and static reference assets

## Additional policy

Large framework or research repos should not be adopted immediately.

However, `reference-only` is **not** a terminal state.
It is a temporary scouting state for future subtree adoption.

Every reference-only repo must maintain:

- candidate source paths
- current blockers
- subtree trigger conditions
- next review step

## Current target classification

### Subtree targets

- `mapbox/pixelmatch` -> whole repo subtree
- `dmtrKovalenko/odiff` -> `npm_packages/odiff-bin` subtree

### Package dependencies

- `gemini-testing/looks-same`
- `gitbrent/PptxGenJS`

### Sync/reference

- `opendataloader-project/opendataloader-pdf`
  - sync `schema.json`
  - sync `options.json`
  - reference processor chain and writer pattern
- `docling-project/docling`
  - reference conversion entrypoint, object model, threaded pipeline, plugin registry

### Deferred

- `atharva9167j/dom-to-pptx`

## Execution order

1. restore and point project docs to v0.2
2. add `subtree_module_inventory_v0.2.md`
3. add `third_party/subtrees.toml`
4. add `sync_opendataloader_pdf_refs.sh`
5. adopt `pixelmatch` subtree
6. adopt `odiff-bin` subtree
7. keep `looks-same` as dependency
8. sync `opendataloader-pdf` reference assets
9. keep `docling` as reference-only while scouting subtree boundaries

## Success criteria

A successful migration means:

- the repo documents HTML as the canonical source of truth
- runtime diff backends are clearly separated from reference frameworks
- schema/options references are versioned inside the repo
- every reference-only repo has a subtree scouting record
- adopted modules have explicit subtree boundaries and validation commands
