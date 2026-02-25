// ============================================================
//  FLIPBOOK CONFIGURATION FILE
//  ============================================================
//  This is the ONLY file you need to edit!
//
//  HOW COORDINATES WORK:
//  - All positions use PERCENTAGES (0-100), not pixels
//  - x = horizontal position (0 = left edge, 100 = right edge)
//  - y = vertical position (0 = top edge, 100 = bottom edge)
//  - width/height = size as percentage of the page
//
//  HOW TO FIND COORDINATES:
//  1. Open your page image in any image editor (or even MS Paint)
//  2. Note the pixel position of where you want the element
//  3. Divide by the image dimensions and multiply by 100
//     Example: Image is 1700x2200, element is at pixel (850, 1100)
//     x = (850 / 1700) × 100 = 50
//     y = (1100 / 2200) × 100 = 50
//
//  OR use the built-in helper tool:
//  - Open your flipbook and press Ctrl+Shift+D to enter "Design Mode"
//  - Click anywhere on a page to see the coordinates
//  - Copy them directly into this file
// ============================================================

const FLIPBOOK_CONFIG = {

  // ----------------------------------------------------------
  //  BASIC SETTINGS
  // ----------------------------------------------------------
  title: "DACC Newsletter - Issue 05",    // Browser tab title
  totalPages: 10,                          // Number of pages
  backgroundColor: "#2c3e50",              // Background color
  pageWidth: 1700,                         // Your image width in pixels
  pageHeight: 2200,                        // Your image height in pixels
  flipTime: 800,                           // Page flip speed (milliseconds)

  // ----------------------------------------------------------
  //  CLICKABLE LINKS
  //  Add invisible hotspot areas that open URLs when clicked
  // ----------------------------------------------------------
  //  page:    which page number (1, 2, 3, etc.)
  //  x, y:    position as percentage from top-left corner
  //  width:   width as percentage of page
  //  height:  height as percentage of page
  //  url:     the web address to open
  //  label:   tooltip text shown on hover (optional)
  // ----------------------------------------------------------
  links: [
    // EXAMPLE: A "Read More" button on page 1
    // {
    //   page: 1,
    //   x: 55,
    //   y: 83,
    //   width: 18,
    //   height: 4,
    //   url: "https://dacc.nmsu.edu",
    //   label: "Visit DACC Website"
    // },

    // EXAMPLE: An email link on page 2
    // {
    //   page: 2,
    //   x: 10,
    //   y: 25,
    //   width: 30,
    //   height: 3,
    //   url: "mailto:info@dacc.nmsu.edu",
    //   label: "Send us an email"
    // },
  ],

  // ----------------------------------------------------------
  //  EMBEDDED VIDEOS
  //  Add play buttons that open YouTube/Vimeo videos
  // ----------------------------------------------------------
  //  page:    which page number
  //  x, y:    center position of the play button (percentage)
  //  width:   width of the clickable area (percentage)
  //  height:  height of the clickable area (percentage)
  //  videoUrl: YouTube or Vimeo link (regular watch URL is fine)
  //  label:   tooltip text shown on hover (optional)
  // ----------------------------------------------------------
  videos: [
    // EXAMPLE: A video on page 3
    // {
    //   page: 3,
    //   x: 25,
    //   y: 50,
    //   width: 50,
    //   height: 30,
    //   videoUrl: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    //   label: "Watch the campus tour"
    // },
  ],

  // ----------------------------------------------------------
  //  IMAGE ZOOM / SPOTLIGHT
  //  Mark areas that can be tapped to view full-screen with zoom
  // ----------------------------------------------------------
  //  page:      which page number
  //  x, y:      position of the zoomable area (percentage)
  //  width:     width of the zoomable area (percentage)
  //  height:    height of the zoomable area (percentage)
  //  imageUrl:  (optional) URL to a higher-res image; if omitted,
  //             the area from the page image is used
  //  caption:   text shown below the zoomed image (optional)
  // ----------------------------------------------------------
  zoomAreas: [
    // EXAMPLE: A flyer image on page 4
    // {
    //   page: 4,
    //   x: 10,
    //   y: 20,
    //   width: 35,
    //   height: 40,
    //   caption: "Spring 2026 Event Schedule"
    // },
  ],

  // ----------------------------------------------------------
  //  TOOLTIPS / CAPTIONS
  //  Add hover/tap info bubbles anywhere on a page
  // ----------------------------------------------------------
  //  page:    which page number
  //  x, y:    position of the tooltip icon (percentage)
  //  text:    the tooltip message
  //  color:   icon color (optional, default: "#3498db")
  // ----------------------------------------------------------
  tooltips: [
    // EXAMPLE: Extra info on page 2
    // {
    //   page: 2,
    //   x: 75,
    //   y: 15,
    //   text: "Office hours: Mon-Fri 8am-5pm",
    //   color: "#e74c3c"
    // },
  ],

  // ----------------------------------------------------------
  //  TABLE OF CONTENTS
  //  Define named sections for the thumbnail navigation panel
  // ----------------------------------------------------------
  //  page:    which page number
  //  title:   section name shown in the panel
  // ----------------------------------------------------------
  tableOfContents: [
    // EXAMPLE:
    // { page: 1,  title: "Cover" },
    // { page: 2,  title: "Letter from the Editor" },
    // { page: 4,  title: "Campus Events" },
    // { page: 6,  title: "Student Spotlight" },
    // { page: 8,  title: "Resources" },
    // { page: 10, title: "Back Cover" },
  ],

};
