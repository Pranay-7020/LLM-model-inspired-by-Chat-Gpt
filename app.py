import streamlit as st
from langchain_ollama import OllamaLLM

# Initialize Ollama model
llm = OllamaLLM(model="gemma2:latest")

st.title("LangChain + Ollama Demo")

user_input = st.text_input("Enter your prompt:")

if user_input:
    response = llm.invoke(user_input)
    st.write("### Response:")
    st.write(response)
