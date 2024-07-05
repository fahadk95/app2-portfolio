import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/image.png.jpg", width=400)

with col2:

    st.title("Fahad Mohammad khan")
    content = """ Hello This is Fahad khan Iam a teacher by profession but
    currently learning to develop some web apps using Python. I have made few apps such as 
    My todo app and image convertor app. This is currently my third app which iam building.
    """
    st.info(content)



