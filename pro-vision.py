# import required libraries
from dotenv import load_dotenv 
load_dotenv()  # to load all the env variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import time

#-------------------------------------------#

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

# creating function to load gemini pro model

model = genai.GenerativeModel("gemini-pro-vision")
model1 = genai.GenerativeModel("gemini-pro")

def get_response(input,image):

    start_time = time.time()
    
    if input != '' and image is not None:
        response = model.generate_content([input,image])
        
    elif image == None:
        response = model1.generate_content(input)
        
    else:
        response = model.generate_content(image)
        #response =  response.parts
        #for part in response:
            #return (part.text)
    end_time = time.time()
    response_time = end_time - start_time
    
    return response.text,response_time
   

    
# To set up streamlit

st.set_page_config(page_title="Content Generation LLM Model using Gemini")
st.header("Content Generation LLM Model ")

input = st.text_input("Input Prompt", key="input")


uploaded_file = st.file_uploader("Input Image", type=["jpg", "jpeg", "png"])
image=None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Generate")


## when submit button is clicked,

if submit:
    response_text,response_time = get_response(input,image)
    
    st.subheader("The Generated Content:")
    st.write(response_text)
    st.write("Response Time :" ,response_time)
