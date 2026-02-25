#!/usr/bin/env python3
"""
PDF to Flipbook Converter
=========================
Converts a PDF file into page images for the flipbook template.

Requirements:
    pip install pdf2image Pillow

Usage:
    python convert_pdf.py your_newsletter.pdf

    Optional arguments:
    --dpi 200          Image quality (default: 200, higher = sharper but larger files)
    --quality 90       JPEG quality (default: 90, range: 1-100)
    --output ./pages   Output directory (default: ./pages)
    --title "My News"  Set the flipbook title

After running, the script will:
    1. Convert each PDF page to a JPEG image in the /pages/ folder
    2. Automatically update config.js with the correct page count and dimensions
    3. Print instructions for deploying to GitHub Pages

Note: You need 'poppler-utils' installed on your system.
    - macOS:   brew install poppler
    - Ubuntu:  sudo apt install poppler-utils
    - Windows: Download from https://github.com/oschwartz10612/poppler-windows/releases
"""

import argparse
import os
import re
import sys

def main():
    parser = argparse.ArgumentParser(
        description='Convert a PDF newsletter into a flipbook'
    )
    parser.add_argument('pdf', help='Path to the PDF file')
    parser.add_argument('--dpi', type=int, default=200,
                        help='Image resolution in DPI (default: 200)')
    parser.add_argument('--quality', type=int, default=90,
                        help='JPEG quality 1-100 (default: 90)')
    parser.add_argument('--output', default='./pages',
                        help='Output directory for page images (default: ./pages)')
    parser.add_argument('--title', default=None,
                        help='Set the flipbook title (default: PDF filename)')
    args = parser.parse_args()

    if not os.path.exists(args.pdf):
        print(f"Error: PDF file '{args.pdf}' not found.")
        sys.exit(1)

    try:
        from pdf2image import convert_from_path
        from PIL import Image
    except ImportError:
        print("Error: Required packages not installed.")
        print("Run: pip install pdf2image Pillow")
        sys.exit(1)

    # Create output directory
    os.makedirs(args.output, exist_ok=True)

    # Convert PDF to images
    print(f"Converting '{args.pdf}' at {args.dpi} DPI...")
    try:
        images = convert_from_path(args.pdf, dpi=args.dpi, fmt='jpeg')
    except Exception as e:
        print(f"Error converting PDF: {e}")
        print("\nMake sure 'poppler-utils' is installed on your system:")
        print("  macOS:   brew install poppler")
        print("  Ubuntu:  sudo apt install poppler-utils")
        print("  Windows: Download from https://github.com/oschwartz10612/poppler-windows/releases")
        sys.exit(1)

    total_pages = len(images)
    print(f"Found {total_pages} pages.")

    # Save each page
    for i, img in enumerate(images):
        filename = os.path.join(args.output, f'page_{i + 1}.jpg')
        img.save(filename, 'JPEG', quality=args.quality)
        w, h = img.size
        print(f"  Saved page {i + 1}/{total_pages}: {filename} ({w}x{h})")

    # Get page dimensions from first image
    first_img = images[0]
    page_w, page_h = first_img.size

    # Determine title
    title = args.title or os.path.splitext(os.path.basename(args.pdf))[0]

    # Update config.js with correct settings
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.js')
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = f.read()

        # Update totalPages
        config = re.sub(
            r'totalPages:\s*\d+',
            f'totalPages: {total_pages}',
            config
        )
        # Update pageWidth
        config = re.sub(
            r'pageWidth:\s*\d+',
            f'pageWidth: {page_w}',
            config
        )
        # Update pageHeight
        config = re.sub(
            r'pageHeight:\s*\d+',
            f'pageHeight: {page_h}',
            config
        )
        # Update title
        config = re.sub(
            r'title:\s*"[^"]*"',
            f'title: "{title}"',
            config
        )

        with open(config_path, 'w') as f:
            f.write(config)

        print(f"\nUpdated config.js:")
        print(f"  Title:  {title}")
        print(f"  Pages:  {total_pages}")
        print(f"  Size:   {page_w} x {page_h} pixels")
    else:
        print(f"\nWarning: config.js not found at {config_path}")
        print(f"Please manually update config.js with:")
        print(f"  totalPages: {total_pages}")
        print(f"  pageWidth: {page_w}")
        print(f"  pageHeight: {page_h}")

    print(f"""
{'='*60}
  CONVERSION COMPLETE!
{'='*60}

  Pages: {total_pages}
  Size:  {page_w} x {page_h} pixels
  Files: {args.output}/page_1.jpg through page_{total_pages}.jpg

  NEXT STEPS:

  1. Add interactive elements (optional):
       Open config.js and add links, videos, tooltips, etc.
       Use Ctrl+Shift+D in the flipbook to find coordinates.

  2. Test locally:
       python -m http.server 8080
       Open http://localhost:8080

  3. Deploy to GitHub Pages:
       git add -A
       git commit -m "Add newsletter flipbook"
       git push

  4. Embed in Good Barber (HTML widget):
       <iframe src="YOUR_GITHUB_PAGES_URL"
               width="100%" height="700"
               frameborder="0" allowfullscreen>
       </iframe>

{'='*60}
""")

if __name__ == '__main__':
    main()
