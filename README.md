# AniManga Hub Frontend 🎨✨

The modern, ultra-premium, and blazing fast frontend for **AniManga Hub**. Built using **Astro**, **TailwindCSS**, and **Vanilla CSS**, this application is designed for visual excellence, seamless responsiveness, and absolute SEO optimization. 

---

## 🎨 Visual Philosophy & Aesthetic System
The design system of AniManga Hub is curated to deliver an immersive, high-end entertainment experience:
* **Curated Dark Theme**: Harmonious deep space backdrops with glowing electric violet, crimson, and neon cyan accents.
* **Glassmorphism**: Elegant translucent navigation bars and sidebars with backdrop-filters and subtle borders.
* **Responsive Collages**: Automatic grid-based featured headers matching content titles, utilizing advanced multi-column cards.
* **Dynamic Micro-animations**: Fluid hover transformations, glowing active states, and custom transitions that make the page feel alive.

---

## 📂 Pages Catalog & Layout Systems

### 🏠 1. Home (`/`)
The main entry point of the platform, structured as a high-density entertainment hub:
* **Dynamic Grid Featured Collage**: Showcases the hottest recent announcements.
* **Trending Carousel**: Ranks franchises experiencing peak discussion in news feeds.
* **Hype Radar**: Highlight lists showcasing high-rated items based on scoring metrics.
* **Recent News Room Feed**: Side-by-side dynamic news cards with semantic entity bubbles.

---

### 📰 2. News Catalog Index (`/news`)
A beautifully structured, high-density listing of SEO-optimized rewritten articles.
* **Grid Layout**: Dual-column card layouts on mobile, expanding to triple-columns on desktop.
* **Tag Filters**: Instant visual filters grouping articles by active themes (e.g., *Collaboration Events*, *Game Releases*, *Trailers*).
* **Infinite Scroll / Pagination**: Fully functional cursor navigation keeping page weight minimal.

---

### 📖 3. News Detail Page (`/news/[slug]`)
A fully-revamped, reading-optimized layout built to maximize user engagement and search engine rankings:
* **Collage Hero Image**: High-resolution collage header generated on-the-fly to represent article entities.
* **Embedded Entity Sidebars**: Floating cards summarizing metadata for all anime/manga mentioned in the article body.
* **Direct Content References**: Hyperlinked tags allowing users to pivot instantly into dedicated media wikis.

---

### 👾 4. Entity Profile Profile (`/entity/[id]`)
An all-inclusive hub summarizing a single franchise:
* **Top Hero Banner**: Floating poster card with real-time rating meters (MAL scores, popularity, active status).
* **AI Interactive Chat Tab**: Uses **Gemini 1.5** via serverless RAG, allowing users to talk directly with the franchise's AI using historical news articles as a knowledge base.
* **Structural Graph Recommendations**: Recommends related anime/manga based on co-occurrence graph weights.
* **Franchise News Room**: Lists all historic articles mentioning this entity.

---

### 📚 5. Medium Hubs (`/anime`, `/manga`, `/manhua`, `/manhwa`)
Tailored catalog indices designed to isolate specific media types.
* Renders premium high-density grids displaying scores, chapters, and episodes.
* Perfect search engine landing pages targeting media-specific queries.

---

### 📈 6. Trending Radar (`/trending`)
Displays ranked charts tracking franchises experiencing sudden jumps in media coverage, with custom mention-intensity meters.

---

### 🔍 7. Search (`/search`)
An elegant fuzzy-search engine query page that retrieves and filters matches by titles and alternative aliases.

---

## 🏗️ Technical Development & Compilation

### Setup Workspace
Ensure you install node dependencies:
```bash
npm install
```

### Run Locally (Dev Mode)
Starts the Astro local development server:
```bash
npm run dev
```

### Static Build Execution
Builds the website for production distribution. It compiles Astro routes and static pages inside `/dist`:
```bash
npm run build
```

### Preview Compiled Assets
Runs a local preview of the build result:
```bash
npm run preview
```

---

## ⚡ Deployment on Cloudflare Pages
This frontend is built to be deployed on **Cloudflare Pages**:
* **Build Command**: `npm run build`
* **Build Directory**: `dist`
* Any new pushes to the `main` branch on GitHub will automatically trigger a clean compile and deploy!
