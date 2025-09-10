import os

# ==============================================================================
# 1. CSS STYLES (style.css)
# This string contains all the CSS for the entire site.
# ==============================================================================
CSS_CONTENT = """
:root {
    --bg-color-light: #f4f7fc;
    --text-color-light: #1e293b;
    --card-bg-light: rgba(255, 255, 255, 0.65);
    --border-color-light: rgba(203, 213, 225, 0.8);
    --subtle-bg-light: #e2e8f0;

    --bg-color-dark: #0f172a;
    --text-color-dark: #e2e8f0;
    --card-bg-dark: rgba(30, 41, 59, 0.55);
    --border-color-dark: rgba(51, 65, 85, 0.9);
    --subtle-bg-dark: #1e293b;

    --accent-color: #3b82f6;
    --accent-color-hover: #2563eb;
    --danger-color: #ef4444;
    --danger-color-hover: #dc2626;

    --font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    --border-radius-lg: 1.5rem;
    --border-radius-md: 0.75rem;
    --shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1);
    --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

[data-theme="light"] {
    --bg-color: var(--bg-color-light);
    --text-color: var(--text-color-light);
    --card-bg: var(--card-bg-light);
    --border-color: var(--border-color-light);
    --subtle-bg: var(--subtle-bg-light);
}

[data-theme="dark"] {
    --bg-color: var(--bg-color-dark);
    --text-color: var(--text-color-dark);
    --card-bg: var(--card-bg-dark);
    --border-color: var(--border-color-dark);
    --subtle-bg: var(--subtle-bg-dark);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

body {
    font-family: var(--font-family);
    background-color: var(--bg-color);
    color: var(--text-color);
    line-height: 1.6;
    transition: var(--transition);
    overflow-x: hidden;
    background-image: radial-gradient(circle at 1% 1%, rgba(150, 150, 255, 0.1), transparent 30%),
                      radial-gradient(circle at 99% 99%, rgba(255, 150, 150, 0.1), transparent 40%);
}

.container { max-width: 960px; margin: 0 auto; padding: 2rem 1.5rem; }
.main-content { padding-top: 4rem; padding-bottom: 4rem; }

/* Header & Navigation */
.header {
    padding: 1rem 0;
    position: sticky;
    top: 0;
    z-index: 100;
    background: var(--card-bg);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border-color);
    transition: var(--transition);
}
.header .container { display: flex; justify-content: space-between; align-items: center; padding-top: 0; padding-bottom: 0; }
.logo { font-weight: 700; font-size: 1.5rem; color: var(--text-color); text-decoration: none; }
.nav a { color: var(--text-color); text-decoration: none; margin: 0 1rem; font-weight: 600; position: relative; transition: var(--transition); }
.nav a::after { content: ''; position: absolute; width: 0; height: 2px; bottom: -5px; left: 50%; transform: translateX(-50%); background-color: var(--accent-color); transition: var(--transition); }
.nav a:hover::after, .nav a.active::after { width: 100%; }
.nav a:hover, .nav a.active { color: var(--accent-color); }

/* Theme Toggle */
.theme-toggle { background: transparent; border: none; cursor: pointer; color: var(--text-color); padding: 0.5rem; border-radius: 50%; transition: var(--transition); }
.theme-toggle:hover { background: var(--subtle-bg); }
[data-theme="light"] .moon-icon { display: none; }
[data-theme="dark"] .sun-icon { display: none; }

/* Main Card */
.card {
    padding: 2.5rem;
    border-radius: var(--border-radius-lg);
    box-shadow: var(--shadow);
    text-align: center;
    background: var(--card-bg);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--border-color);
}
h1 { font-size: 2.8rem; margin-bottom: 0.5rem; line-height: 1.2; }
.card > p { font-size: 1.1rem; margin-bottom: 2rem; max-width: 600px; margin-left: auto; margin-right: auto; color: var(--text-color); opacity: 0.8; }

/* Gradient Preview */
.gradient-preview { width: 100%; height: 320px; border-radius: var(--border-radius-md); margin-bottom: 2rem; transition: background 0.5s ease; border: 1px solid var(--border-color); }

/* Controls & Inputs */
.controls { margin-bottom: 2rem; }
.color-inputs { display: flex; justify-content: center; align-items: center; gap: 1rem; flex-wrap: wrap; }
.color-input-wrapper { position: relative; }
.color-input { -webkit-appearance: none; -moz-appearance: none; appearance: none; width: 60px; height: 60px; background-color: transparent; border: none; cursor: pointer; }
.color-input::-webkit-color-swatch { border-radius: 50%; border: 4px solid var(--bg-color); box-shadow: 0 0 15px rgba(0,0,0,0.1); transition: var(--transition); }
.color-input::-moz-color-swatch { border-radius: 50%; border: 4px solid var(--bg-color); box-shadow: 0 0 15px rgba(0,0,0,0.1); transition: var(--transition); }
.color-input:hover::-webkit-color-swatch { transform: scale(1.1); }
.color-input:hover::-moz-color-swatch { transform: scale(1.1); }

/* Multi-color page controls */
.multi-color-controls { display: flex; justify-content: center; gap: 1rem; margin-top: 1.5rem; }
.color-action-btn { width: 60px; height: 60px; border-radius: 50%; font-size: 2rem; display: flex; align-items: center; justify-content: center; background-color: var(--subtle-bg); color: var(--text-color); }
.color-action-btn.remove-color-btn { background-color: var(--danger-color); color: white; }
.color-action-btn.remove-color-btn:hover { background-color: var(--danger-color-hover); }

/* Output & Buttons */
.output { display: flex; gap: 1rem; margin-bottom: 2.5rem; }
#css-code { width: 100%; padding: 1rem; border-radius: var(--border-radius-md); border: 1px solid var(--border-color); background-color: var(--subtle-bg); color: var(--text-color); font-family: 'Courier New', Courier, monospace; resize: none; font-size: 0.9rem; }
.modern-button { padding: 0 1.5rem; height: 50px; border: none; border-radius: var(--border-radius-md); font-weight: 600; cursor: pointer; transition: var(--transition); background-color: var(--subtle-bg); color: var(--text-color); border: 1px solid var(--border-color); white-space: nowrap; }
.modern-button:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
.modern-button:active { transform: translateY(0); }
.modern-button.primary { background-color: var(--accent-color); color: white; border: none; }
.modern-button.primary:hover { background-color: var(--accent-color-hover); }
.modern-button:disabled { cursor: not-allowed; opacity: 0.6; }

/* Download Section */
.download-section { margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--border-color); }
.download-section h2 { font-size: 1.8rem; margin-bottom: 1.5rem; }
.download-controls { display: flex; justify-content: center; align-items: center; gap: 1rem; flex-wrap: wrap; }
.dropdown { height: 50px; padding: 0 1rem; border-radius: var(--border-radius-md); border: 1px solid var(--border-color); background-color: var(--bg-color); color: var(--text-color); font-family: var(--font-family); cursor: pointer; -webkit-appearance: none; -moz-appearance: none; appearance: none; background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='%2364748b' viewBox='0 0 16 16'%3E%3Cpath fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z'/%3E%3C/svg%3E"); background-repeat: no-repeat; background-position: right 0.7rem center; padding-right: 2.5rem; }

/* Content Sections (About, How-to, FAQ) */
.content-section { text-align: left; max-width: 800px; margin: 4rem auto 0 auto; padding-top: 2rem; border-top: 1px solid var(--border-color); }
.content-section h2 { font-size: 2rem; margin-bottom: 1.5rem; text-align: center; }
.content-section p, .content-section li { font-size: 1.1rem; line-height: 1.7; opacity: 0.9; margin-bottom: 1rem; }
.content-section ul { list-style-position: inside; padding-left: 1rem; }
.steps { counter-reset: step-counter; }
.steps li { counter-increment: step-counter; list-style: none; margin-bottom: 1.5rem; }
.steps li::before { content: counter(step-counter); font-weight: 700; font-size: 1.5rem; background-color: var(--accent-color); color: white; border-radius: 50%; width: 40px; height: 40px; display: inline-flex; align-items: center; justify-content: center; margin-right: 1rem; }

/* FAQ Accordion */
.faq-item { border-bottom: 1px solid var(--border-color); }
.faq-question { display: flex; justify-content: space-between; align-items: center; padding: 1.5rem 0; cursor: pointer; font-weight: 600; font-size: 1.2rem; }
.faq-question:hover { color: var(--accent-color); }
.faq-answer { max-height: 0; overflow: hidden; transition: max-height 0.4s ease-out; }
.faq-answer p { padding-bottom: 1.5rem; }
.faq-item.active .faq-answer { max-height: 300px; }
.faq-toggle { font-size: 2rem; transition: transform 0.3s; }
.faq-item.active .faq-toggle { transform: rotate(45deg); }

/* Footer */
.footer { text-align: center; padding: 3rem 1rem; margin-top: 4rem; border-top: 1px solid var(--border-color); }
.footer p { opacity: 0.7; }

/* Responsive */
@media (max-width: 768px) {
    h1 { font-size: 2.2rem; }
    .header .container { flex-direction: column; gap: 1rem; }
    .nav { margin-top: 0.5rem; }
    .nav a { margin: 0 0.5rem; }
    .download-controls { flex-direction: column; align-items: stretch; }
}
"""

