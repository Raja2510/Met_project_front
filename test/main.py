import streamlit as st
# from api import register
# from api import get_users
# from api import login
 
 
col = st.columns([0.4,3,0.4])
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False 

if st.session_state.logged_in == True:
    st.write('write')
    if st.button("back"):
        st.session_state.logged_in= False
            

if st.session_state.logged_in == False:
    with col[1]:
        tab1, tab2 = st.tabs(["Login", "Register"])
    
    st.html(
                        '<a href="pages/1.py"></a>'
                    )
    with tab1:
        log_name = st.text_input("username", placeholder="Enter Username", label_visibility="collapsed")
        log_pass = st.text_input("password", placeholder="Enter Password", type="password", label_visibility="collapsed")
        is_clicked = st.button("Login", use_container_width=True, type= "primary")
        if is_clicked:
            if not log_name or not log_pass:
                st.toast("please fill all details", icon= "⚠️")    
            else:
                # result = login(log_name, log_pass)
                a=True
                if a is True:
                    st.session_state.logged_in = True
                    st.toast("Login Successfull", icon="👍")

                else:
                    st.error("Login Failed! \n please check your username and password", icon="😢")
        
        
 
 

 
 
 
 
 
 
 
 
 
 
 
 
