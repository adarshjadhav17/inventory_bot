import streamlit as st
from utils.index_management import create_index
from utils.data_management import load_data, search_data, get_total_inventory_price


INDEX_NAME = "tshirt_inventory"
DATA_FILE = "data.json"


def main():
    st.title("T-Shirt Inventory Dashboard")


    st.sidebar.header("Options")
    query_type = st.sidebar.selectbox("Select Query Type", ["Search Inventory", "Calculate Inventory Price"])


    if query_type == "Search Inventory":
        st.subheader("Search Inventory")
        brand = st.text_input("Brand Name")
        size = st.selectbox("Size", ["XS", "S", "M", "L", "XL"])
        if st.button("Search"):
            if brand and size:
                query = {
                    "query": {
                        "bool": {
                            "must": [{"term": {"brand": brand}}],
                            "filter": [{"term": {"size": size}}]
                        }
                    }
                }
                results = search_data(INDEX_NAME, query)
                if results:
                    st.write("Search Results:")
                    for result in results:
                        st.json(result["_source"])
                else:
                    st.warning("No results found.")
            else:
                st.warning("Please provide both Brand and Size.")


    elif query_type == "Calculate Inventory Price":
        st.subheader("Calculate Total Inventory Price")
        size = st.selectbox("Size", ["XS", "S", "M", "L", "XL"])
        if st.button("Calculate"):
            if size:
                total_price = get_total_inventory_price(INDEX_NAME, size)
                if total_price is not None:
                    st.write(f"Total Inventory Price for {size}-size T-Shirts: ${total_price:,.2f}")
            else:
                st.warning("Please select a Size.")

if _name_ == "_main_":

    create_index(INDEX_NAME)

    load_data(INDEX_NAME, DATA_FILE)

    main()