# ==============================================================================
# 2. JAVASCRIPT LOGIC (script.js)
# This string contains all the JavaScript for interactivity.
# ==============================================================================
JAVASCRIPT_CONTENT = """
document.addEventListener('DOMContentLoaded', () => {
    // --- DOM Elements ---
    const gradientPreview = document.getElementById('gradient-preview');
    const colorInputsContainer = document.querySelector('.color-inputs');
    const cssCode = document.getElementById('css-code');
    const copyBtn = document.getElementById('copy-btn');
    const themeToggle = document.getElementById('theme-toggle');
    const downloadBtn = document.getElementById('download-btn');
    const formatSelect = document.getElementById('format-select');
    const sizeSelect = document.getElementById('size-select');
    
    // Elements specific to multi-color page
    const addColorBtn = document.getElementById('add-color-btn');
    const removeColorBtn = document.getElementById('remove-color-btn');

    const MIN_COLORS = 2;
    const MAX_COLORS = 10;

    const getRandomColor = () => '#' + Math.floor(Math.random()*16777215).toString(16).padStart(6, '0');

    // --- Gradient Logic ---
    const updateGradient = () => {
        if (!gradientPreview || !colorInputsContainer) return;
        
        const colorInputs = colorInputsContainer.querySelectorAll('.color-input');
        const colors = Array.from(colorInputs).map(input => input.value);
        
        if (colors.length < 2) return;

        const gradient = `linear-gradient(to right, ${colors.join(', ')})`;
        gradientPreview.style.background = gradient;
        cssCode.value = `background: ${gradient};`;

        if (removeColorBtn) {
            removeColorBtn.disabled = colors.length <= MIN_COLORS;
        }
        if (addColorBtn) {
            addColorBtn.disabled = colors.length >= MAX_COLORS;
        }
    };

    // --- Dynamic Color Input Management (for multi-color page) ---
    const addColorInput = () => {
        const colorInputs = colorInputsContainer.querySelectorAll('.color-input');
        if (colorInputs.length >= MAX_COLORS) return;

        const newColorInput = document.createElement('input');
        newColorInput.type = 'color';
        newColorInput.className = 'color-input';
        newColorInput.value = getRandomColor();
        newColorInput.setAttribute('aria-label', 'Color swatch');
        
        colorInputsContainer.appendChild(newColorInput);
        updateGradient();
    };

    const removeColorInput = () => {
        const colorInputs = colorInputsContainer.querySelectorAll('.color-input');
        if (colorInputs.length > MIN_COLORS) {
            colorInputs[colorInputs.length - 1].remove();
            updateGradient();
        }
    };

    // --- Image Download Logic ---
    const downloadGradient = () => {
        if (!gradientPreview || !downloadBtn) return;

        const [width, height] = sizeSelect.value.split('x').map(Number);
        const format = formatSelect.value;
        const extension = format.split('/')[1];
        
        const tempPreview = document.createElement('div');
        tempPreview.style.width = `${width}px`;
        tempPreview.style.height = `${height}px`;
        tempPreview.style.background = gradientPreview.style.background;
        document.body.appendChild(tempPreview);
        
        downloadBtn.textContent = 'Generating...';
        downloadBtn.disabled = true;

        html2canvas(tempPreview, { width, height, useCORS: true })
            .then(canvas => {
                const link = document.createElement('a');
                link.download = `tinyfont-me-gradient-${Date.now()}.${extension}`;
                link.href = canvas.toDataURL(format, 0.95);
                link.click();
            })
            .catch(err => {
                console.error("Image generation failed:", err);
                alert("Error generating image. Please try again.");
            })
            .finally(() => {
                document.body.removeChild(tempPreview);
                downloadBtn.textContent = 'Download Image';
                downloadBtn.disabled = false;
            });
    };

    // --- Clipboard & Theme ---
    const copyToClipboard = () => {
        navigator.clipboard.writeText(cssCode.value).then(() => {
            copyBtn.textContent = 'Copied!';
            setTimeout(() => { copyBtn.textContent = 'Copy CSS'; }, 2000);
        });
    };

    const applyTheme = (theme) => {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
    };

    const toggleTheme = () => {
        const newTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        applyTheme(newTheme);
    };

    // --- FAQ Accordion ---
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        item.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            faqItems.forEach(i => i.classList.remove('active'));
            if (!isActive) {
                item.classList.add('active');
            }
        });
    });

    // --- Event Listeners ---
    if (colorInputsContainer) {
        colorInputsContainer.addEventListener('input', (e) => {
            if (e.target.classList.contains('color-input')) {
                updateGradient();
            }
        });
    }

    if (copyBtn) copyBtn.addEventListener('click', copyToClipboard);
    if (themeToggle) themeToggle.addEventListener('click', toggleTheme);
    if (downloadBtn) downloadBtn.addEventListener('click', downloadGradient);
    if (addColorBtn) addColorBtn.addEventListener('click', addColorInput);
    if (removeColorBtn) removeColorBtn.addEventListener('click', removeColorInput);

    // --- Initial Setup ---
    const preferredTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    applyTheme(preferredTheme);
    updateGradient();
});
"""

