# Web Data Scraper with Images and Links

## Overview

This project is a **web scraper** built using **Streamlit**, **BeautifulSoup**, and **Requests**. It extracts all the visible and non-visible text from a web page, along with additional data such as headers, links, and images. The scraper also inserts the found images directly into the text using HTML `<img>` tags, and displays them in the Streamlit app.

The application is user-friendly and can be easily deployed as a web-based tool to scrape information from websites by simply entering a URL.

## Features

- Scrapes **all text** content from a web page, including non-visible elements like headers and footers.
- **Extracts images** and integrates them into the scraped text using HTML `<img>` tags.
- Retrieves **hyperlinks** (`<a>` tags) with both their text and URLs.
- Provides a clean and simple **Streamlit interface** to input the URL and display results.
- Displays the scraped data, including images, directly in the app.

## Technologies Used

- **Streamlit** - For creating the interactive user interface.
- **BeautifulSoup** - For parsing and scraping the HTML content from web pages.
- **Requests** - For sending HTTP requests to fetch web page content.
- **Re (Regular Expressions)** - For cleaning the scraped text content.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MOHAMED-EL-HADDIOUI/web-data-scraper.git
   cd web-data-scraper
