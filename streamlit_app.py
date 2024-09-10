import streamlit as st

st.title('Test')
genre = st.radio(
    "What is your price range",
    [":High", "Medium", "Low:"],
    captions=[
        "$30,000+",
        "$10,000-$20,000",
        "Below $10,000",
    ],
)

if genre == "High":
    st.write("You selected high, $30,000+")
else: if genre == "Medium":
    st.write("You selected medium, $10,000-$20,000")
else
    st.write("You selected low, less than $10,000")
