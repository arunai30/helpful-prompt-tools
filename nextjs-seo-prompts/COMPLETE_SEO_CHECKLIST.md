# Complete Next.js SEO Implementation Guide

> **Use this checklist to implement comprehensive SEO on any Next.js website**

This guide captures all SEO best practices implemented on fyllyo.com. Use it as a template/prompt for other Next.js projects.

---

## 📋 Table of Contents

1. [Foundation Setup](#1-foundation-setup)
2. [Root Layout Configuration](#2-root-layout-configuration)
3. [Per-Page Metadata](#3-per-page-metadata)
4. [Canonical URLs](#4-canonical-urls)
5. [Sitemap Configuration](#5-sitemap-configuration)
6. [Robots.txt](#6-robotstxt)
7. [Structured Data (Schema.org)](#7-structured-data-schemaorg)
8. [OpenGraph & Social Media](#8-opengraph--social-media)
9. [URL Management & Redirects](#9-url-management--redirects)
10. [Security Headers](#10-security-headers)
11. [Images & Media](#11-images--media)
12. [Performance & Core Web Vitals](#12-performance--core-web-vitals)
13. [Monitoring & Verification](#13-monitoring--verification)

---

## 1. Foundation Setup

### ✅ Project Structure

```
app/
├── layout.tsx           # Root metadata
├── page.tsx             # Homepage
├── sitemap.ts           # Dynamic sitemap
├── [route]/
│   ├── layout.tsx       # Optional: route-specific metadata
│   └── page.tsx         # Page with metadata
public/
├── robots.txt           # Crawler instructions
├── favicon.ico          # Multiple sizes
├── og-image.png         # Social sharing image (1200x630)
└── apple-touch-icon.png # iOS icon
```

### ✅ Required Files

```bash
# Favicon sizes (generate all)
public/favicon.ico
public/favicon-16x16.png
public/favicon-32x32.png
public/favicon-48x48.png
public/favicon-192x192.png
public/apple-touch-icon.png (180x180)
public/android-chrome-192x192.png
public/android-chrome-512x512.png

# Social sharing
public/og-image.png (1200x630, optimized)
```

---

## 2. Root Layout Configuration

**File**: `app/layout.tsx`

```typescript
import type { Metadata } from "next";

export const metadata: Metadata = {
  // 1. Base URL for all relative URLs
  metadataBase: new URL('https://yourdomain.com'),
  
  // 2. Default title and description
  title: {
    default: "Your Brand - Primary Value Proposition",
    template: "%s | Your Brand", // Page titles will use this
  },
  description: "Compelling 150-160 character description with primary keywords naturally included.",
  
  // 3. Keywords (optional, but good for organization)
  keywords: ["primary keyword", "secondary keyword", "long-tail keyword"],
  
  // 4. Author information
  authors: [{ name: "Your Company Name" }],
  
  // 5. Favicon and app icons
  icons: {
    icon: [
      { url: '/favicon.ico', sizes: 'any' },
      { url: '/favicon-16x16.png', sizes: '16x16', type: 'image/png' },
      { url: '/favicon-32x32.png', sizes: '32x32', type: 'image/png' },
      { url: '/favicon-48x48.png', sizes: '48x48', type: 'image/png' },
      { url: '/favicon-192x192.png', sizes: '192x192', type: 'image/png' },
    ],
    apple: [
      { url: '/apple-touch-icon.png', sizes: '180x180', type: 'image/png' },
    ],
    other: [
      { url: '/android-chrome-192x192.png', sizes: '192x192', type: 'image/png' },
      { url: '/android-chrome-512x512.png', sizes: '512x512', type: 'image/png' },
    ],
  },
  
  // 6. OpenGraph for social media
  openGraph: {
    title: "Your Brand - Primary Value Proposition",
    description: "Compelling description for social sharing",
    type: "website",
    url: "https://yourdomain.com",
    siteName: "Your Brand",
    images: [
      {
        url: "/og-image.png",
        width: 1200,
        height: 630,
        alt: "Your Brand Logo or Key Visual",
      },
    ],
    locale: "en_US",
  },
  
  // 7. Twitter Card
  twitter: {
    card: "summary_large_image",
    title: "Your Brand - Primary Value Proposition",
    description: "Compelling description for Twitter",
    images: ["/og-image.png"],
    creator: "@yourtwitterhandle", // Optional
  },
  
  // 8. Verification (optional)
  verification: {
    google: "your-google-verification-code",
    // yandex: "your-yandex-verification-code",
    // bing: "your-bing-verification-code",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  // 9. Structured Data (Organization Schema)
  const organizationSchema = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Your Company Name",
    "url": "https://yourdomain.com",
    "logo": "https://yourdomain.com/og-image.png",
    "description": "Your company description",
    "sameAs": [
      "https://twitter.com/yourhandle",
      "https://www.linkedin.com/company/yourcompany",
      "https://www.facebook.com/yourpage",
    ]
  };

  return (
    <html lang="en"> {/* ← CRITICAL: Set correct language */}
      <head>
        {/* Inject structured data */}
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(organizationSchema),
          }}
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
```

---

## 3. Per-Page Metadata

**Every page should have unique, optimized metadata.**

### Example: Homepage (`app/page.tsx`)

```typescript
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Your Brand - Specific Page Title", // Will use template from root
  description: "Unique 150-160 char description for this specific page with relevant keywords.",
  keywords: ["page-specific", "keywords", "here"],
  
  alternates: {
    canonical: 'https://yourdomain.com', // ← CRITICAL for SEO
  },
  
  openGraph: {
    title: "Specific OG Title for Social Sharing",
    description: "Description optimized for social media",
    url: "https://yourdomain.com",
    type: "website",
  },
};

export default function HomePage() {
  return <div>Your content</div>;
}
```

### Example: Blog Post (`app/blog/[slug]/page.tsx`)

```typescript
export const metadata: Metadata = {
  title: "Blog Post Title - Keyword Rich & Under 60 Characters",
  description: "Compelling 150-160 character summary of the blog post content.",
  keywords: ["blog topic", "related keywords", "long-tail variations"],
  
  alternates: {
    canonical: 'https://yourdomain.com/blog/post-slug',
  },
  
  openGraph: {
    title: "Blog Post Title",
    description: "Social-optimized description",
    url: "https://yourdomain.com/blog/post-slug",
    type: "article",
    publishedTime: "2025-10-16T00:00:00.000Z",
    authors: ["Author Name"],
    images: ["/blog-post-image.jpg"], // Unique image per post
  },
  
  twitter: {
    card: "summary_large_image",
    title: "Blog Post Title",
    description: "Twitter-optimized description",
    images: ["/blog-post-image.jpg"],
  },
};
```

### 📝 Metadata Best Practices

| Element | Best Practice | Example |
|---------|---------------|---------|
| **Title** | 50-60 characters, include primary keyword | "Form Automation Tool - Save 10 Hours/Week" |
| **Description** | 150-160 characters, compelling CTA | "AI-powered form automation saves 10+ hours weekly. Upload once, use everywhere. Free trial." |
| **Keywords** | 5-10 relevant terms, natural language | ["form automation", "AI autofill"] |
| **Canonical** | ALWAYS set, absolute URL | `https://yourdomain.com/page` |
| **OG Image** | 1200x630px, < 1MB, relevant | `/blog/post-image.jpg` |

---

## 4. Canonical URLs

### ✅ Why Canonical Tags Matter

Prevents duplicate content penalties from:
- www vs non-www (`www.site.com` vs `site.com`)
- HTTP vs HTTPS (`http://` vs `https://`)
- Trailing slashes (`/about` vs `/about/`)
- URL parameters (`?utm_source=`, `?ref=`)

### ✅ Implementation (Every Page)

```typescript
export const metadata: Metadata = {
  alternates: {
    canonical: 'https://yourdomain.com/exact-path',
  },
};
```

### 📋 Canonical URL Rules

1. ✅ Use HTTPS (never HTTP)
2. ✅ Use your preferred domain (www or non-www, pick one)
3. ✅ Use absolute URLs (`https://domain.com/path`)
4. ❌ No trailing slashes (except homepage)
5. ✅ Match sitemap URLs exactly
6. ✅ Consistent across all pages

---

## 5. Sitemap Configuration

**File**: `app/sitemap.ts`

```typescript
import { MetadataRoute } from 'next'

export default function sitemap(): MetadataRoute.Sitemap {
  const baseUrl = 'https://yourdomain.com'
  
  // Static pages
  const staticPages = [
    {
      url: baseUrl,
      lastModified: new Date(),
      changeFrequency: 'weekly' as const,
      priority: 1.0, // Homepage is most important
    },
    {
      url: `${baseUrl}/about`,
      lastModified: new Date(),
      changeFrequency: 'monthly' as const,
      priority: 0.8,
    },
    {
      url: `${baseUrl}/pricing`,
      lastModified: new Date(),
      changeFrequency: 'monthly' as const,
      priority: 0.9, // High priority for conversion page
    },
    {
      url: `${baseUrl}/blog`,
      lastModified: new Date(),
      changeFrequency: 'weekly' as const,
      priority: 0.8,
    },
    // Add all static pages...
  ]
  
  // Dynamic blog posts (if applicable)
  // const blogPosts = await fetchBlogPosts();
  // const blogPages = blogPosts.map(post => ({
  //   url: `${baseUrl}/blog/${post.slug}`,
  //   lastModified: new Date(post.updatedAt),
  //   changeFrequency: 'monthly' as const,
  //   priority: 0.7,
  // }));
  
  return [
    ...staticPages,
    // ...blogPages,
  ]
}
```

### 📋 Sitemap Best Practices

| Property | When to Use | Example |
|----------|-------------|---------|
| **priority** | 1.0 = Homepage, 0.8-0.9 = Key pages, 0.5-0.7 = Content | `1.0` for `/`, `0.9` for `/pricing` |
| **changeFrequency** | How often content updates | `daily`, `weekly`, `monthly`, `yearly` |
| **lastModified** | Actual last update date | `new Date('2025-10-16')` |

---

## 6. Robots.txt

**File**: `public/robots.txt`

```txt
User-agent: *
Allow: /

# Block specific paths (if needed)
Disallow: /api/
Disallow: /admin/
Disallow: /_next/
Disallow: /private/

# Crawl delay (optional, use sparingly)
# Crawl-delay: 1

# Sitemap location (REQUIRED)
Sitemap: https://yourdomain.com/sitemap.xml
```

### 📋 Robots.txt Rules

- ✅ Always allow main content: `Allow: /`
- ✅ Always reference sitemap
- ✅ Block API routes, admin areas, private content
- ✅ Use `Disallow` sparingly (you want to be crawled!)

---

## 7. Structured Data (Schema.org)

### Organization Schema (Root Layout)

```typescript
const organizationSchema = {
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Your Company Name",
  "url": "https://yourdomain.com",
  "logo": "https://yourdomain.com/logo.png",
  "description": "Company description",
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "support@yourdomain.com",
    "contactType": "Customer Service"
  },
  "sameAs": [
    "https://twitter.com/yourhandle",
    "https://linkedin.com/company/yourcompany"
  ]
};
```

### Article Schema (Blog Posts)

```typescript
const articleSchema = {
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Your Blog Post Title",
  "description": "Post description",
  "image": "https://yourdomain.com/blog/image.jpg",
  "datePublished": "2025-10-16T00:00:00Z",
  "dateModified": "2025-10-16T00:00:00Z",
  "author": {
    "@type": "Person",
    "name": "Author Name"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Your Company",
    "logo": {
      "@type": "ImageObject",
      "url": "https://yourdomain.com/logo.png"
    }
  }
};
```

### Product Schema (For SaaS/Products)

```typescript
const productSchema = {
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Your Product Name",
  "operatingSystem": "Web",
  "applicationCategory": "BusinessApplication",
  "offers": {
    "@type": "Offer",
    "price": "9.99",
    "priceCurrency": "USD"
  }
};
```

---

## 8. OpenGraph & Social Media

### ✅ OpenGraph Tags (Every Page)

```typescript
openGraph: {
  title: "Specific page title for social sharing",
  description: "Optimized for social media (more casual than meta description)",
  type: "website", // or "article" for blog posts
  url: "https://yourdomain.com/page",
  siteName: "Your Brand Name",
  images: [
    {
      url: "/og-image.jpg",
      width: 1200,
      height: 630,
      alt: "Descriptive alt text",
    },
  ],
  locale: "en_US",
}
```

### ✅ Twitter Cards

```typescript
twitter: {
  card: "summary_large_image", // or "summary"
  title: "Twitter-optimized title (max 70 chars)",
  description: "Twitter description (max 200 chars)",
  images: ["/twitter-image.jpg"],
  creator: "@yourtwitterhandle",
  site: "@companytwitterhandle",
}
```

### 📋 Social Image Guidelines

| Platform | Size | Format | Notes |
|----------|------|--------|-------|
| **OpenGraph** | 1200×630px | JPG/PNG | Universal social sharing |
| **Twitter** | 1200×628px | JPG/PNG | Same as OG works fine |
| **LinkedIn** | 1200×627px | JPG/PNG | Same as OG works fine |
| **File Size** | < 1MB | Optimized | Use compression |

---

## 9. URL Management & Redirects

**File**: `next.config.ts`

```typescript
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // 1. URL Redirects (CRITICAL for SEO)
  async redirects() {
    return [
      // Redirect www to non-www (or vice versa)
      {
        source: '/:path*',
        has: [
          {
            type: 'host',
            value: 'www.yourdomain.com',
          },
        ],
        destination: 'https://yourdomain.com/:path*',
        permanent: true, // 301 redirect
      },
      
      // Force HTTPS
      {
        source: '/:path*',
        has: [
          {
            type: 'header',
            key: 'x-forwarded-proto',
            value: 'http',
          },
        ],
        destination: 'https://yourdomain.com/:path*',
        permanent: true,
      },
      
      // Legacy URL redirects (if migrating)
      // {
      //   source: '/old-page',
      //   destination: '/new-page',
      //   permanent: true,
      // },
    ];
  },

  // 2. SEO-friendly headers
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'X-Robots-Tag',
            value: 'index, follow', // Tell crawlers to index
          },
        ],
      },
    ];
  },
};

export default nextConfig;
```

### 📋 Redirect Rules

- ✅ **Always 301** (permanent) for SEO redirects
- ✅ Redirect www → non-www (or pick one standard)
- ✅ Redirect HTTP → HTTPS
- ✅ Redirect old URLs to new ones if restructuring
- ❌ Avoid redirect chains (A → B → C)

---

## 10. Security Headers

**File**: `vercel.json` (or `next.config.ts`)

```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        },
        {
          "key": "X-Frame-Options",
          "value": "DENY"
        },
        {
          "key": "X-XSS-Protection",
          "value": "1; mode=block"
        },
        {
          "key": "Referrer-Policy",
          "value": "origin-when-cross-origin"
        },
        {
          "key": "Permissions-Policy",
          "value": "camera=(), microphone=(), geolocation=()"
        }
      ]
    }
  ]
}
```

### Why Security Headers Help SEO

Google considers site security as a ranking factor:
- ✅ HTTPS is mandatory
- ✅ Security headers build trust
- ✅ Prevents clickjacking and XSS attacks
- ✅ Better Core Web Vitals scores

---

## 11. Images & Media

### ✅ Use Next.js Image Component

```tsx
import Image from 'next/image'

<Image
  src="/your-image.jpg"
  alt="Descriptive alt text with keywords" // ← CRITICAL for SEO
  width={1200}
  height={630}
  priority // For above-the-fold images
  loading="lazy" // For below-the-fold images
/>
```

### 📋 Image SEO Checklist

- ✅ **Always use alt text** (descriptive, include keywords naturally)
- ✅ **Use descriptive filenames** (`ai-form-automation.jpg`, not `img123.jpg`)
- ✅ **Compress images** (< 200KB for content, < 1MB for OG images)
- ✅ **Use modern formats** (WebP, AVIF with fallbacks)
- ✅ **Specify dimensions** (prevents layout shift, helps CWV)

---

## 12. Performance & Core Web Vitals

### ✅ Next.js Optimizations

```typescript
// next.config.ts
const nextConfig: NextConfig = {
  images: {
    formats: ['image/avif', 'image/webp'],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
  },
  
  // Enable compression
  compress: true,
  
  // Optimize fonts
  experimental: {
    optimizeFonts: true,
  },
};
```

### 📋 Core Web Vitals Targets

| Metric | Target | Description |
|--------|--------|-------------|
| **LCP** | < 2.5s | Largest Contentful Paint |
| **FID** | < 100ms | First Input Delay |
| **CLS** | < 0.1 | Cumulative Layout Shift |
| **FCP** | < 1.8s | First Contentful Paint |
| **TTFB** | < 600ms | Time to First Byte |

### ✅ Performance Tips

```tsx
// 1. Lazy load components
const HeavyComponent = dynamic(() => import('./HeavyComponent'), {
  loading: () => <LoadingSpinner />,
});

// 2. Optimize fonts
import { Inter } from 'next/font/google'
const inter = Inter({ subsets: ['latin'], display: 'swap' })

// 3. Use loading states
<Suspense fallback={<Skeleton />}>
  <AsyncComponent />
</Suspense>
```

---

## 13. Monitoring & Verification

### ✅ Google Search Console Setup

1. **Verify ownership**:
   ```typescript
   // In app/layout.tsx metadata:
   verification: {
     google: 'your-verification-code',
   }
   ```

2. **Submit sitemap**:
   - URL: `https://yourdomain.com/sitemap.xml`
   - Check "Coverage" report regularly

3. **Monitor**:
   - Index coverage
   - Core Web Vitals
   - Mobile usability
   - Security issues

### ✅ Testing Tools

| Tool | Purpose | URL |
|------|---------|-----|
| **Google Search Console** | Monitor indexing, issues | search.google.com/search-console |
| **PageSpeed Insights** | Performance & CWV | pagespeed.web.dev |
| **Lighthouse** | Overall audit | Chrome DevTools |
| **Rich Results Test** | Structured data | search.google.com/test/rich-results |
| **Mobile-Friendly Test** | Mobile usability | search.google.com/test/mobile-friendly |
| **Canonical Tag Checker** | Verify canonical tags | ahrefs.com/canonical-tag-checker |

### ✅ Pre-Launch Checklist

```bash
# 1. Build and test
npm run build
npm run start

# 2. Check for errors
npm run lint

# 3. Test critical paths
- Homepage loads
- Sitemap accessible at /sitemap.xml
- Robots.txt accessible at /robots.txt
- All images have alt text
- All pages have unique titles
- All pages have canonical tags

# 4. Verify in production
curl -I https://yourdomain.com # Check headers
curl https://yourdomain.com/sitemap.xml # Check sitemap
curl https://yourdomain.com/robots.txt # Check robots

# 5. Test redirects
curl -I http://yourdomain.com # Should 301 to https
curl -I https://www.yourdomain.com # Should 301 to non-www

# 6. Social sharing test
- Post a link on Twitter/LinkedIn
- Verify OG image shows correctly
```

---

## 📝 Quick Copy-Paste Checklist

Use this for every new Next.js project:

```markdown
SEO Implementation Checklist

Foundation:
□ Set metadataBase in root layout
□ Create all favicon sizes (16, 32, 48, 192, 512, apple-touch)
□ Create OG image (1200x630)
□ Set html lang attribute
□ Configure robots.txt with sitemap URL

Metadata (Every Page):
□ Unique title (50-60 chars)
□ Unique description (150-160 chars)
□ Keywords array
□ Canonical URL (absolute, https, no trailing slash)
□ OpenGraph tags (title, description, url, image)
□ Twitter card tags

Technical:
□ Create dynamic sitemap.ts
□ Configure redirects (www→non-www, http→https)
□ Add security headers
□ Add structured data (Organization schema minimum)
□ Verify all images have alt text

Testing:
□ Run Lighthouse audit (score > 90)
□ Test all redirects
□ Verify sitemap.xml loads
□ Verify robots.txt loads
□ Test social sharing on Twitter/LinkedIn
□ Submit to Google Search Console
□ Check mobile-friendliness
```

---

## 🚀 Post-Launch Monitoring

### Week 1-4: Initial Indexing
- Monitor Google Search Console for crawl errors
- Verify all pages are indexed
- Check for canonical tag issues
- Monitor Core Web Vitals

### Month 2-3: Optimization
- Analyze search queries (Search Console)
- Identify top-performing pages
- Optimize underperforming pages
- Add more structured data

### Ongoing:
- Monthly SEO audits
- Update sitemap for new content
- Monitor backlinks
- Track keyword rankings
- Improve Core Web Vitals scores

---

## 🎯 Summary: The Essential SEO Stack

| Layer | Component | Purpose |
|-------|-----------|---------|
| **1. Foundation** | metadataBase, title, description | Basic discoverability |
| **2. Crawling** | sitemap.xml, robots.txt | Help search engines find content |
| **3. Indexing** | Canonical tags, redirects | Prevent duplicate content |
| **4. Ranking** | Quality content, performance, structure | Improve search position |
| **5. Display** | OpenGraph, Twitter cards, schema | Rich search results |
| **6. Trust** | HTTPS, security headers, valid HTML | Build credibility |

---

## 📚 Additional Resources

- [Next.js Metadata Docs](https://nextjs.org/docs/app/building-your-application/optimizing/metadata)
- [Google Search Central](https://developers.google.com/search)
- [Schema.org](https://schema.org/)
- [OpenGraph Protocol](https://ogp.me/)
- [Core Web Vitals Guide](https://web.dev/vitals/)

---


**Use this guide for**: Any Next.js 13+ project with App Router


