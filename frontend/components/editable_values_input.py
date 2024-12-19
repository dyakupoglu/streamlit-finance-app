import streamlit as st


def editable_values_input(default_values, disabled_values=False):
    input_str = st.text_input(
        "Comma-separated values",
        ",".join(map(str, default_values)),
        disabled=disabled_values,
    )
    try:
        values = list(map(float, input_str.split(",")))
        return values
    except:
        st.warning(
            "Invalid input values. Please provide comma-separated numeric values."
        )
        return default_values
