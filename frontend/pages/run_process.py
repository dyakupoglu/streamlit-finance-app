import streamlit as st
import datetime
from api import get_companies, compute_results, save_result
from components import editable_values_input, display_results


def initialize_session_state():
    if "initialized" not in st.session_state:
        st.session_state.update(
            {
                "selected_company": None,
                "selected_date": datetime.date.today(),
                "input_values": [],
                "results": None,
                "ongoing_process": False,
                "run_button_clicked": False,
                "initialized": True,
            }
        )


def is_inputs_filled():
    return (
        st.session_state.selected_company is not None
        and st.session_state.selected_date is not None
        and len(st.session_state.input_values) > 0
    )


def process_results():
    st.session_state.results = None
    st.session_state.ongoing_process = True

    result_data = compute_results(
        st.session_state.selected_company,
        st.session_state.selected_date,
        st.session_state.input_values,
    )

    st.session_state.results = result_data if result_data else None
    if not result_data:
        st.error("Computation failed.")

    st.session_state.ongoing_process = False
    st.session_state.run_button_clicked = False


def render_form():
    companies = get_companies()
    st.session_state.selected_company = st.selectbox(
        "Select Company",
        [None] + companies,
        index=0,
        key="company_select",
        disabled=st.session_state.ongoing_process,
    )

    selected_date = st.date_input(
        "Select Start Date",
        value=st.session_state.selected_date,
        key="selected_date",
        disabled=st.session_state.ongoing_process,
    )
    if selected_date != st.session_state.selected_date:
        st.session_state.selected_date = selected_date

    st.write("Input Values (Adjust as needed):")
    input_values = editable_values_input(
        st.session_state.input_values, st.session_state.ongoing_process
    )
    if input_values != st.session_state.input_values:
        st.session_state.input_values = input_values


def render_results():
    display_results(
        st.session_state.results["series_only"],
        st.session_state.results["series_with_strings"],
    )

    if st.button("Save Results"):
        saved_id = save_result(
            st.session_state.selected_company,
            st.session_state.selected_date,
            st.session_state.results,
        )
        if saved_id:
            st.success("Results saved successfully!")
        else:
            st.error("Failed to save results.")


def run_process_page():
    st.title("Run Process")
    initialize_session_state()

    render_form()

    run_button_disabled = not is_inputs_filled() or st.session_state.ongoing_process
    st.button(
        "Run",
        disabled=run_button_disabled,
        key="run_process_button",
        on_click=start_processing,
    )
    info_placeholder = st.empty()
    if st.session_state.run_button_clicked:
        info_placeholder.info("Computation running... Please wait.")

    if st.session_state.results:
        info_placeholder.empty()
        render_results()


def start_processing():
    st.session_state.run_button_clicked = True
    st.session_state.ongoing_process = True
    process_results()
