import nltk
import spacy
from collections import Counter

# Main class
def main():
    # Download the required NLTK resource + Add the spaCy model (2):
    #nltk.download('punkt')
    #nlp = spacy.load('en_core_web_sm')  

    # Read text into a string variable
    stringText = read_text_and_clean("MobyDickBook.txt")

    # Run the function to tokenize .txt file
    tokenText = tokenize_the_string(stringText)

    # Start building the marcov model using tokenized text
    build_markov_model(tokenText)

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
    filteredText = "".join(c for c in cleanedText if c not in ',.?;""-™()•:!')

    return filteredText

# Takes a string and tokenizes it using nltk
def tokenize_the_string(stringName):
    # Tokenize the text and create bigrams
    words = nltk.word_tokenize(stringName)
    bigrams = zip(words, words[1:])
    counts = Counter(bigrams)

    return counts

# Build a dictionary using marcov chains, that returns a nested dictionary
def build_markov_model(word_list):
    pass

if __name__ == "__main__":
    main()