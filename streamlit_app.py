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

housing = st.radio(
    "What type of housing would you like?",
    ["On-campus", "Off-campus", "Else"]
)

if housing == "Else": 
    housingElse = st.text_input("What are you planning?")
    st.form_submit_button("Submit")
    
st.write("You selected:", priceRange)
