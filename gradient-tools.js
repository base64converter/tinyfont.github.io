
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
                cssValue = `background-color: #000000;\nbackground-image: ${gradient.replace(/\n\s\*/g, '')}`;
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

    // Custom Color Picker Logic
    const colorPickers = []; // To store instances of color pickers

    // Helper function to convert HSL to RGB
    function hslToRgb(h, s, l) {
        s /= 100;
        l /= 100;
        let c = (1 - Math.abs(2 * l - 1)) * s,
            x = c * (1 - Math.abs((h / 60) % 2 - 1)),
            m = l - c / 2,
            r = 0,
            g = 0,
            b = 0;

        if (0 <= h && h < 60) { r = c; g = x; b = 0; }
        else if (60 <= h && h < 120) { r = x; g = c; b = 0; }
        else if (120 <= h && h < 180) { r = 0; g = c; b = x; }
        else if (180 <= h && h < 240) { r = 0; g = x; b = c; }
        else if (240 <= h && h < 300) { r = x; g = 0; b = c; }
        else if (300 <= h && h < 360) { r = c; g = 0; b = x; }
        r = Math.round((r + m) * 255);
        g = Math.round((g + m) * 255);
        b = Math.round((b + m) * 255);

        return `rgb(${r}, ${g}, ${b})`;
    }

    // Helper function to convert RGB to Hex
    function rgbToHex(rgb) {
        const rgbMatch = rgb.match(/^rgba?[(](\d+),\s*(\d+),\s*(\d+)(?:,\s*(\d+\.?\d*))?[)]$/);
        if (!rgbMatch) return '';
        const r = parseInt(rgbMatch[1]);
        const g = parseInt(rgbMatch[2]);
        const b = parseInt(rgbMatch[3]);
        const a = rgbMatch[4] !== undefined ? parseFloat(rgbMatch[4]) : 1;

        const toHex = (c) => {
            const hex = c.toString(16);
            return hex.length === 1 ? "0" + hex : hex;
        };

        if (a === 1) {
            return `#${toHex(r)}${toHex(g)}${toHex(b)}`;
        } else {
            const alphaHex = toHex(Math.round(a * 255));
            return `#${toHex(r)}${toHex(g)}${toHex(b)}${alphaHex}`;
        }
    }

    // Helper function to convert Hex to HSL
    function hexToHsl(hex) {
        if (!hex || typeof hex !== 'string') return { h: 0, s: 0, l: 0, a: 1 };
        let r = 0, g = 0, b = 0, a = 1;

        // Handle #RGB, #RGBA, #RRGGBB, #RRGGBBAA
        if (hex.length === 4) {
            r = parseInt(hex[1] + hex[1], 16);
            g = parseInt(hex[2] + hex[2], 16);
            b = parseInt(hex[3] + hex[3], 16);
        } else if (hex.length === 5) {
            r = parseInt(hex[1] + hex[1], 16);
            g = parseInt(hex[2] + hex[2], 16);
            b = parseInt(hex[3] + hex[3], 16);
            a = parseInt(hex[4] + hex[4], 16) / 255;
        } else if (hex.length === 7) {
            r = parseInt(hex.substring(1, 3), 16);
            g = parseInt(hex.substring(3, 5), 16);
            b = parseInt(hex.substring(5, 7), 16);
        } else if (hex.length === 9) {
            r = parseInt(hex.substring(1, 3), 16);
            g = parseInt(hex.substring(3, 5), 16);
            b = parseInt(hex.substring(5, 7), 16);
            a = parseInt(hex.substring(7, 9), 16) / 255;
        }

        r /= 255; g /= 255; b /= 255;

        let max = Math.max(r, g, b), min = Math.min(r, g, b);
        let h, s, l = (max + min) / 2;

        if (max === min) {
            h = s = 0; // achromatic
        } else {
            let d = max - min;
            s = l > 0.5 ? d / (2 - max - min) : d / (max + min);

            switch (max) {
                case r: h = (g - b) / d + (g < b ? 6 : 0); break;
                case g: h = (b - r) / d + 2; break;
                case b: h = (r - g) / d + 4; break;
            }
            h /= 6;
        }

        return { h: h * 360, s: s * 100, l: l * 100, a: a };
    }

    // Function to update the color picker UI based on HSL values
    function updateColorPickerUI(pickerInstance) {
        const { h, s, l, a } = pickerInstance.hsl;
        const rgb = hslToRgb(h, s, l);
        const hex = rgbToHex(rgb);

        pickerInstance.hueSlider.value = h;
        pickerInstance.saturationSlider.value = s;
        pickerInstance.lightnessSlider.value = l;
        pickerInstance.opacitySlider.value = a * 100;
        pickerInstance.hexInput.value = hex;
        pickerInstance.colorSwatch.style.backgroundColor = `hsla(${h}, ${s}%, ${l}%, ${a})`;

        // Update CSS variables for slider backgrounds
        pickerInstance.colorPickerPopup.style.setProperty('--current-hue', h);
        pickerInstance.colorPickerPopup.style.setProperty('--current-saturation', `${s}%`);
        pickerInstance.colorPickerPopup.style.setProperty('--current-lightness', `${l}%`);

        // Update saturation and lightness slider backgrounds dynamically
        pickerInstance.saturationSlider.style.background = `linear-gradient(to right, hsla(${h}, 0%, ${l}%, ${a}), hsla(${h}, 100%, ${l}%, ${a}))`;
        pickerInstance.lightnessSlider.style.background = `linear-gradient(to right, hsla(${h}, ${s}%, 0%, ${a}), hsla(${h}, ${s}%, 50%, ${a}), hsla(${h}, ${s}%, 100%, ${a}))`;
        pickerInstance.opacitySlider.style.background = `linear-gradient(to right, hsla(${h}, ${s}%, ${l}%, 0), hsla(${h}, ${s}%, ${l}%, 1))`;

        // Update the color spectrum selector position
        const spectrumRect = pickerInstance.colorSpectrum.getBoundingClientRect();
        const selectorX = (s / 100) * spectrumRect.width;
        const selectorY = (1 - l / 100) * spectrumRect.height; // Invert lightness for Y-axis
        pickerInstance.spectrumSelector.style.left = `${selectorX}px`;
        pickerInstance.spectrumSelector.style.top = `${selectorY}px`;

        // Trigger a custom event to notify parent of color change
        const event = new CustomEvent('colorChange', { detail: { color: `hsla(${h}, ${s}%, ${l}%, ${a})` } });
        pickerInstance.colorSwatch.dispatchEvent(event);
    }

    // Initialize color pickers
    document.querySelectorAll('.custom-color-input-wrapper').forEach(wrapper => {
        const colorSwatch = wrapper.querySelector('.color-swatch');
        const colorPickerPopup = wrapper.querySelector('.color-picker-popup');
        const hueSlider = colorPickerPopup.querySelector('.hue-range');
        const saturationSlider = colorPickerPopup.querySelector('.saturation-range');
        const lightnessSlider = colorPickerPopup.querySelector('.lightness-range');
        const opacitySlider = colorPickerPopup.querySelector('.opacity-range');
        const hexInput = colorPickerPopup.querySelector('.hex-input');
        const closeBtn = colorPickerPopup.querySelector('.close-picker-btn');
        const colorSpectrum = colorPickerPopup.querySelector('.color-spectrum');
        const spectrumSelector = document.createElement('div');
        spectrumSelector.classList.add('color-spectrum-selector');
        colorSpectrum.appendChild(spectrumSelector);

        let initialColor = colorSwatch.dataset.color || '#000000';
        let hsl = hexToHsl(initialColor);

        const pickerInstance = { 
            colorSwatch, colorPickerPopup, hueSlider, saturationSlider, lightnessSlider, opacitySlider, hexInput, closeBtn, colorSpectrum, spectrumSelector, hsl 
        };
        colorPickers.push(pickerInstance);

        // Set initial color and update UI
        updateColorPickerUI(pickerInstance);

        // Event Listeners for picker
        colorSwatch.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent body click from closing immediately
            // Close other open pickers
            colorPickers.forEach(p => {
                if (p !== pickerInstance) p.colorPickerPopup.classList.remove('active');
            });
            pickerInstance.colorPickerPopup.classList.toggle('active');
        });

        closeBtn.addEventListener('click', () => {
            pickerInstance.colorPickerPopup.classList.remove('active');
        });

        hueSlider.addEventListener('input', () => {
            pickerInstance.hsl.h = parseFloat(hueSlider.value);
            updateColorPickerUI(pickerInstance);
        });
        saturationSlider.addEventListener('input', () => {
            pickerInstance.hsl.s = parseFloat(saturationSlider.value);
            updateColorPickerUI(pickerInstance);
        });
        lightnessSlider.addEventListener('input', () => {
            pickerInstance.hsl.l = parseFloat(lightnessSlider.value);
            updateColorPickerUI(pickerInstance);
        });
        opacitySlider.addEventListener('input', () => {
            pickerInstance.hsl.a = parseFloat(opacitySlider.value) / 100;
            updateColorPickerUI(pickerInstance);
        });

        hexInput.addEventListener('change', () => {
            const newHex = hexInput.value;
            if (newHex.match(/^#([0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$/)) {
                pickerInstance.hsl = hexToHsl(newHex);
                updateColorPickerUI(pickerInstance);
            } else {
                alert('Invalid Hex color format. Please use #RGB, #RGBA, #RRGGBB, or #RRGGBBAA.');
                hexInput.value = rgbToHex(hslToRgb(pickerInstance.hsl.h, pickerInstance.hsl.s, pickerInstance.hsl.l)); // Revert
            }
        });

        // Spectrum selector drag logic
        let isDraggingSpectrum = false;
        colorSpectrum.addEventListener('mousedown', (e) => {
            isDraggingSpectrum = true;
            updateSpectrumColor(e);
        });
        colorSpectrum.addEventListener('mousemove', (e) => {
            if (isDraggingSpectrum) updateSpectrumColor(e);
        });
        colorSpectrum.addEventListener('mouseup', () => {
            isDraggingSpectrum = false;
        });
        colorSpectrum.addEventListener('mouseleave', () => {
            isDraggingSpectrum = false;
        });

        function updateSpectrumColor(e) {
            const spectrumRect = colorSpectrum.getBoundingClientRect();
            let x = e.clientX - spectrumRect.left;
            let y = e.clientY - spectrumRect.top;

            // Clamp values
            x = Math.max(0, Math.min(x, spectrumRect.width));
            y = Math.max(0, Math.min(y, spectrumRect.height));

            // Calculate saturation and lightness from x, y
            pickerInstance.hsl.s = (x / spectrumRect.width) * 100;
            pickerInstance.hsl.l = (1 - y / spectrumRect.height) * 100; // Invert lightness for Y-axis

            updateColorPickerUI(pickerInstance);
        }
    });

    // Close color picker when clicking outside
    document.addEventListener('click', (e) => {
        colorPickers.forEach(pickerInstance => {
            if (!pickerInstance.colorPickerPopup.contains(e.target) && !pickerInstance.colorSwatch.contains(e.target)) {
                pickerInstance.colorPickerPopup.classList.remove('active');
            }
        });
    });

    // Update gradient based on custom color picker changes
    document.querySelectorAll('.color-swatch').forEach(swatch => {
        swatch.addEventListener('colorChange', () => {
            // Collect all current colors from swatches
            const currentColors = colorPickers.map(pickerInstance => {
                const { h, s, l, a } = pickerInstance.hsl;
                // Convert HSL to RGBA for the gradient
                const rgb = hslToRgb(h, s, l); // This returns "rgb(r, g, b)"
                const rgbMatch = rgb.match(/^rgb[(](\d+),\s*(\d+),\s*(\d+)[)]$/);
                if (rgbMatch) {
                    const r = parseInt(rgbMatch[1]);
                    const g = parseInt(rgbMatch[2]);
                    const b = parseInt(rgbMatch[3]);
                    return `rgba(${r}, ${g}, ${b}, ${a})`;
                }
                return `rgba(0,0,0,1)`; // Fallback
            });
            // Update the main gradient preview and CSS code
            updateGradientFromCustomColors(currentColors);
        });
    });

    // New function to update gradient from custom color picker values
    function updateGradientFromCustomColors(colors) {
        let gradient;
        let cssValue;

        // Reset background color for non-mesh gradients
        gradientPreview.style.backgroundColor = '';

        switch (gradientType) {
            case 'mesh':
                const meshColors = [...colors];
                while (meshColors.length < 4) {
                    meshColors.push('rgba(0,0,0,1)'); // Default to opaque black
                }
                gradient = `radial-gradient(at 0% 0%, ${meshColors[0]} 0px, transparent 50%),
                            radial-gradient(at 90% 10%, ${meshColors[1]} 0px, transparent 50%),
                            radial-gradient(at 20% 80%, ${meshColors[2]} 0px, transparent 50%),
                            radial-gradient(at 70% 70%, ${meshColors[3]} 0px, transparent 50%)`;
                cssValue = `background-color: #000000;\nbackground-image: ${gradient.replace(/\n\s\*/g, '')}`;
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
    }

    // Initial Setup (modified to use custom color logic)
    const preferredTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    applyTheme(preferredTheme);
    // Initial gradient update should now use the custom color logic
    const initialColors = Array.from(document.querySelectorAll('.color-swatch')).map(s => s.dataset.color);
    updateGradientFromCustomColors(initialColors);
});
