import streamlit as st
from datetime import datetime, timedelta


def determine_week(start_date, query_date=None):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")

    if not query_date:
        query_date = datetime.now()
    else:
        query_date = datetime.strptime(query_date, "%Y-%m-%d")

    delta_days = (query_date - start_date).days
    week_num = (delta_days // 7) % 4 + 1

    return week_num


def set_start_date():
    st.title("Set Start Date")

    # Input for start date
    start_date = st.date_input(
        "Start Date (When the week system started):", datetime(2023, 9, 2)
    )

    # Use session state to save the start date
    st.session_state.start_date = start_date.strftime("%Y-%m-%d")

    if st.button("Proceed to Determine Week"):
        st.session_state.page = "Determine Week"


def display_week():
    st.title("Determine the Week")

    # Input for query date
    query_date = st.date_input("Query Date:", datetime.now())

    # Calculate and display the week number
    if "start_date" in st.session_state:
        week_number = determine_week(
            st.session_state.start_date, query_date.strftime("%Y-%m-%d")
        )
        st.write(
            f"The week number for {query_date.strftime('%Y-%m-%d')} is: Week {week_number}"
        )
    else:
        st.write("Please set the start date first.")


def main():
    st.sidebar.title("Navigation")
    pages = {"Set Start Date": set_start_date, "Determine Week": display_week}

    # Page selection
    if "page" not in st.session_state:
        st.session_state.page = "Set Start Date"

    st.session_state.page = st.sidebar.radio(
        "Choose a page",
        list(pages.keys()),
        index=list(pages.keys()).index(st.session_state.page),
    )
    pages[st.session_state.page]()


if __name__ == "__main__":
    main()
