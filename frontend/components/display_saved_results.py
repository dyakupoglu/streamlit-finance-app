import streamlit as st
import pandas as pd


def display_saved_results(saved_results):
    if not saved_results:
        st.write("No saved results found.")
    else:
        for res in saved_results:
            st.write(
                f"ID: {res['id']}, Company: {res['company']}, Start Date: {res['start_date']}"
            )
            df_only = pd.DataFrame(res["series_only"])
            df_with = pd.DataFrame(res["series_with_strings"])
            st.write("Series Only:")
            st.dataframe(df_only)
            st.write("Series With Strings:")
            st.dataframe(df_with)
            st.write("Series Only Chart:")
            df = pd.DataFrame(df_only)
            df["date"] = pd.to_datetime(df["date"])
            st.line_chart(df.set_index("date")[["value1"]])
