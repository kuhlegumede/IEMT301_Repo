

import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.amazon.com/s?k=laptop"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        titles = soup.select("h2 .a-text-normal")
        for idx, title in enumerate(titles[:10], 1):
            print(f"{idx}. {title.get_text(strip=True)}")
    else:
        print("Failed to fetch page:", response.status_code)

if __name__ == "__main__":
    main()
