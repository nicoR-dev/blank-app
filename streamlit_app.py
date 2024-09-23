import streamlit as st
import numpy as np

#add data 
college_data = np.genfromtxt(
    'data/us-colleges-and-universities.csv', delimiter=',',
    names=True, dtype=None, encoding='UTF'
)

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
        
    #checkboxes for stars
    rating1 = st.checkbox("1 Star")
    rating2 = st.checkbox("2 Star")
    rating3 = st.checkbox("3 Star")
    rating4 = st.checkbox("4 Star")
    rating5 = st.checkbox("5 Star")

    #sponsors text entry
    st.write("What sponsors that college?")
    sponsors = st.text_input("What is the college's sponsor?")

    #state/location 
    state = st.selectbox(
        "What state is the college/university in?", 
        ("AL", "AK", "AS", "AZ", "AR", "CA", "CO", "CT")
    )
    
    #your price range
    st.write("Your price range:", start_price, " and ", end_price)

    #write the state value 
    st.write(state)
    
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






