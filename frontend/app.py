import streamlit as st
from pages.home import home_page
from pages.run_process import run_process_page
from pages.saved_results import saved_results_page

st.set_page_config(layout="centered")

tabs = st.tabs(["Home", "Run Process", "Saved Results"])

with tabs[0]:
    home_page()

with tabs[1]:
    run_process_page()

with tabs[2]:
    saved_results_page()
