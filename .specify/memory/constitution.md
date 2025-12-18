<!--
---
Sync Impact Report:
- Version change: 0.0.0 → 1.0.0
- List of modified principles:
  - [PRINCIPLE_1_NAME] → Technical Accuracy
  - [PRINCIPLE_2_NAME] → Engineering Clarity
  - [PRINCIPLE_3_NAME] → Embodiment-First Thinking
  - [PRINCIPLE_4_NAME] → Reproducibility
- Added sections:
  - Key Standards
  - Constraints & Quality Guardrails
  - Success Criteria
- Removed sections:
  - N/A
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
---
-->
# AI/Spec-Driven Book Creation — Physical AI & Humanoid Robotics

## Core Principles

### I. Technical Accuracy
All robotics, AI, and simulation concepts must align with official documentation or peer-reviewed research. All factual claims must be traceable.

### II. Engineering Clarity
Content is written for senior undergraduate, graduate, and professional AI/robotics learners. The target writing clarity is Flesch-Kincaid grade level 11–13.

### III. Embodiment-First Thinking
Intelligence must always be grounded in physical constraints such as physics, sensing, latency, control, and actuation.

### IV. Reproducibility
All system architectures, pipelines, and workflows must be conceptually reproducible by readers. Code examples must be conceptually correct and idiomatic for the target platform.

## Key Standards

- **Traceability**: All factual claims must be traceable to one of the following:
  - Official documentation (ROS 2, Gazebo, Unity, NVIDIA Isaac)
  - Peer-reviewed robotics or AI research
- **Citations**: All citations must use APA style.
- **Source Mix**: A minimum of 50% of sources must be from peer-reviewed research papers. The remainder may be from official SDK or platform documentation.

## Constraints & Quality Guardrails

- **Format**: The final output must be a single instructional textbook in Docusaurus-compatible Markdown with a chapter-based structure.
- **Code**: All code must be in Python (for ROS 2, rclpy, AI pipelines) or YAML (for ROS configuration and launch files). No raw HTML or JSX is permitted.
- **Diagrams**: All diagrams must be described textually. ASCII or Mermaid-compatible formats are required.
- **Integrity**: There must be zero hallucinated APIs or fake citations.

## Success Criteria

A reader who completes this book must be able to:
- Explain Physical AI and the principles of embodied intelligence.
- Build and simulate control pipelines for humanoid robots.
- Connect Large Language Models (LLMs) to robotic actions in a meaningful way.
- Understand the constraints and challenges of sim-to-real deployment.

## Governance

This Constitution is the single source of truth for the project's principles and standards. All contributions and reviews must verify compliance. Any deviation requires a formal amendment to this document.

**Version**: 1.0.0 | **Ratified**: 2025-12-18 | **Last Amended**: 2025-12-18