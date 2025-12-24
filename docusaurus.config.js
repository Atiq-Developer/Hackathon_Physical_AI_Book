// @ts-check
import { themes as prismThemes } from "prism-react-renderer";

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Physical AI & Humanoid Robotics",
  tagline: "Embodied Intelligence in the Physical World",
  favicon: "img/favicon.ico",

  future: {
    v4: true,
  },

  // ✅ IMPORTANT: Vercel + GitHub Pages compatible
  url: "https://atiq-developer.github.io",
  baseUrl: "/",

  organizationName: "Atiq-Developer",
  projectName: "Hackathon_Physical_AI_Book",

  onBrokenLinks: "warn",
  onBrokenMarkdownLinks: "warn",

  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      {
        docs: {
          sidebarPath: "./sidebars.js",
          routeBasePath: "/", // ✅ Docs become homepage
          editUrl:
            "https://github.com/Atiq-Developer/Hackathon_Physical_AI_Book/tree/main/",
        },
        blog: false, // ❌ Disable blog (clean book site)
        theme: {
          customCss: "./src/css/custom.css",
        },
      },
    ],
  ],

  themeConfig: {
    image: "img/social-card.png",

    colorMode: {
      defaultMode: "light",
      respectPrefersColorScheme: true,
    },

    navbar: {
      title: "Physical AI Book",
      logo: {
        alt: "Physical AI Logo",
        src: "img/logo.svg",
      },
      items: [
        {
          type: "docSidebar",
          sidebarId: "tutorialSidebar",
          position: "left",
          label: "Book",
        },
        {
          href: "https://github.com/Atiq-Developer/Hackathon_Physical_AI_Book",
          label: "GitHub",
          position: "right",
        },
      ],
    },

    footer: {
      style: "dark",
      links: [
        {
          title: "Book",
          items: [
            {
              label: "Introduction",
              to: "/",
            },
          ],
        },
        {
          title: "Project",
          items: [
            {
              label: "Repository",
              href: "https://github.com/Atiq-Developer/Hackathon_Physical_AI_Book",
            },
            {
              label: "Hackathon Submission",
              href: "#",
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Atiq Developer. Built with Docusaurus.`,
    },

    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  },
};

export default config;
