import requests
import streamlit as st

def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke", json = {'input':{'topic':input_text}})

    data = response.json()

    # If response is a raw string 
    if isinstance(data, str):
        return data
    
    # If response is {"output":"....."}
    if isinstance(data.get("output"), str):
        return data["output"]
    
st.title("Langchain Demo with Langserve API")
input_text = st.text_input("Write an essay on .....")

if input_text:
    st.write(get_ollama_response(input_text=input_text))