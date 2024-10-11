import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("🎯Let's Play a Game!")

st.sidebar.success("Select a page above.")

# Input option for number 1 to 9
if "my_input" not in st.session_state:
    st.session_state["my_input"] = 0

# Displaying the subheader for the input prompt
st.subheader("Enter a number between 1 and 9")

# Number input method
my_input = st.number_input("", min_value=1, max_value=9, step=1)
submit = st.button("Submit")

if submit:
    st.session_state["my_input"] = my_input
    st.subheader(f"You have entered: {my_input}")
    st.title(f"Go to Projects Page for Surprise!")
