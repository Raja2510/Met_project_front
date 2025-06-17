import streamlit as st
from api import login,register

st.title("LOGIN/REGISTERATION APP")

tab=st.tabs(["LOGIN","REGISTER"])

# col=st.columns([2,1,2])



with tab[0]:
    st.header("LOGIN PAGE")
    username=st.text_input("Username",placeholder="Enter Username")
    password=st.text_input("password",placeholder="Enter password",type="password")
    is_checked=st.checkbox("Agree to terms and conditions")
    is_clicked=st.button("login",use_container_width=True)
    if is_clicked:
        if username and password and is_checked:
            data = login(username, password)
            if data:
                st.toast("Login successful")
            else:
                st.toast('Invalid credentials')
        else:
            st.toast("Please fill the form")



with tab[1]:
    st.header(" REGISTERATION PAGE")
    reg_name=st.text_input("Enter name",placeholder="Enter name")
    reg_username=st.text_input("Choose a username",placeholder="Enter username")
    reg_password=st.text_input("Choose a password",placeholder="Enter password",type="password")
    reg_age=st.text_input("Age",placeholder="Enter age")
    reg_is_checked=st.checkbox("Agree to terms")
    reg_is_clicked=st.button("Register",use_container_width=True)
    if reg_is_clicked:
        if reg_is_checked and reg_username and reg_name and reg_password and reg_age:
            st.toast("Processing")
            show=register(reg_name,reg_username,reg_age,reg_password)
            st.toast(show)
            
            # st.balloons()
        else:
            st.toast("Enter all feilds")
