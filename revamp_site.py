import os
from pathlib import Path

SITE_DIR = Path(r"c:\Users\arslan\Videos\projects\animanga_news\animanga-api\animanga-site")

files = {
    "astro.config.mjs": """import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  output: 'server',
  adapter: cloudflare(), // Works for both Workers and Pages
  integrations: [tailwind()],
});""",

    "wrangler.toml": """name = "animanga-site"
main = "./dist/_worker.js"

[assets]
directory = "./dist"
binding = "ASSETS"

[vars]
API_URL = "https://animanga-api.ionicerrrrscode.workers.dev"
""",

    "tailwind.config.mjs": """/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        brand: {
          light: '#fdfcfe',
          dark: '#0f0f12',
          accent: '#ff0055',
          violet: '#7c3aed',
          pink: '#db2777',
        }
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-out',
        'scale-up': 'scaleUp 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        scaleUp: {
          '0%': { transform: 'scale(1)' },
          '100%': { transform: 'scale(1.02)' },
        }
      }
    },
  },
  plugins: [],
}""",

    "src/layouts/Base.astro": """---
interface Props {
  title: string;
  description?: string;
}
const { title, description = "Animanga News and Database" } = Astro.props;
---
<html lang="en" class="bg-slate-50 text-slate-900">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width" />
    <title>{title} | AniManga</title>
    <meta name="description" content={description} />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
    <style>
      body {
        font-family: 'Outfit', sans-serif;
      }
      .glass {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
      }
    </style>
  </head>
  <body class="min-h-screen flex flex-col antialiased">
    <!-- Decorative background blobs -->
    <div class="fixed inset-0 -z-10 overflow-hidden">
      <div class="absolute -top-40 -right-40 w-80 h-80 bg-violet-200 rounded-full blur-3xl opacity-50"></div>
      <div class="absolute top-60 -left-40 w-80 h-80 bg-pink-200 rounded-full blur-3xl opacity-30"></div>
    </div>

    <header class="sticky top-0 z-50 glass border-b border-slate-100 shadow-sm">
      <div class="container mx-auto flex justify-between items-center p-4">
        <a href="/" class="text-3xl font-extrabold bg-gradient-to-r from-violet-600 to-pink-600 bg-clip-text text-transparent">AniManga</a>
        <nav>
          <ul class="flex gap-6 font-semibold text-slate-600">
            <li><a href="/" class="hover:text-violet-600 transition-colors">Home</a></li>
            <li><a href="/news" class="hover:text-violet-600 transition-colors">News</a></li>
            <li><a href="/trending" class="hover:text-violet-600 transition-colors">Trending</a></li>
          </ul>
        </nav>
      </div>
    </header>

    <main class="flex-grow container mx-auto p-6 animate-fade-in">
      <slot />
    </main>

    <footer class="glass border-t border-slate-100 mt-12 p-6 text-center text-slate-500">
      <p class="font-medium">&copy; 2026 AniManga. Crafted for true fans.</p>
    </footer>
  </body>
</html>
""",

    "src/components/ArticleCard.astro": """---
const { article } = Astro.props;
---
<div class="group relative bg-white rounded-2xl p-1 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
  <!-- Gradient border effect on hover -->
  <div class="absolute inset-0 bg-gradient-to-br from-violet-500 to-pink-500 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
  
  <div class="relative bg-white rounded-2xl p-6 h-full flex flex-col justify-between">
    <div>
      <div class="flex items-center gap-2 mb-3">
        <span class="text-xs font-bold uppercase tracking-wider text-violet-600">Article</span>
        <span class="text-xs text-slate-400">•</span>
        <span class="text-xs text-slate-500">{article.published_at?.slice(0, 10)}</span>
      </div>
      
      <h2 class="text-xl font-bold mb-3 text-slate-800 group-hover:text-violet-600 transition-colors">
        <a href={`/news/${article.slug}`}>
          {article.title}
        </a>
      </h2>
      
      <p class="text-slate-600 text-sm leading-relaxed mb-4 line-clamp-3">
        {article.meta_description}
      </p>
    </div>

    <div class="flex justify-between items-center text-xs border-t border-slate-50 pt-4 mt-auto">
      <span class="font-semibold text-slate-400">Model: {article.model_used}</span>
      <span class="text-violet-600 font-bold group-hover:underline flex items-center gap-1">
        Read More 
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
        </svg>
      </span>
    </div>
  </div>
</div>
""",

    "src/pages/index.astro": """---
import Base from '../layouts/Base.astro';
import ArticleCard from '../components/ArticleCard.astro';
import { getRewrittenArticles } from '../lib/api';

let articles = [];
let error = null;

try {
  const response = await getRewrittenArticles(12);
  articles = response.data || [];
} catch (e) {
  error = e.message;
}
---
<Base title="Premium Anime News" description="SEO Optimized Anime News and Insights">
  <!-- Hero Section -->
  <section class="text-center py-12 mb-8">
    <span class="text-sm font-extrabold uppercase tracking-widest text-pink-600 mb-2 block">AI-Powered Insights</span>
    <h1 class="text-5xl md:text-6xl font-extrabold mb-6 bg-gradient-to-r from-violet-600 via-pink-600 to-amber-500 bg-clip-text text-transparent">
      The Future of Anime News
    </h1>
    <p class="text-xl text-slate-600 max-w-2xl mx-auto font-medium">
      Explore deep-dive articles, character analyses, and breaking news rewritten for perfect readability and SEO.
    </p>
  </section>

  <!-- Grid Section -->
  <section class="mb-12">
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-2xl font-bold text-slate-800">Latest Stories</h2>
      <a href="/news" class="text-sm font-bold text-violet-600 hover:text-pink-600 transition-colors">View All →</a>
    </div>
    
    {error && (
      <div class="bg-red-50 border border-red-200 p-4 rounded-xl text-red-600 mb-6 font-medium">
        ⚠️ Error loading articles: {error}
      </div>
    )}

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      {articles.map((article) => (
        <ArticleCard article={article} />
      ))}
    </div>
  </section>
</Base>
""",

    "src/pages/news/[slug].astro": """---
import Base from '../../layouts/Base.astro';
import { getArticleBySlug } from '../../lib/api';

const { slug } = Astro.params;
let article = null;
let error = null;

try {
  const response = await getArticleBySlug(slug);
  article = response.data;
} catch (e) {
  error = e.message;
}
---
<Base 
  title={article?.title || "News"} 
  description={article?.meta_description}
>
  {error && (
    <div class="bg-red-50 border border-red-200 p-4 rounded-xl text-red-600 mb-6 font-medium">
      ⚠️ Error loading article: {error}
    </div>
  )}

  {article && (
    <article class="max-w-3xl mx-auto bg-white rounded-3xl p-8 md:p-12 shadow-sm border border-slate-100">
      <header class="mb-8 border-b border-slate-100 pb-8">
        <div class="flex items-center gap-2 mb-4">
          <span class="text-xs font-bold uppercase tracking-wider text-pink-600 bg-pink-50 px-2 py-1 rounded">Exclusive</span>
          <span class="text-xs text-slate-400">{article.published_at?.slice(0, 10)}</span>
        </div>
        
        <h1 class="text-4xl md:text-5xl font-extrabold mb-4 text-slate-900 leading-tight">
          {article.title}
        </h1>
        
        <p class="text-lg text-slate-500 font-medium">
          {article.meta_description}
        </p>
      </header>

      <!-- Body -->
      <div class="prose prose-slate max-w-none mb-10 text-slate-700 leading-relaxed text-lg">
        <div class="whitespace-pre-wrap">
          {article.body}
        </div>
      </div>

      <!-- Entities -->
      {article.unresolved_entities?.length > 0 && (
        <div class="border-t border-slate-100 pt-6">
          <h3 class="text-sm font-bold uppercase tracking-wider text-slate-400 mb-3">Linked Entities</h3>
          <div class="flex gap-2 flex-wrap">
            {article.unresolved_entities.map((entity) => (
              <span class="bg-slate-100 text-slate-700 px-3 py-1.5 rounded-full text-xs font-semibold hover:bg-violet-50 hover:text-violet-600 transition-colors cursor-pointer">
                {entity}
              </span>
            ))}
          </div>
        </div>
      )}
    </article>
  )}
</Base>
"""
}

print(f"Revamping project in {SITE_DIR}...")
for rel_path, content in files.items():
    full_path = SITE_DIR / rel_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content, encoding="utf-8")
    print(f"  Updated {rel_path}")

print("Done! Project files updated for Premium Light Theme and Worker Deployment.")
