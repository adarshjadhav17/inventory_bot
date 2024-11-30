import json
from opensearchpy import helpers
from utils.opensearch_client import es
import streamlit as st
def load_data(index_name, json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            actions = [
                {
                    "_index": index_name,
                    "_source": record
                } for record in data
            ]
            helpers.bulk(es, actions)
            st.success(f"Data from '{json_file}' loaded into OpenSearch index: {index_name}")
    except FileNotFoundError:
        st.error(f"File '{json_file}' not found. Please ensure it exists.")
    except Exception as e:
        st.error(f"Error loading data: {e}")


def search_data(index_name, query):
    try:
        response = es.search(index=index_name, body=query)
        return response['hits']['hits']
    except Exception as e:
        st.error(f"Error querying data: {e}")
        return []


def get_total_inventory_price(index_name, size):
    query = {
        "query": {
            "bool": {
                "filter": [
                    {"term": {"size": size}}
                ]
            }
        },
        "aggs": {
            "total_price": {
                "sum": {
                    "script": {
                        "source": "doc['price'].value * doc['stock_quantity'].value"
                    }
                }
            }
        },
        "size": 0
    }
    try:
        result = es.search(index=index_name, body=query)
        return result['aggregations']['total_price']['value']
    except Exception as e:
        st.error(f"Error calculating total inventory price: {e}")
        return None
import json
from opensearchpy import helpers
from utils.opensearch_client import es
import streamlit as st


def load_data(index_name, json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            actions = [
                {
                    "_index": index_name,
                    "_source": record
                } for record in data
            ]
            helpers.bulk(es, actions)
            st.success(f"Data from '{json_file}' loaded into OpenSearch index: {index_name}")
    except FileNotFoundError:
        st.error(f"File '{json_file}' not found. Please ensure it exists.")
    except Exception as e:
        st.error(f"Error loading data: {e}")


def search_data(index_name, query):
    try:
        response = es.search(index=index_name, body=query)
        return response['hits']['hits']
    except Exception as e:
        st.error(f"Error querying data: {e}")
        return []


def get_total_inventory_price(index_name, size):
    query = {
        "query": {
            "bool": {
                "filter": [
                    {"term": {"size": size}}
                ]
            }
        },
        "aggs": {
            "total_price": {
                "sum": {
                    "script": {
                        "source": "doc['price'].value * doc['stock_quantity'].value"
                    }
                }
            }
        },
        "size": 0
    }
    try:
        result = es.search(index=index_name, body=query)
        return result['aggregations']['total_price']['value']
    except Exception as e:
        st.error(f"Error calculating total inventory price: {e}")
        return None
