import google.generativeai as genai
import streamlit as st
import os
genai.configure(api_key=st.secrets('api_key'))
# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)
def gen_ai(input_val):
    
    response = chat_session.send_message(f'{input_val}  This question is Related To Trading')
    return (response.text)
