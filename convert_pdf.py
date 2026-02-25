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

After running, the script will:
    1. Convert each PDF page to a JPEG image in the /pages/ folder
    2. Automatically update index.html with the correct page count
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

    # Get page dimensions from first image for aspect ratio
    first_img = images[0]
    page_w, page_h = first_img.size

    # Update index.html with correct page count and dimensions
    index_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
    if os.path.exists(index_path):
        with open(index_path, 'r') as f:
            html = f.read()

        # Update TOTAL_PAGES
        html = re.sub(
            r"const TOTAL_PAGES = \d+;",
            f"const TOTAL_PAGES = {total_pages};",
            html
        )
        # Update page dimensions
        html = re.sub(
            r"const PAGE_ASPECT_W = \d+;",
            f"const PAGE_ASPECT_W = {page_w};",
            html
        )
        html = re.sub(
            r"const PAGE_ASPECT_H = \d+;",
            f"const PAGE_ASPECT_H = {page_h};",
            html
        )

        with open(index_path, 'w') as f:
            f.write(html)

        print(f"\nUpdated index.html: {total_pages} pages, {page_w}x{page_h} dimensions")
    else:
        print(f"\nWarning: index.html not found at {index_path}")
        print(f"Please manually set TOTAL_PAGES = {total_pages} in your index.html")

    print(f"""
{'='*60}
  CONVERSION COMPLETE!
{'='*60}

  Pages: {total_pages}
  Size:  {page_w} x {page_h} pixels
  Files: {args.output}/page_1.jpg through page_{total_pages}.jpg

  NEXT STEPS:
  1. Test locally:
       python -m http.server 8080
       Open http://localhost:8080

  2. Deploy to GitHub Pages:
       git add -A
       git commit -m "Add newsletter flipbook"
       git push

  3. Embed in Good Barber (HTML widget):
       <iframe src="YOUR_GITHUB_PAGES_URL"
               width="100%" height="600"
               frameborder="0" allowfullscreen>
       </iframe>

{'='*60}
""")

if __name__ == '__main__':
    main()
