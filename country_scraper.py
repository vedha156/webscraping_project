"""1import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)
print(response.text[:800])  # show first 800 characters

"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

all_data = []

# Scraping multiple pages
# pages 1 to 5 exist for hockey teams section
for page in range(1, 6):
    print(f"Scraping page {page}...")
    url = f"https://www.scrapethissite.com/pages/simple/?page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    countries = soup.find_all("div", class_="country")

    for country in countries:
        name = country.find("h3", class_="country-name").text.strip()
        capital = country.find("span", class_="country-capital").text.strip()
        population = country.find("span", class_="country-population").text.strip()

        all_data.append({
            "Country": name,
            "Capital": capital,
            "Population": population
        })

# Create a DataFrame using Pandas
df = pd.DataFrame(all_data)

# Save to CSV file
df.to_csv("countries_data.csv", index=False)

print("\nScraping Completed!")
print("CSV File Saved as: countries_data.csv")
print(df.head())
