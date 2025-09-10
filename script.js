
document.addEventListener('DOMContentLoaded', () => {
    const gradientPreview = document.getElementById('gradient-preview');
    const colorInputs = document.querySelectorAll('.color-input');
    const cssCode = document.getElementById('css-code');
    const copyBtn = document.getElementById('copy-btn');
    const themeToggle = document.getElementById('theme-toggle');
    const downloadBtn = document.getElementById('download-btn');
    const formatSelect = document.getElementById('format-select');
    const sizeSelect = document.getElementById('size-select');
    
    const gradientType = document.body.dataset.gradientType || 'linear';

    const updateGradient = () => {
        if (!gradientPreview || !colorInputs.length) return;

        const colors = Array.from(colorInputs).map(input => input.value);
        let gradient;
        let cssValue;
        
        // Reset background color for non-mesh gradients
        gradientPreview.style.backgroundColor = '';

        switch (gradientType) {
            case 'mesh':
                // Ensure there are enough colors for mesh, provide defaults if not
                const meshColors = [...colors];
                while (meshColors.length < 4) {
                    meshColors.push('#000000');
                }
                gradient = `radial-gradient(at 0% 0%, ${meshColors[0]} 0px, transparent 50%),
                            radial-gradient(at 90% 10%, ${meshColors[1]} 0px, transparent 50%),
                            radial-gradient(at 20% 80%, ${meshColors[2]} 0px, transparent 50%),
                            radial-gradient(at 70% 70%, ${meshColors[3]} 0px, transparent 50%)`;
                cssValue = `background-color: #000000;\nbackground-image: ${gradient.replace(/\n\s*/g, '')}`;
                gradientPreview.style.backgroundColor = '#000000';
                break;
            case 'radial':
                gradient = `radial-gradient(circle, ${colors.join(', ')})`;
                cssValue = `background: ${gradient};`;
                break;
            case 'linear':
            default:
                gradient = `linear-gradient(to right, ${colors.join(', ')})`;
                cssValue = `background: ${gradient};`;
                break;
        }
        
        gradientPreview.style.background = gradient;
        if(cssCode) {
            cssCode.value = cssValue;
        }
    };

    const downloadGradient = () => {
        if (!downloadBtn) return;
        const [width, height] = sizeSelect.value.split('x').map(Number);
        const format = formatSelect.value;
        const extension = format.includes('jpeg') ? 'jpg' : format.split('/')[1];
        
        const tempPreview = document.createElement('div');
        tempPreview.style.width = `${width}px`;
        tempPreview.style.height = `${height}px`;
        tempPreview.style.background = gradientPreview.style.background;
        tempPreview.style.backgroundColor = gradientPreview.style.backgroundColor;
        document.body.appendChild(tempPreview);
        
        downloadBtn.textContent = 'Generating...';
        downloadBtn.disabled = true;

        html2canvas(tempPreview, { width, height, useCORS: true, logging: false })
            .then(canvas => {
                const link = document.createElement('a');
                link.download = `tinyfont-me-gradient-${Date.now()}.${extension}`;
                link.href = canvas.toDataURL(format, 0.98);
                link.click();
            })
            .catch(err => {
                console.error("Oops, something went wrong!", err);
                alert("Sorry, could not generate the image. Please try again.");
            })
            .finally(() => {
                document.body.removeChild(tempPreview);
                downloadBtn.textContent = 'Download Image';
                downloadBtn.disabled = false;
            });
    };

    const copyToClipboard = () => {
        if (!copyBtn || !cssCode) return;
        navigator.clipboard.writeText(cssCode.value).then(() => {
            copyBtn.textContent = 'Copied!';
            setTimeout(() => { copyBtn.textContent = 'Copy CSS'; }, 2000);
        }, () => {
            alert('Failed to copy. Please copy manually.');
        });
    };

    const applyTheme = (theme) => {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
    };
    
    if(themeToggle) {
        themeToggle.addEventListener('click', () => {
            const newTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
            applyTheme(newTheme);
        });
    }

    document.querySelectorAll('.faq-item .faq-question').forEach(question => {
        question.addEventListener('click', () => {
            const faqItem = question.parentElement;
            const currentlyActive = faqItem.classList.contains('active');
            document.querySelectorAll('.faq-item.active').forEach(item => item.classList.remove('active'));
            if (!currentlyActive) {
                faqItem.classList.add('active');
            }
        });
    });

    colorInputs.forEach(input => input.addEventListener('input', updateGradient));
    if (copyBtn) copyBtn.addEventListener('click', copyToClipboard);
    if (downloadBtn) downloadBtn.addEventListener('click', downloadGradient);

    // Burger menu logic
    const menuToggle = document.querySelector('.menu-toggle');
    const mobileNav = document.querySelector('.mobile-nav');
    const mobileNavOverlay = document.querySelector('.mobile-nav-overlay');
    const body = document.body;

    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            body.classList.toggle('menu-open');
        });
    }

    if (mobileNavOverlay) {
        mobileNavOverlay.addEventListener('click', () => {
            body.classList.remove('menu-open');
        });
    }

    if (mobileNav) {
        mobileNav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                body.classList.remove('menu-open');
            });
        });
    }

    // Initial Setup
    const preferredTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    applyTheme(preferredTheme);
    updateGradient();
});
