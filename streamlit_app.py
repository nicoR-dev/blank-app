import streamlit as st
import numpy as np

#add data 

# import pandas as pd
# coldata=pd.read_excel(
#     'data/us-colleges-and-universities.xlsx', 
# )
# # coldata.head()
# st.write("blah")


#price range & housing info
st.title('Test')

#extra options
with st.expander('Extra settings.'): 
    col_sports = st.selectbox(
        "What are the college's sports?",
        ('Soccer', 'Hockey', 'Basketball')
    )
    col_intern = st.selectbox(
        "What are the college's internships?",
        ('blah')
    )
    col_degree = st.radio(
        with st.title("What type of degree do you want?"),
        # "What type of degree do you want?", 
        ['Engineering', 'Biology', 'Nursing', 'Astronomy']
    )

#name of tabs 
tab1, tab2 = st.tabs(["college a", "college b"])

#sidebar to select different different settings.
with st.sidebar: 
    #college name
    st.write("Type the college name")
    col_name = st.text_input("What is the college's name?")
    
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
    
    #Admission requirements 
    st.header("Admission requirements:")
    admis_reqs1=st.checkbox('Extracurricular Activities')
    admis_reqs2=st.checkbox('Standardized Test Scores')
    admis_reqs3=st.checkbox('Student GPA')
    admis_reqs4=st.checkbox('Personal Statment/Essay')
    admis_reqs5=st.checkbox('Recommendation Letters')
    admis_reqs6=st.checkbox('Invested Interest')
    admis_reqs7=st.checkbox('Class Rank')
    admis_reqs8=st.checkbox('Good Behavior"')

    #Programs
    col_program = st.selectbox(
        "What are the college's programs?", 
        ("Business", "Bio Engineering", "Health Sciences", "Computer Engineering", "Civil Engineering", "Engineering", "Biology", "Education")
    )

    
    st.header("You've chosen:")
    #your price range
    st.write("Your price range:", start_price, " and ", end_price)

    #write the state value 
    st.write("The college's state:", state)
    
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



    


