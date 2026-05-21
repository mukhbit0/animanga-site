const API_URL = import.meta.env.API_URL || 'https://animanga-api.ionicerrrrscode.workers.dev';

export async function fetchAPI(endpoint: string) {
  const env = (globalThis as any).currentEnv;
  if (env && env.API) {
    const fullUrl = `https://animanga-api.ionicerrrrscode.workers.dev${endpoint}`;
    console.log("[fetchAPI] Service Binding available. Routing request:", fullUrl);
    try {
      const res = await env.API.fetch(fullUrl);
      if (!res.ok) {
        console.error("[fetchAPI] Service Binding error response status:", res.status, "for URL:", fullUrl);
        throw new Error(`API Service Binding error: ${res.status}`);
      }
      return await res.json();
    } catch (err) {
      console.error("[fetchAPI] Service Binding exception:", err, "for URL:", fullUrl);
      throw err;
    }
  }

  // Fallback to public URL fetch
  const fullUrl = `${API_URL}${endpoint}`;
  console.log("[fetchAPI] Routing via public URL fetch:", fullUrl);
  try {
    const res = await fetch(fullUrl);
    if (!res.ok) {
      console.error("[fetchAPI] Public fetch error response status:", res.status, "for URL:", fullUrl);
      throw new Error(`API error: ${res.status}`);
    }
    return await res.json();
  } catch (err) {
    console.error("[fetchAPI] Public fetch exception:", err, "for URL:", fullUrl);
    throw err;
  }
}

// ── Rewritten Articles ──────────────────────────────────────────────
export async function getRewrittenArticles(limit = 20, cursor = '', year = '', month = '', tag = '', type = '') {
  let url = `/v1/rewritten?limit=${limit}`;
  if (cursor) url += `&cursor=${encodeURIComponent(cursor)}`;
  if (year) url += `&year=${year}`;
  if (month) url += `&month=${month}`;
  if (tag) url += `&tag=${encodeURIComponent(tag)}`;
  if (type) url += `&type=${type}`;
  return fetchAPI(url);
}

export async function getRewrittenRecent(type: string, limit = 10) {
  return fetchAPI(`/v1/rewritten/recent/${type}?limit=${limit}`);
}

export async function getArticleBySlug(slug: string) {
  return fetchAPI(`/v1/rewritten/${encodeURIComponent(slug)}`);
}

export async function getRewrittenArticlesByEntity(id: string, limit = 10) {
  return fetchAPI(`/v1/rewritten/by-entity/${id}?limit=${limit}`);
}

// ── Trending ────────────────────────────────────────────────────────
export async function getTrending(type = '', days = 30, limit = 20) {
  let url = `/v1/trending?days=${days}&limit=${limit}`;
  if (type) url += `&type=${type}`;
  return fetchAPI(url);
}

// ── Entity ──────────────────────────────────────────────────────────
export async function getEntity(id: string) {
  return fetchAPI(`/v1/entity/${id}`);
}

export async function getEntityBySlug(slug: string) {
  return fetchAPI(`/v1/entity/by-slug/${encodeURIComponent(slug)}`);
}

export async function getEntityRecommendations(id: string, type = '', limit = 10) {
  let url = `/v1/entity/${id}/recommendations?limit=${limit}`;
  if (type) url += `&type=${type}`;
  return fetchAPI(url);
}

export async function getEntityArticles(id: string, cursor = '', limit = 10) {
  let url = `/v1/entity/${id}/articles?limit=${limit}`;
  if (cursor) url += `&cursor=${encodeURIComponent(cursor)}`;
  return fetchAPI(url);
}

// ── Search ──────────────────────────────────────────────────────────
export async function searchEntities(q: string, type = '', limit = 20) {
  let url = `/v1/search?q=${encodeURIComponent(q)}&limit=${limit}`;
  if (type) url += `&type=${type}`;
  return fetchAPI(url);
}

export async function searchByTags(tags: string, type = '', limit = 50) {
  let url = `/v1/search/tags?tags=${encodeURIComponent(tags)}&limit=${limit}`;
  if (type) url += `&type=${type}`;
  return fetchAPI(url);
}

// ── Additional Endpoints ────────────────────────────────────────────
export async function getTop(type: string) {
  return fetchAPI(`/v1/top/${type}`);
}

export async function getNew(type: string) {
  return fetchAPI(`/v1/new/${type}`);
}

export async function getSeason(season: string) {
  return fetchAPI(`/v1/season/${season}`);
}

export async function getJikanData(path: string) {
  return fetchAPI(`/v1/external/jikan/${path}`);
}

// ── Catalog & Hype (New) ────────────────────────────────────────────
export async function getCatalog(type: string, sort = 'score', status = '', genre = '', limit = 20, cursor = '') {
  let url = `/v1/catalog?type=${type}&sort=${sort}&limit=${limit}`;
  if (status) url += `&status=${status}`;
  if (genre) url += `&genre=${encodeURIComponent(genre)}`;
  if (cursor) url += `&cursor=${encodeURIComponent(cursor)}`;
  return fetchAPI(url);
}

export async function getHype(limit = 20) {
  return fetchAPI(`/v1/hype?limit=${limit}`);
}
