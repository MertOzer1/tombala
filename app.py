import streamlit as st
import pandas as pd

def main():
    st.title("Bingo Tracker")
    sheets, called_numbers = load_data()

    add_sheet(sheets, called_numbers)

    new_game(sheets, called_numbers)
    delete_sheet(sheets)
    enter_number(sheets, called_numbers)

    display_sheets(sheets, called_numbers)






def load_data():
    if 'sheets' not in st.session_state:
        st.session_state.sheets = []
    if 'called_numbers' not in st.session_state:
        st.session_state.called_numbers = []
    return st.session_state.sheets, st.session_state.called_numbers

def save_data(sheets, called_numbers):
    st.session_state.sheets = sheets
    st.session_state.called_numbers = called_numbers

def enter_number(sheets, called_numbers):
    with st.form("enter_number"):
        st.write("Enter a Called Number")
        called_number = st.number_input('Number', min_value=1, max_value=99, key='called_number')
        submit_called_number = st.form_submit_button("Enter Number")

        if submit_called_number and called_number not in called_numbers:
            called_numbers.append(called_number)
            save_data(sheets, called_numbers)



def new_game(sheets, called_numbers):
    if st.button("New Game"):
        called_numbers.clear()  # Reset the called numbers


def delete_sheet(sheets):
    delete_sheet_index = st.selectbox("Select a Sheet to Delete", range(len(sheets)), format_func=lambda x: f"Sheet {x+1}")
    if st.button("Delete Sheet"):
        if 0 <= delete_sheet_index < len(sheets):
            del sheets[delete_sheet_index]

def add_sheet(sheets, called_numbers):
    with st.form("add_sheet"):
        st.write("Add a New Bingo Sheet")
        new_sheet_numbers = [st.number_input(f'Number {i}', min_value=1, max_value=99, key=f'number{i}') for i in range(1, 16)]
        submit_button = st.form_submit_button("Add Sheet")
        
        if submit_button:
            sheets.append(new_sheet_numbers)
            save_data(sheets, called_numbers)



def display_sheets(sheets, called_numbers):
    for index, sheet in enumerate(sheets):
        st.write(f"Bingo Sheet {index + 1}")
        # Create a DataFrame for each sheet
        data = [sheet[i:i+5] for i in range(0, 15, 5)]  # Split sheet into rows
        df = pd.DataFrame(data)
        # Apply highlighting style
        st.dataframe(df.style.applymap(lambda x: 'background-color: yellow' if x in called_numbers else ''))








if __name__ == "__main__":
    main()
