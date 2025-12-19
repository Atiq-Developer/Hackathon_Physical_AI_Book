// @ts-check

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.

 /** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    {
      type: "doc",
      id: "intro",
      label: "Introduction",
    },

    {
      type: "category",
      label: "Module 1 — Introduction to Physical AI",
      items: [
        "physical-ai-book/module-1-intro-physical-ai/foundations",
        "physical-ai-book/module-1-intro-physical-ai/sensors",
      ],
    },

    {
      type: "category",
      label: "Module 2 — The Robotic Nervous System (ROS 2)",
      items: [
        "physical-ai-book/module-2-ros-2/architecture",
        "physical-ai-book/module-2-ros-2/rclpy-agents",
        "physical-ai-book/module-2-ros-2/urdf",
      ],
    },

    {
      type: "category",
      label: "Module 3 — The Digital Twin (Gazebo & Unity)",
      items: [
        "physical-ai-book/module-3-digital-twin/gazebo-physics",
        "physical-ai-book/module-3-digital-twin/sensor-simulation",
      ],
    },

    {
      type: "category",
      label: "Module 4 — The AI-Robot Brain (NVIDIA Isaac)",
      items: [
        "physical-ai-book/module-4-nvidia-isaac/isaac-sim",
        "physical-ai-book/module-4-nvidia-isaac/isaac-ros",
      ],
    },

    {
      type: "category",
      label: "Module 5 — Vision-Language-Action (VLA)",
      items: [
        "physical-ai-book/module-5-vla/llm-reasoning",
        "physical-ai-book/module-5-vla/voice-to-action",
      ],
    },

    {
      type: "category",
      label: "Module 6 — Capstone Project",
      items: ["physical-ai-book/module-6-capstone/index"],
    },
  ],
};

module.exports = sidebars;
