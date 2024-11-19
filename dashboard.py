import streamlit as st
import requests
import os

# Set your OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Define API endpoint and headers for OpenRouter
url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
}

# Function to fetch sustainable fashion recommendations
def get_fashion_recommendations(user_input):
    payload = {
        "model": "meta-llama/llama-3.2-3b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are an assistant specializing in sustainable fashion recommendations."},
            {"role": "user", "content": user_input},
        ],
        "temperature": 0.4,
        "max_tokens": 500,
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        completion = response.json()
        return completion["choices"][0]["message"]["content"]
    else:
        return "Error: Unable to fetch recommendations."

# Dashboard Interface
def sustainable_fashion_dashboard():
    st.set_page_config(
        page_title="Sustainable Fashion Dashboard",
        page_icon="🌿",
        layout="wide",
    )

    # Title and Description
    st.title("🌿 Revive the Vibe:Sustainable Fashion Recommendation Dashboard")
    st.markdown(
        """
        Welcome to the Sustainable Fashion Dashboard! 🌱  
        Here, you can explore eco-friendly outfit ideas, learn about sustainable fashion trends, 
        and discover brands committed to sustainability.
        """
    )

    # Sidebar for navigation
    with st.sidebar:
        st.header("Navigation")
        section = st.radio(
            "Choose a section:",
            ("Recommendations", "Trends & Tips", "Sustainable Brands", "Impact Calculator"),
        )

    # Recommendations Section
    if section == "Recommendations":
        st.subheader("👗 Get Personalized Recommendations")
        st.write("Enter your preferences or occasion to get sustainable outfit suggestions.")
        user_input = st.text_input("Your Preferences:", "")

        if user_input:
            with st.spinner("Fetching recommendations..."):
                recommendations = get_fashion_recommendations(user_input)
                st.success("Here are your sustainable outfit suggestions:")
                st.write(recommendations)

    # Trends & Tips Section
    elif section == "Trends & Tips":
        st.subheader("🌟 Sustainable Fashion Trends & Tips")
        st.markdown(
            """
            - **Opt for timeless pieces:** Invest in high-quality, versatile items that never go out of style.  
            - **Choose sustainable fabrics:** Look for organic cotton, linen, hemp, or recycled materials.  
            - **Support ethical brands:** Prefer brands with transparent supply chains and fair labor practices.  
            - **Care for your clothes:** Extend the life of your wardrobe by washing less, repairing, and upcycling.
            """
        )
        # st.image(
        #     "https://images.unsplash.com/photo-1618354699826-d965d6c4e09b",
        #     caption="Sustainable Fashion Inspiration",
        #     use_column_width=True,
        # )

    # Sustainable Brands Section
    elif section == "Sustainable Brands":
        st.subheader("🌍 Discover Sustainable Brands")
        st.write(
            """
            Here are some well-known brands that focus on sustainability:
            - **Patagonia**: Environmentally responsible outdoor clothing.
            - **Reformation**: Stylish clothing with a focus on eco-friendliness.
            - **Everlane**: Transparent pricing and sustainable materials.
            - **Allbirds**: Eco-friendly footwear using natural materials.
            - **Eileen Fisher**: Timeless, minimalist clothing with ethical practices.
            """
        )
        # st.image(
        #     "https://images.unsplash.com/photo-1512757776218-8c7babd9f9d0",
        #     caption="Support Sustainable Fashion Brands",
        #     use_column_width=True,
        # )

    # Impact Calculator Section
    elif section == "Impact Calculator":
        st.subheader("🌏 Calculate Your Fashion Impact")
        st.write(
            """
            Estimate your fashion choices' environmental impact by entering details about your wardrobe.
            """
        )
        # User inputs for impact calculation
        num_items = st.number_input("How many clothing items do you buy annually?", min_value=0, value=10)
        percent_sustainable = st.slider("What percentage of your purchases are sustainable?", 0, 100, 50)

        # Calculate impact
        total_impact = num_items * (1 - percent_sustainable / 100) * 10  # Example formula
        st.write(f"Your estimated annual carbon footprint: **{total_impact} kg CO₂**")
        st.info("Switching to sustainable choices can significantly reduce your footprint!")

    # Footer
    st.markdown("---")
    st.markdown(
        "🔗 [Learn More About Sustainable Fashion](https://www.sustainablefashion.com/) | 🛒 [Shop Sustainably](https://goodonyou.eco/)"
    )

# Run the dashboard
if __name__ == "__main__":
    sustainable_fashion_dashboard()
