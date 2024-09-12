import streamlit as st

#price range & housing info
st.title('Test')

#name of tabs 
tab1, tab2 = st.tabs(["college a", "college b"])

#sidebar to select different different settings.
with st.sidebar: 
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

#tabs :)
    with tab1:
        st.header("college a")
        
    with tab2:
        st.header("college b")
    
    
    st.write("You selected:", priceRange)


