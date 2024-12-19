import streamlit as st
import pandas as pd
from streamlit_sortables import sort_items


def display_results(series_only, series_with_strings):
    st.subheader("Results")

    items = ["Series Only Table", "Series with Strings Table", "Series Only Chart"]
    reordered = sort_items(items, direction="horizontal")

    for item in reordered:
        if "Only Table" in item:
            st.write("Series Only Table:")
            st.dataframe(pd.DataFrame(series_only))
        elif "Strings" in item:
            st.write("Series with Strings Table:")
            st.dataframe(pd.DataFrame(series_with_strings))
        else:
            st.write("Series Only Chart:")
            df = pd.DataFrame(series_only)
            df["date"] = pd.to_datetime(df["date"])
            st.line_chart(df.set_index("date")[["value1"]])
