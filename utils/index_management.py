from utils.opensearch_client import es
import streamlit as st


def create_index(index_name):
    if not es.indices.exists(index=index_name):
        body = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 1
            },
            "mappings": {
                "properties": {
                    "brand": {"type": "keyword"},
                    "size": {"type": "keyword"},
                    "price": {"type": "double"},
                    "stock_quantity": {"type": "integer"}
                }
            }
        }
        es.indices.create(index=index_name, body=body)
        st.success(f"Index '{index_name}' created successfully.")
    else:
        st.info(f"Index '{index_name}' already exists.")
