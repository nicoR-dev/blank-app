import streamlit as st

#price range & housing info
st.title('Test')

#name of tabs 
tab1, tab2 = st.tabs(["college a", "college b"])

#sidebar to select different different settings.
with st.sidebar: 
    #get price range
    start_price, end_price = st.select_slider(
        "Select your price range",
        options=[
            "<$10,000",
            "$10,000",
            "$14,000",
            "$18,000",
            "$22,000",
            "$26,000",
            "$30,000",
            ">$30,000",
        ],
        value=("<$10,000", ">$30,000"),
    )
    
    #get housing type
    housing = st.radio(
        "What type of housing would you like?",
        ["On-campus", "Off-campus", "Else"]
    )
    if housing == "Else": 
        housingElse = st.text_input("What are you planning?")

    #your price range
    st.write("Your price range:", start_price, " and ", end_price)

    #write result 4 price range
    st.write("You selected:", priceRange)
#tabs :)
with tab1:
        st.header("college a")
        
with tab2:
        st.header("college b")

#containers
container = st.container(border=True)
container.title('coleg')
container.write('coleg picture comin son')

container = st.container(border=True)
container.title('university of berkley')
container.write('coleg picture comin son')

container = st.container(border=True)
container.title('university of stockton')
container.write('coleg picture comin son')






