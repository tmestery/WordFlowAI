import nltk
import random as rand

# Main class
def main():
    # Read text into a string variable
    string_text = read_text_and_clean("samples/MobyDickBook.txt") + read_text_and_clean("samples/modern_slang.txt")

    # Run the function to tokenize .txt file
    token_text = tokenize_text(string_text)

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

# Tokenize the text using nltk
def tokenize_text(text):
    return nltk.word_tokenize(text)

# Build a dictionary using marcov chains, that returns a nested dictionary
def build_markov_model(word_list):
    markov_model = {}

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
    # good fallback word list
    fallback_words = [
    "the", "of", "and", "a", "to", "in", "is", "that", "it", "for",
    "on", "you", "with", "as", "I", "was", "at", "be", "this", "have"
]

    # check if the word is in the model
    if model.get(current_word) == None:
        rand_fallback_word = rand.choice(fallback_words)
        return rand_fallback_word
        
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