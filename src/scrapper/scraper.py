# Scraping module
from bs4 import BeautifulSoup
import requests


# Standard headers to fetch a website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def fetch_website_contents(url, verified_certificate=None):
    """
    Return the title and contents of the website at the given url;
    truncate to 2,000 characters as a sensible limit
    """
    response = requests.get(url, headers=headers, verify= verified_certificate)
    soup = BeautifulSoup(response.content, "html.parser")
    # Fetch title
    title = soup.title.string if soup.title else "No title found"
    # Fetch body text, removing script, style, img and input tags as they are unlikely to be useful for an LLM and can add a lot of noise
    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            # Decompose the tag to remove it from the soup
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    return (title + "\n\n" + text)[:2_000]
