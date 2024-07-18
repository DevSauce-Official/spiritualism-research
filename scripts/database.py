import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('data/spiritualism_research.db')
c = conn.cursor()

# Create a table for articles
c.execute('''CREATE TABLE IF NOT EXISTS articles
             (id INTEGER PRIMARY KEY, title TEXT, link TEXT, summary TEXT)''')

# Function to insert articles
def insert_article(title, link, summary):
    c.execute("INSERT INTO articles (title, link, summary) VALUES (?, ?, ?)", (title, link, summary))
    conn.commit()

# Example data (this would come from your web scraping script)
articles = [
    {'title': 'Spiritualism and Mediumship', 'link': 'https://example.com/article1', 'summary': 'An in-depth look at spiritualism.'},
    {'title': 'Allan Kardec\'s Theories', 'link': 'https://example.com/article2', 'summary': 'Exploring Kardec\'s contributions to mediumship.'}
]

# Insert example data
for article in articles:
    insert_article(article['title'], article['link'], article['summary'])

# Query the database
c.execute("SELECT * FROM articles")
rows = c.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
