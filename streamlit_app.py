import streamlit as st

#price range & housing info
st.title('Test')

#name of tabs 
tab1, tab2 = st.tabs(["college a", "college b"])

#sidebar to select different different settings.
with st.sidebar: 
    #get price range
    priceRange = st.radio(
        "What is your price range",
        ["High", "Medium", "Low"],
        captions=[
            "$30,000+",
            "$10,000-$20,000",
            "Below $10,000",
        ],
    )
    
    #get housing type
    housing = st.radio(
        "What type of housing would you like?",
        ["On-campus", "Off-campus", "Else"]
    )
    
    #write result 4 price range
    st.write("You selected:", priceRange)
    if housing == "Else": 
        housingElse = st.text_input("What are you planning?")

#tabs :)
with tab1:
        st.header("college a")
        
with tab2:
        st.header("college b")

#containers
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)

for colNum in row1 + row2 + row3:
    tile=colNum.container(height=175)
    tile.title("college")

container = st.container(border=True)
container.title('coleg')
container.write('coleg picture comin son')






