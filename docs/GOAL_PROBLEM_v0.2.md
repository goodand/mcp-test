# Goal / Problem v0.2

## 1. Problem statement

We want to compile an HTML artifact into an editable PPTX while preserving as much semantic structure and visual intent as possible.

The input should be treated as:

```text
HTML artifact + rendered runtime state
```

not as a screenshot-only source.

## 2. Core problem

There is a structural mismatch between:

- HTML / CSS / JS-rendered layout
- PowerPoint's native object model

Therefore the system must not map DOM nodes directly to PPT objects.

Preferred progression:

```text
HTML artifact
  -> measured visual nodes
  -> Visual Object IR
  -> semantic candidates
  -> native / split / fallback decision
  -> PPTX objects
```

## 3. Immediate technical questions

The system must answer:

1. What is the canonical authoring source?
   - Answer: HTML artifact
2. What is the evaluation surface?
   - Answer: PPTX and rendered validation output
3. What triggers a revised artifact?
   - Answer: textual or multimodal feedback
4. How is loss handled?
   - Answer: explicit fallback policy and validation report

## 4. Required module roles

### Native project roles

1. Runtime rendering / measurement
2. Measured DOM extractor
3. Visual Object IR normalizer
4. Semantic candidate classifier
5. Text run collector
6. Shape mapper
7. Table detector / native table mapper
8. Chart semantic extractor
9. Fallback policy engine
10. PPTX compiler
11. Validation runner
12. Loss / editability report generator
13. HTML revision loop support
14. Multimodal critic / patch suggestion layer

### Key distinction

The final compiler should stay deterministic.
Multimodal reasoning should act as:

- critic
- classifier correction layer
- issue localizer
- patch suggester for the next HTML artifact

## 5. Reusable module slots

### Slot A — validation backend
Candidates:

- `mapbox/pixelmatch`
- `dmtrKovalenko/odiff` (`npm_packages/odiff-bin` boundary)
- `gemini-testing/looks-same`

### Slot B — HTML to PPT mapping reference
Candidates:

- `atharva9167j/dom-to-pptx`
- `gitbrent/PptxGenJS`

### Slot C — semantic IR schema reference
Candidates:

- `opendataloader-project/opendataloader-pdf`
- `docling-project/docling`

### Slot D — processor-chain / pipeline reference
Candidates:

- `opendataloader-project/opendataloader-pdf`
- `docling-project/docling`

## 6. How the two reference repos are used

### opendataloader-pdf
Use as reference for:

- bbox-aware semantic schema
- deterministic processor chain
- semantic dispatch / generator pattern
- options and policy surface

Immediate reusable assets:

- `schema.json`
- `options.json`
- processor design from `DocumentProcessor`
- semantic writer pattern from `HtmlGenerator`

### docling
Use as reference for:

- conversion entrypoint and format routing
- unified document object model
- staged threaded pipeline design
- plugin / model registry pattern

Immediate reusable references:

- `DocumentConverter`
- `DoclingDocument` / `ConversionResult`
- `StandardPdfPipeline`
- `models/plugins/defaults.py`

## 7. Third-party import policy

The project uses four import modes:

- `clone` — full-read analysis and evaluation
- `subtree` — adopted runtime modules with a stable working boundary
- `package_dependency` — when upstream packaging is cleaner than vendoring
- `sync_reference` — schemas, options, and static reference assets

## 8. Current direction

### Adopt subtree

- `pixelmatch` -> whole repo subtree
- `odiff-bin` -> split-subdir subtree

### Package dependency

- `looks-same`
- `PptxGenJS`

### Reference / sync

- `opendataloader-pdf` -> sync `schema.json`, `options.json` + code reference
- `docling` -> reference-only or package dependency for experiments

### Deferred

- `dom-to-pptx`

## 9. Reference-only rule

Large framework / research repos are not immediately vendored.

However, `reference-only` is **not a terminal state**.
It is a scouting state for future subtree adoption.

Each reference-only repo must have:

- candidate source paths
- current blockers
- subtree trigger conditions
- next review step
