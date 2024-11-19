# Eco-Friendly Fabric Recommendation System

The **Eco-Friendly Fabric Recommendation System** helps users discover sustainable and eco-friendly fabric alternatives. By selecting a fabric, the system suggests similar options using advanced similarity search algorithms powered by FAISS (Facebook AI Similarity Search) and TF-IDF. The application features an interactive UI built with Streamlit.

This project is part of the [Eco-Friendly Tribe](https://github.com/Hacxmr/my_eco_tribe) initiative, which aims to promote sustainable fabric choices.

![Eco-Friendly Fabric Recommendation System](https://github.com/Hacxmr/my_eco_tribe/blob/main/fabric_recommendation.jpg)

---

## Features

- **Interactive Fabric Selection**: Users can select a fabric to find similar eco-friendly alternatives.
- **Text Vectorization**: Leverages TF-IDF to analyze fabric titles and descriptions.
- **Categorical Encoding**: Encodes categorical labels using one-hot encoding for enhanced similarity search.
- **FAISS Integration**: Employs FAISS for fast and accurate similarity search.
- **Streamlit Frontend**: Provides a simple and user-friendly interface.

---

## Dataset

The system uses the [FabricFrontiers](https://huggingface.co/datasets/infinite-dataset-hub/FabricFrontiers) dataset. This dataset contains the following fields:

- `idx`: Unique identifier for each fabric.
- `title`: Name of the fabric.
- `description`: Description of the fabric, including eco-friendly attributes.
- `source`: Source or origin of the fabric.
- `label`: Categorical label representing the fabric's type or category.

Download the dataset [here](https://huggingface.co/datasets/infinite-dataset-hub/FabricFrontiers).

---

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Hacxmr/my_eco_tribe.git
    cd my_eco_tribe
    ```

2. **Install Dependencies**:
    Ensure you have Python 3.8+ installed. Then, install the required packages:
    ```bash
    pip install streamlit pandas faiss-cpu scikit-learn numpy
    ```

3. **Download the Dataset**:
    Place the `fabric_frontiers.csv` file in the root directory of the project, or update the dataset URL in the code if needed.

---

## Usage

1. **Run the Streamlit Application**:
    ```bash
    streamlit run streamlit_app.py
    ```

2. **Interact with the Application**:
    - Select a fabric from the dropdown menu.
    - Click the "Recommend" button to view similar fabric suggestions.

---

## How It Works

1. **Data Preprocessing**:
    - Combines `title` and `description` fields for text analysis.
    - Transforms text data into numerical vectors using TF-IDF.
    - Encodes categorical labels using one-hot encoding.

2. **Similarity Search**:
    - Creates a FAISS index for efficient similarity search.
    - Searches for fabrics most similar to the selected fabric based on vectorized features.

3. **Interactive Recommendations**:
    - Displays the top 5 fabric recommendations along with their descriptions and sources.

---

## Example Output

**Selected Fabric**: Organic Cotton

**Recommended Fabrics**:
1. Hemp Fabric (Source: Sustainable Textiles)  
   - *Description*: Durable and eco-friendly fabric made from hemp fibers.
2. Recycled Polyester (Source: EcoThreads)  
   - *Description*: Sustainable polyester made from recycled plastic bottles.
3. Bamboo Rayon (Source: Nature's Fabrics)  
   - *Description*: Soft and eco-conscious fabric derived from bamboo pulp.

---

## Contributions

Contributions are welcome! If you want to contribute:
1. Fork the repository.
2. Make your changes.
3. Submit a pull request.


---

## Contact

For any queries or suggestions, feel free to reach out:

- **GitHub**: [@Hacxmr](https://github.com/Hacxmr)
- **Email**: [rajmitali1111@gmail.com](rajmitali1111@gmail.com)
