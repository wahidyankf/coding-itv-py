import { defineConfig, devices } from "@playwright/test";

const port = 3000;

// Tests run against the production build, so they match what ships.
export default defineConfig({
  testDir: "./tests",
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  reporter: "list",
  use: {
    baseURL: `http://localhost:${port}`,
    trace: "on-first-retry",
  },
  projects: [
    {
      name: "chromium",
      use: { ...devices["Desktop Chrome"] },
    },
  ],
  webServer: {
    command: "npm --prefix ../super-web run build && npm --prefix ../super-web run start",
    url: `http://localhost:${port}`,
    reuseExistingServer: !process.env.CI,
    timeout: 240_000,
  },
});
