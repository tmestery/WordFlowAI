# ./venv/bin/python3

# Simple Test Code to Ensure Everything is Installed Correctly...
import nltk
nltk.download('punkt_tab')
import spacy
from collections import Counter

# Download the required NLTK resource
nltk.download('punkt')

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Sample text
text = "This is a test. This test is simple."

# Tokenize the text and create bigrams
words = nltk.word_tokenize(text.lower())
bigrams = zip(words, words[1:])
counts = Counter(bigrams)

# Output the bigram counts
print(counts)