import streamlit as st
import random

st.title("Projects")

# Check if a user input has been entered in session state
if "my_input" not in st.session_state:
    st.write("Please go to the homepage and enter a number between 1 and 9.")
else:
    # Generate a random number between 1 and 9
    random_number = random.randint(1, 9)

    st.subheader(f"You have entered: {st.session_state['my_input']}")
    st.subheader(f"Generated random number: {random_number}")

    # Compare user input with random number
    if st.session_state["my_input"] == random_number:
        st.title("Hurrah! You have won the game!")
    else:
        st.title("You have lost! Try Again!")
