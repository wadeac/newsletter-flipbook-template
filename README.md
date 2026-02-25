# Newsletter Flipbook Template

A ready-to-use template for converting PDF newsletters into interactive, embeddable flipbooks with realistic page-turning animations. Perfect for embedding in **Good Barber**, websites, or any platform that supports HTML/iframe widgets.

![Flipbook Preview](https://img.shields.io/badge/status-ready--to--use-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue)

---

## Features

- Realistic page-flip animation with drag, click, and swipe support
- Fully responsive — works on desktop, tablet, and mobile
- Keyboard navigation (arrow keys, Home/End)
- Fullscreen mode
- Page counter with first/last page jump buttons
- Lightweight — no server required, runs entirely in the browser
- Easy to embed via iframe in Good Barber, WordPress, Wix, etc.

---

## Quick Start

### Option A: Automatic (with Python)

> Requires Python 3.7+ and `poppler-utils` installed on your system.

```bash
# 1. Clone this template
git clone https://github.com/wadeac/newsletter-flipbook-template.git my-newsletter
cd my-newsletter

# 2. Install Python dependencies
pip install pdf2image Pillow

# 3. Convert your PDF
python convert_pdf.py your_newsletter.pdf

# 4. Test locally
python -m http.server 8080
# Open http://localhost:8080 in your browser

# 5. Deploy to GitHub Pages
git add -A
git commit -m "Add newsletter"
git push
```

### Option B: Manual Setup

1. **Convert your PDF to images** using any tool (Adobe Acrobat, online converters, Preview on Mac, etc.)
2. **Name the images** `page_1.jpg`, `page_2.jpg`, `page_3.jpg`, etc.
3. **Place them** in the `/pages/` folder
4. **Edit `index.html`** — update the configuration at the top of the `<script>` section:

```javascript
const TOTAL_PAGES = 10;              // Change to your page count
const BACKGROUND_COLOR = '#2c3e50';  // Change the background color
const PAGE_ASPECT_W = 1700;          // Width of your images in pixels
const PAGE_ASPECT_H = 2200;          // Height of your images in pixels
```

5. **Test locally** by opening `index.html` in a browser, or run:
```bash
python -m http.server 8080
```

---

## Deploying to GitHub Pages

1. Create a new GitHub repository
2. Push your flipbook files to the repository:
```bash
git init
git add -A
git commit -m "Add newsletter flipbook"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin master
```
3. Go to **Settings → Pages** in your repository
4. Under **Source**, select **Deploy from a branch**
5. Set branch to **master** and folder to **/ (root)**
6. Click **Save**
7. Your flipbook will be live at: `https://YOUR_USERNAME.github.io/YOUR_REPO/`

---

## Embedding in Good Barber

Once your flipbook is deployed, embed it in Good Barber using an **HTML widget**:

### Method 1: Custom HTML Section
1. In Good Barber, go to **Content → Add a section**
2. Choose **Custom Code / HTML**
3. Paste this embed code (replace the URL with yours):

```html
<iframe
  src="https://YOUR_USERNAME.github.io/YOUR_REPO/"
  width="100%"
  height="700"
  frameborder="0"
  allowfullscreen
  style="border: none; border-radius: 8px;">
</iframe>
```

### Method 2: Click-to-Web Section
1. Add a **Click-to** section in Good Barber
2. Choose **Web link**
3. Enter your flipbook URL

---

## Customization

### Background Color
Change `BACKGROUND_COLOR` in `index.html`:
```javascript
const BACKGROUND_COLOR = '#2c3e50';  // Dark blue-gray (default)
const BACKGROUND_COLOR = '#1a1a2e';  // Dark navy
const BACKGROUND_COLOR = '#0d1117';  // GitHub dark
const BACKGROUND_COLOR = '#ffffff';  // White
```

### Page Flip Speed
Change `FLIP_TIME` in `index.html` (in milliseconds):
```javascript
const FLIP_TIME = 800;   // Default
const FLIP_TIME = 500;   // Faster
const FLIP_TIME = 1200;  // Slower
```

### Newsletter Title
Update the `<title>` tag in `index.html`:
```html
<title>Your Newsletter Name - Issue XX</title>
```

---

## File Structure

```
newsletter-flipbook-template/
├── index.html              ← Main flipbook viewer (edit config here)
├── page-flip.browser.js    ← Page flip animation library (do not edit)
├── convert_pdf.py          ← PDF to images converter script
├── README.md               ← This file
└── pages/                  ← Put your page images here
    ├── page_1.jpg
    ├── page_2.jpg
    ├── page_3.jpg
    └── ...
```

---

## Installing poppler-utils

The `convert_pdf.py` script requires `poppler-utils`:

| Platform | Command |
|----------|---------|
| macOS    | `brew install poppler` |
| Ubuntu/Debian | `sudo apt install poppler-utils` |
| Windows  | Download from [poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases) |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Pages appear blank | Check that images are named `page_1.jpg`, `page_2.jpg`, etc. |
| Wrong page count | Update `TOTAL_PAGES` in `index.html` |
| Pages look stretched | Update `PAGE_ASPECT_W` and `PAGE_ASPECT_H` to match your image dimensions |
| Flipbook not loading in iframe | Ensure the hosting URL uses HTTPS |
| Script error on convert | Install `poppler-utils` (see above) |

---

## License

MIT License — free to use, modify, and distribute.

---

*Built with [StPageFlip](https://github.com/Nodlik/StPageFlip)*
