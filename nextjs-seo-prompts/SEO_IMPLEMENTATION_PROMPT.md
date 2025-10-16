# SEO Implementation Prompt for Next.js Projects

> **Copy this entire prompt and paste it to an AI assistant when starting a new Next.js project**

---

## Prompt: Implement Complete SEO for Next.js Website

I need you to implement comprehensive SEO for my Next.js 13+ (App Router) website. Use the following specifications:

### Website Details:
- **Domain**: [YOUR_DOMAIN]
- **Brand Name**: [YOUR_BRAND]
- **Primary Keywords**: [LIST_KEYWORDS]
- **Description**: [YOUR_DESCRIPTION]
- **Social Handles**: Twitter: [HANDLE], LinkedIn: [HANDLE]

### 1. Root Layout Metadata (`app/layout.tsx`)

Add complete metadata configuration:

```typescript
export const metadata: Metadata = {
  metadataBase: new URL('https://[YOUR_DOMAIN]'),
  title: {
    default: "[YOUR_BRAND] - [VALUE_PROPOSITION]",
    template: "%s | [YOUR_BRAND]",
  },
  description: "[150-160 character description with keywords]",
  keywords: ["keyword1", "keyword2", "keyword3"],
  authors: [{ name: "[YOUR_COMPANY]" }],
  
  // Favicons
  icons: {
    icon: [
      { url: '/favicon.ico', sizes: 'any' },
      { url: '/favicon-16x16.png', sizes: '16x16', type: 'image/png' },
      { url: '/favicon-32x32.png', sizes: '32x32', type: 'image/png' },
      { url: '/favicon-192x192.png', sizes: '192x192', type: 'image/png' },
    ],
    apple: [{ url: '/apple-touch-icon.png', sizes: '180x180', type: 'image/png' }],
  },
  
  // OpenGraph
  openGraph: {
    title: "[YOUR_BRAND] - [VALUE_PROPOSITION]",
    description: "[Social-optimized description]",
    type: "website",
    url: "https://[YOUR_DOMAIN]",
    siteName: "[YOUR_BRAND]",
    images: [{ url: "/og-image.png", width: 1200, height: 630, alt: "[Image description]" }],
  },
  
  // Twitter
  twitter: {
    card: "summary_large_image",
    title: "[YOUR_BRAND] - [VALUE_PROPOSITION]",
    description: "[Twitter-optimized description]",
    images: ["/og-image.png"],
  },
};
```

Add Organization schema in the layout:

```typescript
const organizationSchema = {
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[YOUR_COMPANY]",
  "url": "https://[YOUR_DOMAIN]",
  "logo": "https://[YOUR_DOMAIN]/og-image.png",
  "description": "[Company description]",
  "sameAs": ["[TWITTER_URL]", "[LINKEDIN_URL]"]
};

<html lang="en">
  <head>
    <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(organizationSchema) }} />
  </head>
  <body>{children}</body>
</html>
```

### 2. Per-Page Metadata

For EVERY page, add:

```typescript
export const metadata: Metadata = {
  title: "[Unique 50-60 char title with keywords]",
  description: "[Unique 150-160 char description]",
  keywords: ["page-specific", "keywords"],
  
  alternates: {
    canonical: 'https://[YOUR_DOMAIN]/[exact-path]',
  },
  
  openGraph: {
    title: "[Page-specific OG title]",
    description: "[Social description]",
    url: "https://[YOUR_DOMAIN]/[path]",
    type: "website", // or "article" for blog
  },
};
```

For blog posts, also add:
```typescript
openGraph: {
  type: "article",
  publishedTime: "2025-10-16T00:00:00.000Z",
  authors: ["Author Name"],
}
```

### 3. Dynamic Sitemap (`app/sitemap.ts`)

Create a sitemap with all pages:

```typescript
import { MetadataRoute } from 'next'

export default function sitemap(): MetadataRoute.Sitemap {
  const baseUrl = 'https://[YOUR_DOMAIN]'
  
  return [
    { url: baseUrl, lastModified: new Date(), changeFrequency: 'weekly', priority: 1.0 },
    { url: `${baseUrl}/about`, lastModified: new Date(), changeFrequency: 'monthly', priority: 0.8 },
    { url: `${baseUrl}/pricing`, lastModified: new Date(), changeFrequency: 'monthly', priority: 0.9 },
    // Add all pages with appropriate priorities (0.5-1.0)
  ]
}
```

**Priorities**: Homepage (1.0), Key pages (0.8-0.9), Content (0.5-0.7), Legal (0.3)

