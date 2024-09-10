import streamlit as st

st.title("🎈 My new app")
price = st.radio(
    'Choose your price range:'.
    ['Low: 7,000-10,000', 'Medium: 10,000-20,000', 'High']
    captions=[
        '7,000-10,000',
        '10,000-20,000',
        '20,000+',
    ],
)

