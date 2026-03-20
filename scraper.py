import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = []

    # NEW correct selector
    for item in soup.select(".titleline a"):
        titles.append(item.text.strip())

    df = pd.DataFrame({"Title": titles})
    df.to_csv("data.csv", index=False)

    print("Scraping done! Data saved.")

if __name__ == "__main__":
    scrape_data()