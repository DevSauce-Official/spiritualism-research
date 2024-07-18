import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

# Load text
with open('data/the_spirits_book.txt', 'r') as file:
    text = file.read()

# Tokenize text
tokens = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words and word.isalpha()]

# Frequency distribution
fdist = FreqDist(filtered_tokens)

# Plot most common words
plt.figure(figsize=(12, 8))
fdist.plot(30, cumulative=False)
plt.show()

# Print most common words
print(fdist.most_common(30))
