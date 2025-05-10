import nltk
nltk.download('punkt_tab')
import spacy
from collections import Counter

# Main class
def main():
    # Download the required NLTK resource + Add the spaCy model
    nltk.download('punkt')
    nlp = spacy.load('en_core_web_sm')  

    # Read text into a string variable
    textString = read_text_and_clean("MobyDickBook.txt")

    # Run the function to clean/tokenize .txt file
    tokenize_the_string(textString)

# Get the sample text into string format
def read_text_and_clean(file_path):
    with open(file_path, 'r') as file:
        file_content = ""
        line = file.readline()

        while line:
            file_content += line
            line = file.readline()

    # Make it all lowercase text
    cleanedText = file_content.lower()

    # Remove all punctuation from text
    for punctuation in ',.?;"-':
        cleanedText = text.replace(punctuation, "")

    return cleanedText

# Takes a text file, cleans it, tokenizes it, and saves cleaned word list for later use
def tokenize_the_string(stringName):
    # Tokenize the text and create bigrams
    words = nltk.word_tokenize(stringName.lower())
    bigrams = zip(words, words[1:])
    counts = Counter(bigrams)

    # print(counts)

    # return counts