import nltk
import spacy
from collections import Counter
nltk.download('punkt')
nlp = spacy.load('en_core_web_sm')

text = "This is a test. This test is simple."
words = nltk.word_tokenize(text.lower())
bigrams = zip(words, words[1:])
counts = Counter(bigrams)
print(counts)