### 4. Robots.txt (`public/robots.txt`)

```txt
User-agent: *
Allow: /
Disallow: /api/
Disallow: /admin/

Sitemap: https://[YOUR_DOMAIN]/sitemap.xml
```

### 5. Redirects & Headers (`next.config.ts`)

```typescript
const nextConfig: NextConfig = {
  async redirects() {
    return [
      // www to non-www
      {
        source: '/:path*',
        has: [{ type: 'host', value: 'www.[YOUR_DOMAIN]' }],
        destination: 'https://[YOUR_DOMAIN]/:path*',
        permanent: true,
      },
      // HTTP to HTTPS
      {
        source: '/:path*',
        has: [{ type: 'header', key: 'x-forwarded-proto', value: 'http' }],
        destination: 'https://[YOUR_DOMAIN]/:path*',
        permanent: true,
      },
    ];
  },
  
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [{ key: 'X-Robots-Tag', value: 'index, follow' }],
      },
    ];
  },
};
```

### 6. Security Headers (`vercel.json` or `next.config.ts`)

```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "X-XSS-Protection", "value": "1; mode=block" },
        { "key": "Referrer-Policy", "value": "origin-when-cross-origin" }
      ]
    }
  ]
}
```

### 7. Required Files in `public/`

Create these files:
- `favicon.ico`
- `favicon-16x16.png`
- `favicon-32x32.png`
- `favicon-192x192.png`
- `apple-touch-icon.png` (180x180)
- `og-image.png` (1200x630, optimized)
- `robots.txt`

### 8. Image Optimization

Use Next.js Image component everywhere:

```tsx
import Image from 'next/image'

<Image
  src="/image.jpg"
  alt="Descriptive alt text with keywords"
  width={1200}
  height={630}
  priority // for above-the-fold
/>
```

**Requirements**:
- ✅ Every image must have descriptive alt text
- ✅ Use descriptive filenames (not img123.jpg)
- ✅ Compress images (< 200KB for content, < 1MB for OG)

### 9. Canonical URL Rules

For every page:
1. Use HTTPS (never HTTP)
2. Use non-www (or www, pick one and be consistent)
3. Use absolute URLs: `https://domain.com/path`
4. No trailing slashes (except homepage)
5. Match sitemap URLs exactly

### 10. Verification

After implementation, verify:

```bash
# Check sitemap
curl https://[YOUR_DOMAIN]/sitemap.xml

# Check robots
curl https://[YOUR_DOMAIN]/robots.txt

# Check redirects
curl -I http://[YOUR_DOMAIN]  # Should 301 to https
curl -I https://www.[YOUR_DOMAIN]  # Should 301 to non-www

# Lighthouse audit
lighthouse https://[YOUR_DOMAIN] --view
```

### 11. Testing Checklist

- [ ] All pages have unique titles (50-60 chars)
- [ ] All pages have unique descriptions (150-160 chars)
- [ ] All pages have canonical tags
- [ ] Sitemap includes all pages
- [ ] Robots.txt is accessible
- [ ] All images have alt text
- [ ] www redirects to non-www (or vice versa)
- [ ] HTTP redirects to HTTPS
- [ ] OpenGraph image shows correctly on social media
- [ ] Lighthouse SEO score > 90
- [ ] Mobile-friendly test passes
- [ ] Core Web Vitals are in green

### Pages to Configure

Please implement the above for these pages:
- [ ] Homepage (`/`)
- [ ] About (`/about`)
- [ ] Pricing (`/pricing`)
- [ ] Contact (`/contact`)
- [ ] Blog index (`/blog`)
- [ ] Blog posts (`/blog/[slug]`)
- [ ] Terms (`/terms`)
- [ ] Privacy (`/privacy`)
- [LIST ANY ADDITIONAL PAGES]

### Additional Requirements

1. **For blog posts**: Add Article schema with publishedTime, author
2. **For products**: Add Product/SoftwareApplication schema
3. **All links**: Use absolute URLs in metadata
4. **Performance**: Target Core Web Vitals in green (LCP < 2.5s, FID < 100ms, CLS < 0.1)

### Output Format

Please:
1. Show me the complete `app/layout.tsx` with all metadata
2. Show me 2-3 example pages with metadata
3. Show me the complete `sitemap.ts`
4. Show me the `next.config.ts` with redirects
5. Create the `robots.txt` content
6. List any additional files I need to create

---

**Note**: Replace all [PLACEHOLDERS] with actual values before implementing.


