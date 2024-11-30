# T-Shirt Inventory Calculator

The T-Shirt Inventory Calculator is a web-based application built using Python, Elasticsearch, and Streamlit. It allows users to search for inventory items and calculate the total inventory price for specific sizes in a t-shirt inventory database.

## Features
- Search for t-shirt inventory by brand and size.
- Calculate the total inventory price for t-shirts of a specific size.
- Uses Elasticsearch for indexing and querying inventory data.
- Built with Streamlit for a user-friendly dashboard interface.

## Technologies Used
- **Python**: Backend scripting.
- **Elasticsearch**: Indexing and querying inventory data.
- **Streamlit**: Frontend dashboard development.
- **dotenv**: For managing environment variables.
- **JSON**: For storing and loading inventory data.

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/adarshjadhav17/inventory_bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your Elasticsearch credentials:
   ```
   OPENSEARCH_URL="https://your-opensearch-endpoint"
   OPENSEARCH_USERNAME="your-username"
   OPENSEARCH_PASSWORD="your-password"
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## How to Use

### 1. Search Inventory
- Enter the brand name in the text input field.
- Select the desired t-shirt size from the dropdown menu.
- Click the **Search** button to view matching inventory items.

### 2. Calculate Inventory Price
- Select the desired t-shirt size from the dropdown menu.
- Click the **Calculate** button to view the total inventory price for the selected size.

## Code Explanation
- **create_index**: Creates the Elasticsearch index with predefined settings and mappings.
- **load_data**: Loads inventory data from a JSON file into the Elasticsearch index.
- **search_data**: Searches the inventory for specific criteria using Elasticsearch queries.
- **get_total_inventory_price**: Calculates the total inventory price for a specific size using Elasticsearch aggregations.
- **Streamlit Dashboard**: Provides an interactive interface for users to query and analyze inventory data.

## Data Format
The JSON data for loading inventory should be structured as follows:
```json
[
    {
        "brand": "BrandA",
        "size": "M",
        "price": 20.0,
        "stock_quantity": 100
    },
    {
        "brand": "BrandB",
        "size": "L",
        "price": 25.0,
        "stock_quantity": 50
    }
]
```

## Acknowledgements
This project uses:
- [OpenSearch](https://opensearch.org/) for indexing and searching data.
- [Streamlit](https://streamlit.io/) for building the dashboard interface.
- [dotenv](https://pypi.org/project/python-dotenv/) for environment variable management.
