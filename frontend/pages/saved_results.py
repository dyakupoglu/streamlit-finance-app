import streamlit as st
from api import fetch_saved_results
from components import display_saved_results


def saved_results_page():
    st.title("Saved Results")
    saved_results = fetch_saved_results()
    display_saved_results(saved_results)
