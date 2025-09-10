# New Page/Feature Development Checklist

When requesting a new page or feature, please consider and specify the following:

1.  **Core Content & Purpose:**
    *   What is the main content or functionality of this page/feature?
    *   What problem does it solve or what value does it provide to the user?
    *   Provide the full HTML content or detailed instructions for generating it.

2.  **File Location & Naming:**
    *   What is the desired filename (e.g., `new-tool.html`)?
    *   Where should it be located in the project structure (e.g., in the root, in a new subdirectory)?

3.  **Navigation & Linking:**
    *   **Main Navigation:** Should it be added to the main navigation bar (`<nav class="main-nav">`)? If so, under which existing category (e.g., "Font Discovery", "Design & Typography", "Performance & Web", "Guides") or a new one?
    *   **Footer Navigation:** Should it be added to the footer navigation (`<footer>`)? If so, under which column?
    *   **Homepage/Index:** Should there be a link to it from the `index.html` homepage (e.g., as a new tool card)? If so, under which category?
    *   **Search Bar:** Should it be discoverable via the homepage search bar? (This usually requires updating `TOOL_DATA` in `index.html`.)

4.  **Search Engine Optimization (SEO) & Discoverability:**
    *   **Meta Tags:**
        *   `title`: What should the page title be (e.g., "New Tool Name | Tinyfont")?
        *   `description`: A concise summary for search engines.
        *   `keywords`: Relevant keywords.
        *   `author`: (e.g., "Prasoon")
        *   `canonical`: The full canonical URL (e.g., `https://tinyfont.me/new-tool.html`).
        *   Open Graph (`og:`) tags: `og:title`, `og:description`, `og:image`, `og:image:alt`, `og:url`, `og:type` (usually "website").
        *   Twitter Card (`twitter:`) tags: `twitter:card` (usually "summary_large_image"), `twitter:title`, `twitter:description`, `twitter:image`.
        *   `og:image` and `twitter:image` paths (e.g., `assets/images/og/new-tool.png`).
    *   **Sitemap:** Should it be added to `sitemap.xml`? (Usually yes, and I will handle the slugification and date.)

5.  **Monetization (AdSense):**
    *   Should AdSense ads be added to this page?
    *   If yes, where (e.g., top, bottom, within content, sidebar)?
    *   Any specific ad formats or sizes? (Default is usually responsive auto ads.)

6.  **Styling & Responsiveness:**
    *   Does it require any specific CSS? (If so, provide it or describe it.)
    *   Does it need to integrate with `assets/css/main.css`?
    *   Is it responsive and mobile-friendly? (Assumed by default, but confirm if specific layouts are needed.)

7.  **JavaScript Functionality:**
    *   Does it require any specific JavaScript? (If so, provide the code or detailed logic.)
    *   Should it use existing JavaScript files (e.g., `assets/js/main.js`, `google-fonts-downloader/assets/js/main.js`) or a new one?

8.  **Deployment & Verification:**
    *   After implementation, should I redeploy the site? (Usually yes.)
    *   Are there any specific tests or checks to perform to verify the new page/feature is working correctly?
