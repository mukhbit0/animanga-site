import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  output: 'server',
  adapter: cloudflare(), // Works for both Workers and Pages
  integrations: [tailwind()],
  prefetch: true,
});