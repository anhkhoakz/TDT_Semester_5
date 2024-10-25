import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Ensure the base images directory exists
base_dir = "images"
os.makedirs(base_dir, exist_ok=True)

visited_urls = set()


def sanitize_path(path):
    return path.replace("/", "_").replace(":", "_")


def crawl(url):
    if url in visited_urls:
        return
    visited_urls.add(url)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.find_all("img")

    # Create a directory for the current page
    parsed_url = urlparse(url)
    page_dir = os.path.join(base_dir, sanitize_path(parsed_url.path))
    os.makedirs(page_dir, exist_ok=True)

    for image in images:
        if "src" in image.attrs:
            image_url = urljoin(url, image["src"])
            image_name = os.path.basename(urlparse(image_url).path)
            try:
                image_response = requests.get(image_url)
                image_response.raise_for_status()
                with open(os.path.join(page_dir, image_name), "wb") as f:
                    f.write(image_response.content)
            except requests.RequestException as e:
                print(f"Failed to download image {image_url}: {e}")

    links = soup.find_all("a", href=True)
    for link in links:
        link_url = urljoin(url, link["href"])
        if urlparse(link_url).netloc == urlparse(url).netloc:
            crawl(link_url)


start_url = "https://cellphones.com.vn/"
crawl(start_url)