# ==============================================================================
# 3. HTML TEMPLATE AND CONTENT GENERATION
# These functions build the HTML for each page.
# ==============================================================================

def generate_head(page_config):
    """Generates the <head> section of the HTML document."""
    return f"""
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_config['title']}</title>
    <meta name="description" content="{page_config['description']}">
    <meta name="keywords" content="{page_config['keywords']}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js" integrity="sha512-BNaRQnYJYiPSqHHDb58B0yaPfCu+Wgds8Gp/gU33kqBtgNS4tSPHuGibyoVBL5gI9kDXrdIGNORE/lenZsummaries.sourceforge.net/group__C45__API.html" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
</head>
"""

def generate_header(active_page):
    """Generates the <header> and navigation."""
    nav_links = {
        '3': '<a href="3-color-gradient-generator.html">3-Color</a>',
        '4': '<a href="4-color-gradient-generator.html">4-Color</a>',
        '5': '<a href="5-color-gradient-generator.html">5-Color</a>',
        'multi': '<a href="multi-color-gradient-generator.html">Multi-Color</a>'
    }
    # Add 'active' class to the current page's link
    nav_links[active_page] = nav_links[active_page].replace('href', 'class="active" href')
    
    return f"""
<header class="header">
    <div class="container">
        <a href="3-color-gradient-generator.html" class="logo">tinyfont.me</a>
        <nav class="nav">{''.join(nav_links.values())}</nav>
        <button id="theme-toggle" class="theme-toggle" aria-label="Toggle theme">
            <svg class="sun-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
            <svg class="moon-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        </button>
    </div>
</header>
"""

