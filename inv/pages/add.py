import streamlit as st 
import requests 
if 'sup_name' not in st.session_state:
    st.session_state.sup_name = ""
if 'sup_age' not in st.session_state:
     st.session_state.sup_age= ""
if 'sup_contact' not in st.session_state:
    st.session_state.sup_contact = ""

def add_supplier(name,age, contact):
    responce=requests.post(f'http://127.0.0.1:8000/supplier/create?name={name}&age={age}&contact={contact}')
    return responce.json()
st.write("ADD SUPPLIER")
st.session_state.sup_name = st.text_input("SUPPLIER NAME", value=st.session_state.sup_name, placeholder="Enter name here")
st.session_state.sup_age = st.text_input("SUPPLIER AGE", value=st.session_state.sup_age, placeholder="Enter age here")
st.session_state.sup_contact = st.text_input("SUPPLIER CONTACT", value=st.session_state.sup_contact, placeholder="Enter contact here")

is_clicked=st.button("ADD",use_container_width=True)
if is_clicked:
    if st.session_state.sup_name and st.session_state.sup_age and st.session_state.sup_contact:
        sup_added=add_supplier(st.session_state.sup_name,st.session_state.sup_age,st.session_state.sup_contact)
        st.write(sup_added)



