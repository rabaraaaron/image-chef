import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vite.dev/config/
export default defineConfig({
  server: {
    host: "0.0.0.0", // Listen on all network interfaces
    port: 3000,
    strictPort: true, // Fail if port is already in use
    hmr: {
      clientPort: 3000, // The port your host machine will use
      overlay: false,
    },
  },
  plugins: [react()],
});