def generate_main_content(page_config):
    """Generates the main content area with the gradient tool."""
    
    # Generate color inputs
    color_inputs_html = ""
    for color in page_config['colors']:
        color_inputs_html += f'<input type="color" class="color-input" value="{color}" aria-label="Color swatch">'

    # Generate multi-color controls if needed
    multi_color_controls_html = ""
    if page_config['id'] == 'multi':
        multi_color_controls_html = """
        <div class="multi-color-controls">
            <button id="add-color-btn" class="modern-button color-action-btn" aria-label="Add color">+</button>
            <button id="remove-color-btn" class="modern-button color-action-btn remove-color-btn" aria-label="Remove last color">-</button>
        </div>
        """

    return f"""
<main class="main-content">
    <div class="container">
        <div class="card glassmorphism">
            <h1>{page_config['h1']}</h1>
            <p>{page_config['subheading']}</p>
            
            <div id="gradient-preview" class="gradient-preview"></div>

            <div class="controls">
                <div class="color-inputs">
                    {color_inputs_html}
                </div>
                {multi_color_controls_html}
            </div>

            <div class="output">
                <textarea id="css-code" readonly aria-label="CSS gradient code"></textarea>
                <button id="copy-btn" class="modern-button">Copy CSS</button>
            </div>

            <div class="download-section">
                <h2>Download Your Gradient</h2>
                <div class="download-controls">
                    <select id="format-select" class="dropdown" aria-label="Select image format">
                        <option value="image/png">PNG</option>
                        <option value="image/jpeg">JPEG</option>
                        <option value="image/webp">WebP</option>
                    </select>
                    <select id="size-select" class="dropdown" aria-label="Select image size">
                        <option value="1920x1080">Full HD (1920x1080)</option>
                        <option value="1280x720">HD (1280x720)</option>
                        <option value="3840x2160">4K UHD (3840x2160)</option>
                        <option value="2560x1440">QHD (2560x1440)</option>
                        <option value="1080x1080">Instagram Post (1080x1080)</option>
                        <option value="1080x1920">Instagram Story (1080x1920)</option>
                        <option value="1200x630">Facebook Post (1200x630)</option>
                        <option value="1024x512">Twitter Post (1024x512)</option>
                    </select>
                    <button id="download-btn" class="modern-button primary">Download Image</button>
                </div>
            </div>
        </div>

        <!-- SEO Content Sections -->
        <section class="content-section">
            <h2>About Our Gradient Generator</h2>
            <p>Welcome to the ultimate {page_config['h1']} on tinyfont.me. This free tool is designed for developers, designers, and content creators who need beautiful, high-quality gradients in seconds. Whether you're creating a website background, a social media graphic, or digital art, our generator provides the flexibility to create and export stunning visuals with ease. Forget complex software; generate CSS code or download high-resolution images directly from your browser.</p>
        </section>

        <section class="content-section">
            <h2>How to Use This Tool</h2>
            <ol class="steps">
                <li><strong>Select Your Colors:</strong> Click on the colored circles to open the color picker. Choose your desired hues. {'On the Multi-Color page, you can even add or remove colors using the "+" and "-" buttons.' if page_config['id'] == 'multi' else ''}</li>
                <li><strong>Preview Instantly:</strong> The gradient display at the top updates in real-time as you adjust the colors, giving you an immediate preview of your creation.</li>
                <li><strong>Copy the Code:</strong> Once you're happy with the gradient, click the "Copy CSS" button to grab the `linear-gradient` code for your web projects.</li>
                <li><strong>Download as an Image:</strong> Choose your desired format (PNG, JPEG, WebP) and resolution from the dropdown menus. Click "Download Image" to save the gradient as a high-quality file, ready for any project.</li>
            </ol>
        </section>

        <section class="content-section">
            <h2>Frequently Asked Questions</h2>
            <div class="faq-list">
                <div class="faq-item">
                    <div class="faq-question">What is a multi-color gradient?<span class="faq-toggle">+</span></div>
                    <div class="faq-answer"><p>A multi-color gradient is a smooth transition between two or more colors. While a classic gradient blends two colors, using three, four, five, or more colors allows for richer, more vibrant, and complex visual effects, perfect for modern design trends.</p></div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Can I download the gradient as a transparent PNG?<span class="faq-toggle">+</span></div>
                    <div class="faq-answer"><p>Currently, the tool generates opaque images. The PNG format downloaded from here will have a solid, non-transparent background. This is ideal for wallpapers, website backgrounds, and social media graphics.</p></div>
                </div>
                 <div class="faq-item">
                    <div class="faq-question">Is this tool completely free to use?<span class="faq-toggle">+</span></div>
                    <div class="faq-answer"><p>Yes, absolutely! Our {page_config['h1']} is 100% free for both personal and commercial projects. There are no hidden fees, watermarks, or limitations. Enjoy creating!</p></div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Which image format should I choose?<span class="faq-toggle">+</span></div>
                    <div class="faq-answer"><p>It depends on your needs. **PNG** is great for high-quality, lossless images. **JPEG** offers a good balance of quality and smaller file size. **WebP** is a modern format that provides excellent quality with significantly smaller file sizes, making it perfect for web use.</p></div>
                </div>
            </div>
        </section>
    </div>
</main>
"""

