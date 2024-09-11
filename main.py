import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find('title').get_text()
    return f"Website Title: {title}"

if __name__ == "__main__":
    url = "https://example.com"
    print(scrape_website(url))