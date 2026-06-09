# Architecture v0.2

This version reflects the updated source-of-truth policy:

- HTML artifact is the canonical source
- rendered HTML is the visual reference
- PPTX is the evaluation surface
- multimodal feedback is a correction layer for revised HTML generation

## 1. High-level mechanism

```mermaid
flowchart TD
    A[HTML artifact] --> B[Runtime render / Playwright]
    B --> C[Measured DOM extraction]
    C --> D[Visual Object IR]
    D --> E[Semantic candidate classifier]
    E --> F[Native / split / fallback decision]
    F --> G[PPT IR]
    G --> H[PPTX compiler]
    H --> I[Rendered PPTX]

    B --> J[Rendered HTML reference]
    I --> K[Validation runner]
    J --> K

    K --> L[Validation / loss report]
    L --> M[Textual or multimodal feedback]
    M --> N[Revised HTML artifact]
    N --> B
```

## 2. Layered module design

```mermaid
flowchart LR
    subgraph SourceLayer[Source Layer]
        A1[HTML artifact]
        A2[CSS]
        A3[JS runtime state]
        A4[External assets]
    end

    subgraph RenderLayer[Render Layer]
        B1[Playwright]
        B2[DOM traversal]
        B3[getBoundingClientRect]
        B4[getComputedStyle]
    end

    subgraph IRLayer[IR Layer]
        C1[Measured visual nodes]
        C2[Visual Object IR]
        C3[Reading order resolver]
        C4[Z-order resolver]
        C5[Semantic candidate classifier]
    end

    subgraph MappingLayer[Mapping Layer]
        D1[Text run collector]
        D2[Shape mapper]
        D3[Table detector / mapper]
        D4[Chart semantic extractor]
        D5[Fallback policy engine]
        D6[PPT IR]
    end

    subgraph OutputLayer[Output Layer]
        E1[PPTX compiler]
        E2[Rendered PPTX]
    end

    subgraph ReviewLayer[Review Layer]
        F1[Validation runner]
        F2[Loss report]
        F3[Textual feedback]
        F4[Multimodal critic]
        F5[HTML revision loop]
    end

    SourceLayer --> RenderLayer --> IRLayer --> MappingLayer --> OutputLayer --> ReviewLayer
    ReviewLayer --> SourceLayer
```

## 3. Third-party integration architecture

```mermaid
flowchart TD
    subgraph RuntimeBackends[Runtime Backends]
        A1[pixelmatch subtree]
        A2[odiff-bin subtree]
        A3[looks-same dependency]
        A4[PptxGenJS dependency]
    end

    subgraph ReferenceAssets[Reference Assets]
        B1[ODL schema sync]
        B2[ODL options sync]
        B3[ODL processor reference]
        B4[Docling pipeline reference]
    end

    subgraph NativeProject[Project Core]
        C1[Measured DOM Extractor]
        C2[Visual Object IR]
        C3[Classifier]
        C4[Mapper / Fallback]
        C5[PPTX Compiler]
        C6[Validator]
    end

    B1 --> C2
    B2 --> C4
    B3 --> C3
    B4 --> C3

    C1 --> C2 --> C3 --> C4 --> C5 --> C6

    A1 --> C6
    A2 --> C6
    A3 --> C6
    A4 --> C5
```

## 4. Design authority

The architecture should also include a design authority layer, even if implemented incrementally.

Its role is to preserve consistency across iterations:

- spacing scale
- typography scale
- radius scale
- color/token policy
- component recipe selection
- fallback style consistency

## 5. Compiler rule

The final PPT compiler must remain deterministic.

Preferred split of responsibilities:

- deterministic compiler -> final PPT objects and package generation
- multimodal layer -> visual critique, localization, and revision suggestions
