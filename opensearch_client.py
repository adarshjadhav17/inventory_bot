import os
from dotenv import load_dotenv
from opensearchpy import OpenSearch
import streamlit as st


load_dotenv()

OPENSEARCH_URL = os.getenv("OPENSEARCH_URL")
OPENSEARCH_USERNAME = os.getenv("OPENSEARCH_USERNAME")
OPENSEARCH_PASSWORD = os.getenv("OPENSEARCH_PASSWORD")

def get_opensearch_client():
    try:
        client = OpenSearch(
            OPENSEARCH_URL,
            http_auth=(OPENSEARCH_USERNAME, OPENSEARCH_PASSWORD),
            scheme="https",
            port=443
        )
        if not client.ping():
            raise ConnectionError("Could not connect to OpenSearch.")
        return client
    except Exception as e:
        st.error(f"Error connecting to OpenSearch: {e}")
        st.stop()

es = get_opensearch_client()
