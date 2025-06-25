
import streamlit as st
import requests
# Hide sidebar



# Initialize page state
if "page" not in st.session_state:
    st.session_state.page = "home"

# Navigation buttons
def navigate(page_name):
    st.session_state.page = page_name
    st.rerun()

# Home page
if st.session_state.page == "home":
    st.title(" Home Page")
    if st.button("Go to Add Page"):
        navigate("add")
    if st.button("Go to Show Page"):
        navigate("show")

#show page
elif st.session_state.page=="show":
 
              

    if st.button("GO to Home page"):
        navigate("home")
    

# Add page
elif st.session_state.page == "add":
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
            if sup_added !="This person already exsist":
                st.write(f"name = {sup_added[0]["supplier_name"]}..\n..age = {sup_added[0]["supplier_age"]}..\n..contact={sup_added[0]["contact_info"]} \nis added")
            else:
                st.write(sup_added)
    if st.button("Back to Home",type="primary"):
        st.session_state.sup_name = ""
        st.session_state.sup_age= ""
        st.session_state.sup_contact = ""
        navigate("home")
        st.rerun()
    
