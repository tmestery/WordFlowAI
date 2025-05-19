import nltk
import spacy
from collections import Counter
import random as rand

# Main class
def main():
    # Download the required NLTK resource + Add the spaCy model (2):
    #nltk.download('punkt')
    #nltk.download('punkt_tab')
    #nlp = spacy.load('en_core_web_sm')  

    # Read text into a string variable
    string_text = read_text_and_clean("samples/MobyDickBook.txt")

    # Run the function to tokenize .txt file
    token_text = nltk.word_tokenize(string_text)

    # Start building the marcov model using tokenized text
    print("Building model...")
    markov_model = build_markov_model(token_text)
    print("Success!\n")

    # Listen for input from the user
    input_word = input("Input a word: ").lower()
    input_length = int(input("How many words to generate: "))
    print(generate_text(markov_model,input_word,input_length))


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


# Build a dictionary using marcov chains, that returns a nested dictionary
def build_markov_model(word_list):
    markov_model = {}
    word_counts = Counter(word_list)

    # loop through the words and count instances of next words
    for index in range(len(word_list)-1):
        word = word_list[index]
        next_word = word_list[index+1]
        # check if this word has been included in the model
        if markov_model.get(word) == None:
            markov_model.update({word:{}})
        # check if the next word has been included in word's model
        if markov_model[word].get(next_word) == None:
            markov_model[word].update({next_word:1})
        else:
            markov_model[word][next_word] += 1

    return markov_model


# given a word, generate a next word using the markov model
def next_word(model, current_word):
    # check if the word is in the model
    if model.get(current_word) == None:
        return "X"
    # the word is in the model, sample a random word
    dict = model[current_word]
    population = list(dict.keys())
    probabilities = list(dict.values())
    next = str(rand.choices(population,probabilities)[0])

    return next


# given a word, generate several words using the markov model and next_word()
def generate_text(model, first_word, length: int):
    s = ""
    prev_word = first_word
    for i in range(length):
        prev_word = next_word(model,prev_word)
        s = s + prev_word + " "
    return s


if __name__ == "__main__":
    main()
