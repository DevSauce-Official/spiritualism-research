import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape a webpage
def scrape_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# Example URL (change this to a relevant website)
url = 'https://example.com/spiritualism-articles'
soup = scrape_webpage(url)

# Extract article information (assuming articles are within <article> tags)
articles = []
for article in soup.find_all('article'):
    title = article.find('h2').text
    link = article.find('a')['href']
    summary = article.find('p').text
    articles.append({'Title': title, 'Link': link, 'Summary': summary})

# Convert to DataFrame and save as CSV
df = pd.DataFrame(articles)
df.to_csv('data/spiritualism_articles.csv', index=False)

print(df.head())
