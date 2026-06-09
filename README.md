# html-to-editable-pptx

Editability-first HTML to PPTX compiler project.

The current project direction is:

- **HTML artifact is the source of truth**
- **rendered HTML is the visual reference**
- **PPTX is an evaluation and interaction surface**
- **textual or multimodal feedback produces a revised HTML artifact**

Read the current versioned documents:

```text
docs/ULTIMATE_GOAL_v0.2.md
docs/GOAL_PROBLEM_v0.2.md
docs/architecture_v0.2.md
docs/subtree_module_inventory_v0.2.md
docs/third_party_strategy_plan_v0.2.md
```

Third-party integration follows a mixed policy:

- `clone` for full-read analysis
- `git subtree` for adopted runtime modules
- package dependencies when upstream packaging is cleaner than vendoring
- sync/reference for schemas, options, and static reference assets

Current integration direction:

- `pixelmatch` -> subtree candidate / primary validation backend
- `odiff-bin` -> subtree candidate / high-performance validation backend
- `looks-same` -> package dependency candidate
- `opendataloader-pdf` -> schema/options/processors reference
- `docling` -> conversion/pipeline/object-model reference

The repository is still in bootstrap phase. The immediate goal is to define the source-of-truth model, the mixed third-party import policy, and a minimal validated conversion path.
