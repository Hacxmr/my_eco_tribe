import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("sustainable_fashion_trends_2024.csv")

# Preprocessing: Group data by Material_Type for analysis
material_analysis = data.groupby('Material_Type').agg({
    'Carbon_Footprint_MT': 'mean',
    'Water_Usage_Liters': 'mean',
    'Eco_Friendly_Manufacturing': lambda x: x.value_counts().get('Yes', 0),
    'Sustainability_Rating': lambda x: x.value_counts().idxmax()
}).reset_index()

# Rename columns for better understanding
material_analysis.rename(columns={
    'Carbon_Footprint_MT': 'Avg_Carbon_Footprint_MT',
    'Water_Usage_Liters': 'Avg_Water_Usage_Liters',
    'Eco_Friendly_Manufacturing': 'Eco_Friendly_Count',
    'Sustainability_Rating': 'Most_Common_Rating'
}, inplace=True)

# Sort data for better visualization
material_analysis = material_analysis.sort_values(by='Avg_Carbon_Footprint_MT')

# Create the Streamlit app
def create_dashboard():
    st.title("Sustainable Fabric Recommendations Dashboard")
    st.markdown("Compare fabrics based on sustainability metrics to make eco-conscious choices.")
    
    # Display Sustainability Ratings by Fabric
    st.header("Material Analysis")
    st.dataframe(material_analysis)

    # Visualization: Carbon Footprint vs Water Usage
    st.header("Environmental Impact: Carbon Footprint vs Water Usage")
    fig, ax = plt.subplots(figsize=(10, 6))
    for _, row in material_analysis.iterrows():
        ax.scatter(
            row['Avg_Carbon_Footprint_MT'], 
            row['Avg_Water_Usage_Liters'], 
            s=row['Eco_Friendly_Count'] * 10, 
            label=row['Material_Type']
        )
    ax.set_title("Fabric Environmental Impact")
    ax.set_xlabel("Average Carbon Footprint (MT)")
    ax.set_ylabel("Average Water Usage (Liters)")
    ax.legend(title="Material Type")
    st.pyplot(fig)

    # Recommendations
    st.header("Recommendations")
    low_impact_materials = material_analysis[
        (material_analysis['Avg_Carbon_Footprint_MT'] < material_analysis['Avg_Carbon_Footprint_MT'].median()) &
        (material_analysis['Avg_Water_Usage_Liters'] < material_analysis['Avg_Water_Usage_Liters'].median())
    ]
    st.markdown("### Best Materials to Use:")
    st.dataframe(low_impact_materials[['Material_Type', 'Avg_Carbon_Footprint_MT', 'Avg_Water_Usage_Liters', 'Most_Common_Rating']])

    st.markdown("### Key Insights:")
    st.write("1. **Eco-Friendliness**: Fabrics with the highest eco-friendly scores are recommended.")
    st.write("2. **Carbon and Water Efficiency**: Fabrics with low average carbon footprint and water usage are ideal.")
    st.write("3. **Sustainability Rating**: Consider fabrics with top sustainability ratings.")

create_dashboard()
