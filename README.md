# T-Shirt Inventory Calculator

This is a Streamlit-based web application for managing a T-Shirt inventory using Elasticsearch. The app allows users to:
- Search inventory by brand and size.
- Calculate the total inventory price for specific T-Shirt sizes.

## Features

1. *Search Inventory:*
   - Search for T-Shirts based on brand and size.
   - View details such as brand, size, price, and stock quantity.

2. *Calculate Inventory Price:*
   - Calculate the total inventory price for a specific size by multiplying the price and stock quantity.

3. *Data Management:*
   - Index T-Shirt inventory data into Elasticsearch from a JSON file.
   - Automatically creates the index with proper mappings if it doesn't exist.

## Technology Stack

- *Frontend:* Streamlit
- *Backend:* Elasticsearch - OpenSearch
- *Language:* Python
- *Libraries:* 
  - opensearch-py for Elasticsearch interactions.
  - streamlit for the web interface.
  - dotenv for managing environment variables.

## Project Structure


.
├── app.py                # Main Streamlit application.
├── utils/                # Utility functions for Elasticsearch operations.
│   ├── opensearch_client.py  # Elasticsearch client initialization.
│   ├── data_loader.py        # Functions for loading and indexing data.
│   ├── search_utils.py       # Query and search functions.
├── data/                # Directory for data files.
│   ├── data.json           # Sample T-Shirt inventory data.
├── .env                 # Environment variables for Elasticsearch credentials.
├── requirements.txt     # Python dependencies.
└── README.md            # Project documentation.


## Installation

1. Clone the repository:
   bash
   git clone (https://github.com/adarshjadhav17/inventory_bot)
   cd tshirt-inventory
   

2. Install dependencies:
   bash
   pip install -r requirements.txt
   

3. Add a .env file with Elasticsearch credentials:
   env
   OPENSEARCH_URL=<your-elasticsearch-url>
   OPENSEARCH_USERNAME=<your-username>
   OPENSEARCH_PASSWORD=<your-password>
   

4. Run the app:
   bash
   streamlit run app.py


## Sample Data

The app uses a sample data file (data.json) for T-Shirt inventory. Replace this file with your data as needed.

## Contribution

Feel free to fork the repository and create a pull request if you want to contribute.
