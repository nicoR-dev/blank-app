import streamlit as st

st.title('Test')
priceRange = st.radio(
    "What is your price range",
    ["High", "Medium", "Low"],
    captions=[
        "$30,000+",
        "$10,000-$20,000",
        "Below $10,000",
    ],
)
st.write("You selected:", priceRange)
