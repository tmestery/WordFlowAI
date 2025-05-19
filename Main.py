import nltk
import spacy
from collections import Counter

# Main class
def main():
    # Download the required NLTK resource + Add the spaCy model (2):
    #nltk.download('punkt')
    #nltk.download('punkt_tab')
    #nlp = spacy.load('en_core_web_sm')  

    # Read text into a string variable
    string_text = read_text_and_clean("BrownFox.txt")

    # Run the function to tokenize .txt file
    token_text = nltk.word_tokenize(string_text)

    # Start building the marcov model using tokenized text
    print("building model")
    build_markov_model(token_text)


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

    # for every unique word in the text, loop through the text and count all next words
    for unique_word in word_counts:
        next_word_dict = {}
        # loop through the text again, looking for this word
        for index in range(len(word_list)-1):
            if(word_list[index] == unique_word):
                next_word = word_list[index+1]
                # if this word does not exist in the dictionary, add it, otherwise update the count
                if next_word_dict.get(next_word) == None:
                    next_word_dict.update({next_word:1}) 
                else:
                    next_word_dict[next_word] += 1
        # add the dictionary for this word to the model
        markov_model.update({unique_word : next_word_dict})
    
    # print the results
    for dict in markov_model:
        print(f"The word '{dict}' is followed by: {markov_model[dict]}")


if __name__ == "__main__":
    main()