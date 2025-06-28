import streamlit as st 
import requests 

a=[]
getsup=requests.get("http://127.0.0.1:8000/category")
for i in getsup.json()["data"]:
    a.append(i["category_name"])    
sel=st.selectbox("select",a)
if st.button("press"):
    st.write(sel)