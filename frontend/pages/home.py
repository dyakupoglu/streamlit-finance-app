import streamlit as st


def home_page():
    st.title("Welcome to the Allianz Streamlit Application")
    st.write(
        """
    This application allows you to:
    - Select a company and start date, input values, and run a simulation of financial time series data.
    - View and reorder result tables, and plot the results.
    - Save your processed results and review them later.
    
    Use the tabs at the top to navigate:
    - **Home**: You're here now.
    - **Run Process**: Run simulations and see the results.
    - **Saved Results**: Review previously saved results.
    """
    )
