# Interactive Newsletter Flipbook Template

Create beautiful, interactive flipbooks from PDF newsletters — with clickable links, embedded videos, image zoom, tooltips, and a table of contents. No coding required.

---

## What You Get

| Feature | Description |
|---------|-------------|
| **Page-Flip Animation** | Realistic flip effect with drag, click, and swipe support |
| **Clickable Links** | Add invisible hotspot areas that open URLs when clicked |
| **Embedded Videos** | Play YouTube/Vimeo videos in a sleek overlay |
| **Image Zoom** | Tap to view images full-screen with zoom |
| **Tooltips** | Hover/tap info bubbles with extra context |
| **Table of Contents** | Slide-out panel with page thumbnails for quick navigation |
| **Design Mode** | Built-in coordinate finder (Ctrl+Shift+D) |
| **Responsive** | Works on desktop, tablet, and mobile |
| **Fullscreen** | Toggle fullscreen viewing |
| **Keyboard Nav** | Arrow keys, Home/End support |

---

## Quick Start (3 Steps)

### Step 1: Get the Template

```bash
git clone https://github.com/wadeac/newsletter-flipbook-template.git my-newsletter
cd my-newsletter
```

Or download the ZIP file and extract it.

### Step 2: Add Your PDF Pages

**Option A — Automatic (recommended):**
```bash
pip install pdf2image Pillow
python convert_pdf.py your_newsletter.pdf
```
This converts your PDF and auto-configures everything.

**Option B — Manual:**
1. Convert your PDF to images using any tool (Adobe, Preview, online converters)
2. Name them `page_1.jpg`, `page_2.jpg`, `page_3.jpg`, etc.
3. Place them in the `/pages/` folder
4. Open `config.js` and update `totalPages` to match your page count

### Step 3: Test It

```bash
python -m http.server 8080
```
Open **http://localhost:8080** in your browser.

---

## Adding Interactive Elements

All interactive elements are configured in **`config.js`** — the only file you need to edit. Each element uses **percentage-based coordinates** (0-100), so they work at any screen size.

### Finding Coordinates

You have two options:

**Option 1: Design Mode (easiest)**
1. Open your flipbook in a browser
2. Press **Ctrl+Shift+D** to enter Design Mode
3. Click anywhere on a page — coordinates are shown and copied to clipboard
4. Use those values in `config.js`

**Option 2: Calculate from image dimensions**
1. Open your page image in any image editor
2. Note the pixel position of where you want the element
3. Convert to percentage:
   - `x% = (pixel_x ÷ image_width) × 100`
   - `y% = (pixel_y ÷ image_height) × 100`

> **Example:** Your image is 1700×2200 pixels. You want a link at pixel (850, 1760).
> - x = (850 ÷ 1700) × 100 = **50**
> - y = (1760 ÷ 2200) × 100 = **80**

---

### Adding Clickable Links

Links create invisible hotspot areas that open a URL when clicked. They show a subtle highlight and tooltip on hover.

```javascript
links: [
  {
    page: 1,           // Which page (1, 2, 3, etc.)
    x: 55,             // Left position (%)
    y: 80,             // Top position (%)
    width: 20,         // Width of clickable area (%)
    height: 5,         // Height of clickable area (%)
    url: "https://dacc.nmsu.edu",
    label: "Visit DACC Website"   // Tooltip text (optional)
  },
],
```

**Common uses:** "Read More" buttons, email links (`mailto:...`), social media links, website references.

---

### Adding Embedded Videos

Videos show a play button that opens a YouTube or Vimeo video in a modal overlay.

```javascript
videos: [
  {
    page: 3,           // Which page
    x: 25,             // Left position (%)
    y: 40,             // Top position (%)
    width: 50,         // Width of play button area (%)
    height: 30,        // Height of play button area (%)
    videoUrl: "https://www.youtube.com/watch?v=YOUR_VIDEO_ID",
    label: "Watch the campus tour"   // Tooltip text (optional)
  },
],
```

