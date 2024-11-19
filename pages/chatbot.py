import streamlit as st
import requests
import os

# Set your OpenRouter API key and optional headers
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  # Replace with your OpenRouter API key
YOUR_SITE_URL = "https://yourwebsite.com"  # Optional: For rankings
YOUR_APP_NAME = "ClothRecommendationApp"  # Optional: App name for OpenRouter rankings

# Define the API endpoint and headers for OpenRouter (Meta Llama 3.2 3B Instruct)
url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "HTTP-Referer": YOUR_SITE_URL,
    "X-Title": YOUR_APP_NAME,
    "Content-Type": "application/json",
}

# Function to get clothing recommendations
def get_clothing_recommendations(user_input):
    payload = {
        "model": "meta-llama/llama-3.2-3b-instruct:free",  # Using the free Meta Llama 3.2 3B model
        "messages": [
            {"role": "system", "content": "You are a fashion assistant who suggests clothing and outfit pairings."},
            {"role": "user", "content": user_input},
        ],
        "temperature": 0.7,
        "max_tokens": 300,
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        completion = response.json()
        return completion["choices"][0]["message"]["content"]
    else:
        return "Error: Unable to fetch recommendations."

# Chatbot Interface
def chatbot_ui():
    st.set_page_config(page_title="Clothing Recommendation Chatbot", page_icon="👗")
    st.title("👗 Clothing Recommendation Chatbot")
    
    st.write("### Ask the chatbot for clothing suggestions!")
    
    # Session state to store query history
    if "queries" not in st.session_state:
        st.session_state.queries = []  # Initialize as an empty list

    # User input for the current query
    user_input = st.text_input("Enter your clothing preferences or question:", "")

    # Handle the query and response
    if user_input:
        with st.spinner("Fetching clothing recommendations..."):
            recommendations = get_clothing_recommendations(user_input)
            # Add the current query and response to the top of the history
            st.session_state.queries.insert(0, {"query": user_input, "response": recommendations})

    # Display "Clear Chat" button
    if st.button("Clear Chat"):
        st.session_state.queries = []  # Reset the history

    # Display query history
    st.write("### Chat History")
    if st.session_state.queries:
        for i, entry in enumerate(st.session_state.queries):
            st.write(f"**Query {len(st.session_state.queries) - i}:** {entry['query']}")
            st.write(f"**Recommendation:** {entry['response']}")
            st.markdown("---")  # Separator for clarity
    else:
        st.write("No chat history yet. Ask a question to get started!")

# Run chatbot page
chatbot_ui()
