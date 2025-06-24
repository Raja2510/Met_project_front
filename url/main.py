import streamlit as st 
import requests

cols=st.columns([0.5,3,0.5])
with cols[1]:
    st.title("URL Shortner")

    lurl=st.text_input("Enter Url",placeholder="ENTER LONG URL" )
    isclicked=st.button("shorten",use_container_width=True)
    if isclicked and lurl:
        responce=requests.post(f"http://127.0.0.1:8000/?long_url={lurl}")
        if responce.status_code==200:
            st.write(responce.json())   