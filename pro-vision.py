# import required libraries
from dotenv import load_dotenv 
load_dotenv()  # to load all the env variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

#-------------------------------------------#

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

# creating function to load gemini pro model

model = genai.GenerativeModel("gemini-pro-vision") # model optimized for images
model1 = genai.GenerativeModel("gemini-pro")   # model optimized for text data

def get_response(input,image):

    if input != '':
        if image is not None:
            response = model.generate_content([input, image])
            return response.text
        else:
            response = model1.generate_content(input)
            return response.text
    else:
        if image is not None:
            response = model.generate_content(image)
            return response.text
        else:
            response = "Please provide either an input prompt or upload an image."
            return response.text

    

# To set up streamlit

st.set_page_config(page_title="Content Generation model using Gemini")
st.header("LLM MODEL")

input = st.text_input("Input Prompt", key="input")


uploaded_file = st.file_uploader("Input Image", type=["jpg", "jpeg", "png"])

image=""  

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
else:
    image = None
    


submit = st.button("submit")


## when submit button is clicked,

if submit:
    response = get_response(input,image)
    st.subheader("The Generated Content:")
    st.write(response)
