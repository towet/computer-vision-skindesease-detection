import streamlit as st
from PIL import Image
import torch
from classy import classification_model  # Import the classification model
import tempfile
import openai
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os


import streamlit as st
from PIL import Image
import torch
import tempfile
import os




# Load your custom YOLOv5 model
detection_model = None
try:
    detection_model = torch.hub.load('ultralytics/yolov5', 'custom', path='models/best.pt', force_reload=True)
    st.success('Model loaded successfully!')
except Exception as e:
    st.error(f'Failed to load the model: {e}')

# Title of the app
st.title("Skin Disease Detection")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Affected Area image.', use_column_width=True)
    st.write("")

    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_file_path = temp_file.name

    # Check if the model is loaded before proceeding
    if detection_model is not None:
        # Perform object detection
        st.write("Analyzing...")
        results = detection_model(temp_file_path)

        # Extract the disease name from the detection results
        predictions = results.pandas().xyxy[0]  # Get the DataFrame of detection results
        if not predictions.empty:
            # Assuming the disease name is the class with the highest confidence
            disease_name = predictions.loc[predictions['confidence'].idxmax(), 'name']
            st.write(f"This is a {disease_name}.")

            # Set up the prompt template for the LLM
            prompt_template = f"What is the cause and possible treatment for {disease_name}?"
            prompt = PromptTemplate(input_variables=["disease_name"], template=prompt_template)

            # Set up the LLM
            llm = OpenAI(temperature=0.9)
            llm_chain = LLMChain(prompt=prompt, llm=llm)

            # Generate the response
            response = llm_chain.run(disease_name=disease_name)
            st.write(f"Cause and possible treatment: {response}")
        else:
            st.write("No disease detected.")
    else:
        st.error("Model not loaded. Cannot perform detection.")

    # Clean up the temporary file
    temp_file.close()