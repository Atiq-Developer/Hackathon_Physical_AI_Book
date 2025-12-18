# Tasks: Physical AI & Humanoid Robotics Textbook

**Input**: Design documents from `specs/001-physical-ai-textbook/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions.

## Phase 1: Setup (Book & Docusaurus Structure)

**Purpose**: Project initialization and basic Docusaurus site structure.

- [x] T001 [P] Create the book's root directory `docs/physical-ai-book/`.
- [x] T002 [P] Create Module 1 directory `docs/physical-ai-book/module-1-intro-physical-ai/`.
- [x] T003 [P] Create Module 2 directory `docs/physical-ai-book/module-2-ros-2/`.
- [x] T004 [P] Create Module 3 directory `docs/physical-ai-book/module-3-digital-twin/`.
- [x] T005 [P] Create Module 4 directory `docs/physical-ai-book/module-4-nvidia-isaac/`.
- [x] T006 [P] Create Module 5 directory `docs/physical-ai-book/module-5-vla/`.
- [x] T007 [P] Create Module 6 directory `docs/physical-ai-book/module-6-capstone/`.
- [x] T008 Update `sidebars.js` to add a new sidebar category for "Physical AI & Humanoid Robotics" with links to the modules.

---

## Phase 2: Foundational (Module Configuration)

**Purpose**: Configure each module to appear correctly in the Docusaurus sidebar.

- [x] T009 [P] Create category metadata file `docs/physical-ai-book/module-1-intro-physical-ai/_category_.json`.
- [x] T010 [P] Create category metadata file `docs/physical-ai-book/module-2-ros-2/_category_.json`.
- [x] T011 [P] Create category metadata file `docs/physical-ai-book/module-3-digital-twin/_category_.json`.
- [x] T012 [P] Create category metadata file `docs/physical-ai-book/module-4-nvidia-isaac/_category_.json`.
- [x] T013 [P] Create category metadata file `docs/physical-ai-book/module-5-vla/_category_.json`.
- [x] T014 [P] Create category metadata file `docs/physical-ai-book/module-6-capstone/_category_.json`.

**Checkpoint**: Foundation ready. The book's structure is now visible on the site. Chapter writing can begin.

---

## Phase 3: User Story 1 - Foundational Learning (Modules 1-3)

**Goal**: Provide the foundational knowledge for AI engineers to understand robotics.
**Independent Test**: A reader can complete Modules 1-3 and build a basic simulated robot in Gazebo controlled by ROS 2.

### Implementation for User Story 1

- [x] T015 [US1] Write Chapter: "Foundations of Embodied Intelligence" in `docs/physical-ai-book/module-1-intro-physical-ai/foundations.md`.
- [x] T016 [US1] Write Chapter: "Sensors and Physical Constraints" in `docs/physical-ai-book/module-1-intro-physical-ai/sensors.md`.
- [x] T017 [US1] Write Chapter: "ROS 2 Architecture" in `docs/physical-ai-book/module-2-ros-2/architecture.md`.
- [x] T018 [US1] Write Chapter: "Python Agents with rclpy" in `docs/physical-ai-book/module-2-ros-2/rclpy-agents.md`.
- [x] T019 [US1] Write Chapter: "URDF for Humanoid Robots" in `docs/physical-ai-book/module-2-ros-2/urdf.md`.
- [x] T020 [US1] Write Chapter: "Physics Simulation with Gazebo" in `docs/physical-ai-book/module-3-digital-twin/gazebo-physics.md`.
- [x] T021 [US1] Write Chapter: "Sensor Simulation" in `docs/physical-ai-book/module-3-digital-twin/sensor-simulation.md`.

**Checkpoint**: User Story 1 is complete. A reader can learn the fundamentals of Physical AI and ROS 2 with simulation.

---

## Phase 4: User Story 2 - Practical AI Integration (Modules 4-5)

**Goal**: Enable robotics students to integrate modern AI techniques into their projects.
**Independent Test**: A reader can complete Modules 4-5 and use Isaac Sim for perception and LLMs for task planning.

### Implementation for User Story 2

- [x] T022 [US2] Write Chapter: "Isaac Sim and Synthetic Data" in `docs/physical-ai-book/module-4-nvidia-isaac/isaac-sim.md`.
- [x] T023 [US2] Write Chapter: "Isaac ROS and VSLAM" in `docs/physical-ai-book/module-4-nvidia-isaac/isaac-ros.md`.
- [x] T024 [US2] Write Chapter: "LLMs for Robotic Reasoning" in `docs/physical-ai-book/module-5-vla/llm-reasoning.md`.
- [x] T025 [US2] Write Chapter: "Voice-to-Action Pipelines" in `docs/physical-ai-book/module-5-vla/voice-to-action.md`.

**Checkpoint**: User Story 2 is complete. A reader can now integrate advanced AI capabilities.

---

## Phase 5: User Story 3 - Capstone Project (Module 6)

**Goal**: Guide a graduate student through an end-to-end autonomous humanoid project.
**Independent Test**: A reader can complete Module 6 and have a fully functioning simulated robot that responds to voice commands.

### Implementation for User Story 3

- [x] T026 [US3] Write Chapter: "Capstone Project: Autonomous Humanoid Robot" in `docs/physical-ai-book/module-6-capstone/index.md`.

**Checkpoint**: All user stories are implemented. The book is content-complete.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final review and improvements that affect the entire book.

- [x] T027 [P] Review all chapters for technical accuracy, clarity, and consistency. (See `specs/001-physical-ai-textbook/review_process.md`)
- [x] T028 [P] Validate all code examples are runnable and produce the expected output. (See `specs/001-physical-ai-textbook/code_validation.md`)
- [x] T029 [P] Check all diagrams for correctness and clarity. (See `specs/001-physical-ai-textbook/diagram_validation.md`)
- [x] T030 [P] Add a companion code repository with all examples and launch files. (See `specs/001-physical-ai-textbook/companion_code_repo.md`)
- [x] T031 Update `docs/intro.md` to introduce the new book.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)** & **Foundational (Phase 2)** can run in parallel, but must be complete before chapter writing.
- **User Stories (Phases 3-5)** depend on Phase 1 & 2 completion. They should be executed sequentially (US1 → US2 → US3) as the knowledge is cumulative.
- **Polish (Phase 6)** depends on all user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2).
- **User Story 2 (P2)**: Depends on User Story 1.
- **User Story 3 (P3)**: Depends on User Story 2.

## Implementation Strategy

### Incremental Delivery

The book will be written and delivered sequentially by module, following the user story priorities.
1.  Complete Setup and Foundational Phases.
2.  Complete Phase 3 (Modules 1-3) → Foundational knowledge is available.
3.  Complete Phase 4 (Modules 4-5) → Advanced AI integration is available.
4.  Complete Phase 5 (Module 6) → The complete end-to-end project is available.
5.  Complete Polish phase for a final, high-quality release.
