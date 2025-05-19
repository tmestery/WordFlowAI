# Usual imports along with downloading punkt again...
import streamlit as st
from Main import read_text_and_clean, build_markov_model, generate_text, tokenize_text

# Keep this, it's needed to run in streamlit:
# "Please use the NLTK Downloader to obtain the resource:"
import nltk
nltk.download('punkt_tab')

# Adding logo (thanks, for now, grok)
main_logo = "logo.jpg"
st.logo(main_logo)

# Read and process text
string_text = read_text_and_clean("samples/MobyDickBook.txt")
token_text = tokenize_text(string_text)
model = build_markov_model(token_text)

# Creates title, and two different places for user input in the UI
st.title("Markov Chain Text Generator")
input_word = st.text_input("Enter a starting word:")
input_length = st.number_input("How many words to generate?", min_value=1, step=1)

# Generation button
if st.button("Generate"):
    output = generate_text(model, input_word.lower(), int(input_length))
    st.write(output)

# Feedback button
star_map = ["1", "2", "3", "4", "5"]
selected_star = st.feedback("stars")
if selected_star is not None:
    st.markdown(f"You selected {star_map[selected_star]} star(s)!")