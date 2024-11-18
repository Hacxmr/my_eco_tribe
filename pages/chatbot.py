import streamlit as st
import requests

# Set your OpenRouter API key and optional headers
OPENROUTER_API_KEY = "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"  # Replace with your OpenRouter API key
YOUR_SITE_URL = "https://yourwebsite.com"       # Optional: For rankings
YOUR_APP_NAME = "ClothRecommendationApp"        # Optional: App name for OpenRouter rankings

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
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7,
        "max_tokens": 200,
    }

    # Make the API request to OpenRouter
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        completion = response.json()
        return completion["choices"][0]["message"]["content"]
    else:
        return "Error: Unable to fetch recommendations."

# Chatbot Interface
def chatbot_ui():
    st.title("Clothing Recommendation Chatbot")
    
    st.write("### Ask the chatbot for clothing suggestions!")
    
    user_input = st.text_input("Enter your clothing preferences or question:", "")
    
    if user_input:
        with st.spinner("Fetching clothing recommendations..."):
            recommendations = get_clothing_recommendations(user_input)
            st.write(f"**Recommendation for your query**: {recommendations}")

# Run chatbot page
chatbot_ui()
