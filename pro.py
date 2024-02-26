# import required libraries
from dotenv import load_dotenv 
load_dotenv()  # to load all the env variables

import streamlit as st
import os
import google.generativeai as genai

#-------------------------------------------#

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

# creating function to load gemini pro model

model = genai.GenerativeModel("gemini-pro") # gemini pro used for text data

def get_respone(query):
    response = model.generate_content(query)
    return response.text



# To set up streamlit

st.set_page_config(page_title="Q & A using Gemini")
st.header("Responsive AI")

input = st.text_input("Input", key="input")
submit = st.button("submit")


## when submit button is clicked,

if submit:
    response = get_respone(input)
    st.subheader("The Generated Content:")
    st.write(response)

