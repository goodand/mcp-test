# Ultimate Goal v0.2

## 1. Goal

The project goal is to turn an HTML artifact into an editable PPTX while keeping **HTML as the canonical source of truth**.

The project does **not** treat PPTX as the primary authoring source. PPTX is the presentation, evaluation, and interaction surface.

## 2. Source-of-truth model

```text
HTML artifact
  -> render in browser/runtime sandbox
  -> extract measured visual structure
  -> compile to editable PPTX
  -> review in PPT / rendered validation view
  -> textual or multimodal feedback
  -> revised HTML artifact
```

This means:

- HTML is the canonical artifact
- rendered HTML is the visual reference
- PPTX is the editable delivery surface
- feedback should produce a **new HTML artifact**, not a hidden PPT-only state

## 3. Why this model

HTML/CSS/JS can express more layout and styling behavior than native PPT objects.
Therefore the system must:

1. preserve as much editability as possible,
2. explicitly account for loss when native mapping is impossible,
3. use rendered validation and multimodal review to guide the next HTML revision.

## 4. User interaction loop

```text
LLM / agent generates HTML
  -> user views PPT output and rendered diffs
  -> user gives textual or multimodal feedback
  -> system revises HTML
  -> system recompiles PPTX
```

The loop should remain traceable:

- which HTML artifact produced which PPTX
- which feedback caused which HTML revision
- which objects became native PPT objects
- which regions fell back to assets

## 5. In-scope outcomes

The system should aim to produce native editable PPT objects for:

- text
- rich text runs
- shapes
- tables
- charts where semantic recovery is available

The system may keep the following as asset-backed output when necessary:

- PNG / JPG / GIF
- complex SVG effects
- video thumbnails
- visual effects that do not map reliably to PPT

## 6. Multimodal role

Multimodal reasoning is used as a **correction and review layer**, not as the primary compiler.

Preferred role:

- visual critic
- issue localizer
- semantic guess correction
- patch suggester for the next HTML artifact

Not preferred role:

- nondeterministic final PPT compiler
- hidden state mutation without artifact revision

## 7. Non-goals

- Do not treat PPT as the long-term source of truth.
- Do not require perfect round-trip fidelity from PPT back to HTML.
- Do not silently rasterize everything.
- Do not rely only on screenshots when code/source structure is available.

## 8. Success criteria

A successful system:

- keeps HTML as the canonical editable source,
- produces an editable PPTX where possible,
- explains losses and fallbacks,
- supports a feedback loop that results in a revised HTML artifact,
- preserves design consistency across iterations.
