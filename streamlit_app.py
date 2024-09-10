import streamlit as st

st.title("🎈 My new app")

st.title("Hello, Streamlit!")

name = st.text_input("What's your name?")

if st.button("Submit"):
    st.write(f"Hello, {name}!")


