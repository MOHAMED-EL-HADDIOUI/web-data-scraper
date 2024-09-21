import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

# Function to scrape all data from the given URL, including images and other elements
def scrape_all_data_with_images(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all visible and non-visible text
        all_text = soup.get_text()

        # Extract headers, images, and links
        headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        images = soup.find_all('img')
        links = soup.find_all('a')

        # Collect headers
        headers_text = "\n".join([header.get_text().strip() for header in headers])

        # Collect image data (desanonymization step) and insert <img> tags into the text
        images_data = "\n"
        for img in images:
            img_alt = img.get('alt', 'No Alt')
            img_src = img.get('src', '#')
            img_tag = f"<img alt='{img_alt}' src='{img_src}'/>"
            images_data += f"Image found: {img_tag}\n\n"

        # Collect links and hrefs
        links_data = "\n".join([f"Link text: {link.get_text().strip()} | URL: {link.get('href')}" for link in links])

        # Remove multiple whitespaces and newlines
        all_text_clean = re.sub(r'\s+', ' ', all_text)

        # Combine all the data
        scraped_data = f"Headers:\n\n{headers_text}\n\nImages:\n\n{images_data}\n\nLinks:\n{links_data}\n\nFull Text:\n\n{all_text_clean}"

        return scraped_data
    except Exception as e:
        st.error(f"Error occurred while scraping the data: {e}")
        return None

# Streamlit UI
def main():
    st.title("Web Data Scraper with Images and Links")

    # Get the URL from the user
    url_input = st.text_input("Enter the URL of the web page:", "")

    if st.button("Scrape All Data"):
        if url_input:
            # Extract all data including images and links
            data = scrape_all_data_with_images(url_input)
            if data:
                st.success("All data successfully scraped!")
                st.subheader("Scraped Data:")
                st.write(data, unsafe_allow_html=True)  # Allow HTML to display image tags
            else:
                st.warning("Failed to scrape data from the URL.")
        else:
            st.warning("Please enter a valid URL.")

if __name__ == "__main__":
    main()
