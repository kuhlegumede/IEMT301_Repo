import requests
from bs4 import BeautifulSoup

# Amazon search URL
url = "https://www.amazon.com/s?k=laptop"

# Set headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Send the request
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Try multiple ways to get titles (Amazon uses different structures dynamically)
    titles = soup.select("h2 .a-text-normal")

    print("Laptop Listings Found:\n")
    for idx, title in enumerate(titles[:10], 1):  # Limit to 10 results
        print(f"{idx}. {title.get_text(strip=True)}")
else:
    print("Failed to fetch the page. Status code:", response.status_code)
