import streamlit as st
import pandas as pd
import plotly.express as px

# Load datasets for sustainable fashion
fabric_url = "https://huggingface.co/datasets/infinite-dataset-hub/FabricFrontiers/resolve/main/data.csv"
fabric_df = pd.read_csv(fabric_url)
fashion_df = pd.DataFrame({  # Replace this with your actual dataset
    "Country": ["USA", "India", "France"],
    "Year": [2023, 2024, 2023],
    "Sustainability_Rating": ["High", "Medium", "High"],
})

# Sidebar Navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Choose a page:", ["Dashboard", "Chatbot"])

if selection == "Dashboard":
    # Main Dashboard for Sustainable Fashion Trends
    st.title("🌿 Sustainable Fashion & Fabric Recommendation Dashboard")
    st.write("Explore sustainable fabrics and fashion trends while getting recommendations based on your selections!")

    # Sidebar Filters for Sustainable Fashion Trends
    st.sidebar.header("Fashion Trends Filter")
    selected_country = st.sidebar.selectbox(
        "Select a Country",
        options=sorted(fashion_df['Country'].unique()),
        index=0  # Default: first country
    )
    year_range = st.sidebar.slider(
        "Select Year Range",
        min_value=int(fashion_df['Year'].min()),
        max_value=int(fashion_df['Year'].max()),
        value=(int(fashion_df['Year'].min()), int(fashion_df['Year'].max()))
    )

    # Filter Fashion Trends Data
    filtered_fashion_df = fashion_df[
        (fashion_df['Country'] == selected_country) &
        (fashion_df['Year'] >= year_range[0]) &
        (fashion_df['Year'] <= year_range[1])
    ]

    st.markdown(f"### Fashion Trends in {selected_country} ({year_range[0]} - {year_range[1]})")
    st.dataframe(filtered_fashion_df)

    # Visualizations for Fashion Trends
    st.markdown("### Sustainability Ratings Distribution")
    pie_chart = px.pie(
        filtered_fashion_df,
        names="Sustainability_Rating",
        title="Sustainability Ratings",
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    st.plotly_chart(pie_chart, use_container_width=True)

    # Download filtered fashion data
    st.markdown("### Download Filtered Fashion Data")
    csv = filtered_fashion_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="filtered_fashion_trends.csv",
        mime="text/csv"
    )

elif selection == "Chatbot":
    # Import chatbot code directly here
    st.title("🧵 Clothing Recommendation Chatbot")
    st.write("Ask for outfit ideas, fabric recommendations, or anything about sustainable fashion!")

    user_input = st.text_input("Enter your question or preferences:", "")
    if user_input:
        with st.spinner("Fetching recommendation..."):
            # Replace with your chatbot logic
            chatbot_response = f"Recommendation for '{user_input}': Try eco-friendly fabrics like organic cotton or bamboo!"
            st.write(f"**Chatbot Response:** {chatbot_response}")
