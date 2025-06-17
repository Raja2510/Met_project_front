import streamlit as st
from api import login,register

tab=st.tabs(["login","regester"])

# col=st.columns([2,1,2])



with tab[0]:
    st.header("login page")
    username=st.text_input("username",placeholder="Enter username")
    password=st.text_input("password",placeholder="Enter password",type="password")
    is_checked=st.checkbox("agree to terms and conditions")
    is_clicked=st.button("login",use_container_width=True)
    if is_clicked:
        if username and password and is_checked:
            data = login(username, password)
            if data:
                st.toast("Login successful")
            else:
                st.toast('invalid credentials')
        else:
            st.toast("Please fill the form")



with tab[1]:
    st.header("register")
    reg_name=st.text_input("choose a namename",placeholder="Enter namename")
    reg_username=st.text_input("choose a username",placeholder="Enter username")
    reg_password=st.text_input("choose a password",placeholder="Enter password")
    reg_age=st.text_input("age",placeholder="Enter age")
    reg_is_checked=st.checkbox("Agree to terms")
    reg_is_clicked=st.button("register",use_container_width=True)
    if reg_is_clicked:
        if reg_is_checked and reg_username and reg_name and reg_password and reg_age:
            st.toast("Processing")
            show=register(reg_name,reg_username,reg_age,reg_password)
            st.toast(show)
            st.balloons()
        else:
            st.toast("Enter all feilds")   
    