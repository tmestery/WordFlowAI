# Usual imports along with downloading punkt again...
import streamlit as st
from Main import read_text_and_clean, build_markov_model, generate_text
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')  # Added to fix punkt_tab error

# Read and process text
string_text = read_text_and_clean("samples/MobyDickBook.txt")
token_text = nltk.word_tokenize(string_text)
model = build_markov_model(token_text)

# Creates title, and two different places for user input in the UI
st.title("Markov Chain Text Generator")
input_word = st.text_input("Enter a starting word:")
input_length = st.number_input("How many words to generate?", min_value=1, step=1)

# Generation button
if st.button("Generate"):
    output = generate_text(model, input_word.lower(), int(input_length))
    st.write(output)