**Supported formats:** YouTube links, Vimeo links, or any embed URL.

---

### Adding Image Zoom

Zoom areas let readers tap to see an image full-screen.

```javascript
zoomAreas: [
  {
    page: 4,           // Which page
    x: 10,             // Left position (%)
    y: 20,             // Top position (%)
    width: 35,         // Width of zoomable area (%)
    height: 40,        // Height of zoomable area (%)
    caption: "Spring 2026 Event Schedule"   // Caption text (optional)
  },
],
```

**Common uses:** Flyers, schedules, detailed graphics, photos.

---

### Adding Tooltips

Tooltips show a small "i" icon that reveals extra information on hover or tap.

```javascript
tooltips: [
  {
    page: 2,           // Which page
    x: 75,             // Position (%)
    y: 15,             // Position (%)
    text: "Office hours: Mon-Fri 8am-5pm",
    color: "#3498db"   // Icon color (optional, default: blue)
  },
],
```

**Color options:** `#3498db` (blue), `#e74c3c` (red), `#2ecc71` (green), `#f39c12` (orange), `#9b59b6` (purple).

---

### Setting Up Table of Contents

Define named sections for the navigation panel.

```javascript
tableOfContents: [
  { page: 1,  title: "Cover" },
  { page: 2,  title: "Letter from the Editor" },
  { page: 4,  title: "Campus Events" },
  { page: 6,  title: "Student Spotlight" },
  { page: 8,  title: "Resources" },
  { page: 10, title: "Back Cover" },
],
```

If you leave this empty, the panel will show all pages with default names.

---

## Deploying to GitHub Pages

1. Create a new GitHub repository
2. Push your files:
```bash
git init
git add -A
git commit -m "Add newsletter flipbook"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin master
```
3. Go to **Settings → Pages** in your repository
4. Set **Source** to **Deploy from a branch**
5. Set branch to **master**, folder to **/ (root)**
6. Click **Save**
7. Your flipbook will be live at: `https://YOUR_USERNAME.github.io/YOUR_REPO/`

---

## Embedding in Good Barber

### Method 1: Custom HTML Section (Recommended)
1. In Good Barber, go to **Content → Add a section**
2. Choose **Custom Code / HTML**
3. Paste this embed code:

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
1. Add a **Click-to** section
2. Choose **Web link**
3. Enter your flipbook URL

---

## Customization

Open `config.js` and change these values:

| Setting | Default | Description |
|---------|---------|-------------|
| `title` | `"Newsletter"` | Browser tab title |
| `backgroundColor` | `"#2c3e50"` | Background color around the book |
| `flipTime` | `800` | Page flip speed in milliseconds |

---

## File Structure

```
your-flipbook/
├── index.html              ← Flipbook viewer (do not edit)
├── config.js               ← YOUR CONFIGURATION (edit this!)
├── page-flip.browser.js    ← Animation library (do not edit)
├── convert_pdf.py          ← PDF converter script
├── README.md               ← This file
└── pages/                  ← Your page images go here
    ├── page_1.jpg
    ├── page_2.jpg
    └── ...
```

---

## Installing poppler-utils (for PDF converter)

| Platform | Command |
|----------|---------|
| macOS | `brew install poppler` |
| Ubuntu/Debian | `sudo apt install poppler-utils` |
| Windows | Download from [poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases) |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Pages appear blank | Check that images are named `page_1.jpg`, `page_2.jpg`, etc. |
| Wrong page count | Update `totalPages` in `config.js` |
| Pages look stretched | Update `pageWidth` and `pageHeight` in `config.js` |
| Links not clickable | Check coordinates using Design Mode (Ctrl+Shift+D) |
| Video won't play | Use a standard YouTube or Vimeo URL |
| Flipbook not loading in iframe | Ensure the hosting URL uses HTTPS |

---

## License

MIT License — free to use, modify, and distribute.

*Built with [StPageFlip](https://github.com/Nodlik/StPageFlip)*