def generate_footer():
    """Generates the <footer>."""
    return """
<footer class="footer">
    <div class="container">
        <p>&copy; 2025 tinyfont.me. All Rights Reserved.</p>
        <p>A modern tool for modern creators.</p>
    </div>
</footer>
"""

def generate_html_file(page_config):
    """Assembles a full HTML page from components."""
    html_content = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
{generate_head(page_config)}
<body>
    {generate_header(page_config['id'])}
    {generate_main_content(page_config)}
    {generate_footer()}
    <script src="script.js"></script>
</body>
</html>
"""
    file_name = f"{page_config['id']}-color-gradient-generator.html"
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✅ Successfully created {file_name}")

# ==============================================================================
# 4. SITE CONFIGURATION & MAIN EXECUTION
# ==============================================================================

# Define the configuration for each page we want to generate
PAGES_CONFIG = [
    {
        'id': '3',
        'title': '3 Color Gradient Generator (PNG, WebP) | tinyfont.me',
        'description': 'Generate, customize, and download beautiful 3-color gradients as PNG, JPEG, or WebP images for free. Get CSS and hex codes instantly for your designs.',
        'keywords': '3 color gradient generator, 3 color gradient generator png, 3 color gradient generator free, 3 color gradient generator hex, multi color gradient generator, 3 color scale generator',
        'h1': '3-Color Gradient Generator',
        'subheading': 'Create and export beautiful three-color gradients for your projects.',
        'colors': ['#ff6b6b', '#feca57', '#48dbfb']
    },
    {
        'id': '4',
        'title': '4 Color Gradient Generator (PNG, WebP) | tinyfont.me',
        'description': 'Design and download custom 4-color gradients as high-resolution images (PNG, JPEG, WebP). The perfect tool for creating multi-color backgrounds.',
        'keywords': '4 color gradient generator, multi color gradient generator, color gradient, gradient generator free, download gradient image, color palette generator',
        'h1': '4-Color Gradient Generator',
        'subheading': 'Design complex, vibrant four-color gradients with ease.',
        'colors': ['#ff6b6b', '#feca57', '#48dbfb', '#1dd1a1']
    },
    {
        'id': '5',
        'title': '5 Color Gradient Generator (PNG, WebP) | tinyfont.me',
        'description': 'Create rich, multi-color gradients with five distinct colors. Download your creation as a high-quality PNG, JPEG, or WebP image for free.',
        'keywords': '5 color gradient generator, multi color gradient maker, illustrator gradient, color palette generator, download gradient background, hex color gradient',
        'h1': '5-Color Gradient Generator',
        'subheading': 'Craft intricate and beautiful five-color gradients for any use case.',
        'colors': ['#ff6b6b', '#feca57', '#48dbfb', '#1dd1a1', '#f368e0']
    },
    {
        'id': 'multi',
        'title': 'Multi-Color Gradient Generator (PNG, WebP) | tinyfont.me',
        'description': 'The ultimate tool for creating dynamic, multi-color gradients. Add, remove, and customize colors to generate unique backgrounds and download them as high-res images.',
        'keywords': 'multi color gradient generator, custom gradient generator, color gradient maker, dynamic gradient, gradient tool, css gradient, download background',
        'h1': 'Multi-Color Gradient Generator',
        'subheading': 'Unleash your creativity. Add or remove colors to design the perfect gradient.',
        'colors': ['#ff6b6b', '#feca57', '#48dbfb'] # Start with 3 colors
    }
]

def main():
    """Main function to generate all website files."""
    print("🚀 Starting website generation for tinyfont.me...")

    # Create CSS file
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(CSS_CONTENT)
    print("✅ Successfully created style.css")

    # Create JavaScript file
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(JAVASCRIPT_CONTENT)
    print("✅ Successfully created script.js")

    # Create all HTML files
    for config in PAGES_CONFIG:
        generate_html_file(config)

    print("\n🎉 All files have been generated successfully!")
    print("You can now open any of the .html files in your browser.")

if __name__ == '__main__':
    main()