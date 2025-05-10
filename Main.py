# importing necessary packages
import nltk
nltk.download('punkt_tab')
import spacy
from collections import Counter

# Main class
def main():
    # Download the required NLTK resource + oad the spaCy model
    nltk.download('punkt')
    nlp = spacy.load('en_core_web_sm')  

    # Read text into a string variable
    textString = read_text_into_string("MobyDickBook.txt")

    # Run the function to clean/tokenize .txt file
    clean_and_tokenize(textString)

# Get the sample text into string format
def read_text_into_string(file_path):
    with open(file_path, 'r') as file:
        file_content = ""
        line = file.readline()

        while line:
            file_content += line
            line = file.readline()

    return file_content

# Takes a text file, cleans it, tokenizes it, and saves cleaned word list for later use
def clean_and_tokenize(stringName):
    # Tokenize the text and create bigrams
    words = nltk.word_tokenize(stringName.lower())
    bigrams = zip(words, words[1:])
    counts = Counter(bigrams)

    print(counts)

    #return counts