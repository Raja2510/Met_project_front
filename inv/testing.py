import streamlit as st
import requests
if "page" not in st.session_state:
    st.session_state.page = "home"


def navigate(page_name):
    st.session_state.page = page_name
    st.rerun()


if st.session_state.page == "home":
    st.title(" Home Page")
    if st.button("Go to category Page",use_container_width=True,type="primary"):
        navigate("category_page")
    if st.button("Go to supplier Page",use_container_width=True,type="primary"):
        navigate("supplier_page")





# -----------------------------supplier-------------------------------------------------------------------------------

if st.session_state.page=="supplier_page":
    st.title("SUPPLIER PAGE")
    if st.button("SHOW SUPPLIER DETAILES",use_container_width=True):
        navigate("show_supplier")
    if st.button("ADD SUPPLIER",use_container_width=True):
        navigate("add_supplier")
    if st.button("go to home",key="supplier",use_container_width=True,type="primary"):
        navigate("home")

#  ---show page supplier ----------------------
if st.session_state.page=="show_supplier":

    def show_supplier():
        response = requests.post('http://127.0.0.1:8000/supplier')
        return response.json()

    st.write("SHOW SUPPLIER")

    # Load data when "SHOW" is clicked
    if "show_clicked" not in st.session_state:
        st.session_state.show_clicked = False

    if st.button("SHOW", use_container_width=True):
        st.session_state.show_clicked = True

    if st.session_state.show_clicked:
        sup_show = show_supplier()
        
        for key in sup_show['data']:
            cols = st.columns([5, 2, 2])    

            with cols[0]:
                st.markdown(f"**SUPPLIER NAME:** {key['supplier_name']}")
                st.write(f"**AGE:** {key['supplier_age']}")
                st.write(f"**CONTACT:** {key['contact_info']}")

            update_key = f"update_{key['supplier_name']}"
            delete_key = f"delete_{key['supplier_name']}"

            with cols[1]:
                if st.button("Update", key=update_key):
                    st.session_state['action'] = f"update:{key['supplier_name']}"

            with cols[2]:
                if st.button("Delete", key=delete_key):
                    st.session_state['action'] = f"delete:{key['supplier_name']}"

            st.divider()

        # Handle button actions
        if 'action' in st.session_state:
            action, name = st.session_state['action'].split(":")
            if action == "update":
                upname=st.text_input("updated name",placeholder="enter updated age")
                upage=st.text_input("updated age",placeholder="enter updated age")
                upcontact=st.text_input("updated contact",placeholder="enter updated contactt")
                if st.button("update",key="supplier"):
                    if upage and upcontact and upname:
                        updateresponce=requests.put(f"http://127.0.0.1:8000/supplier/update?name={name}&uname={upname}&age={upage}&contact={upage}")
                        st.write(updateresponce.json())
                    else:
                        st.write("check inputs")
            if action=="delete":
                delresponce=requests.delete(f"http://127.0.0.1:8000/supplier?name={name}")
                st.write(delresponce.json(),"deleted sucessfully")
                del st.session_state['action']
                navigate("show_supplier")
            st.success(f"{action.capitalize()} button clicked for {name}")

    if st.button("Refresh"):
        if "show_clicked" in st.session_state:
            st.session_state.show_clicked=False
        if "action"in st.session_state:
            del st.session_state['action']
        st.rerun()
    if st.button("Back",key="show_supplier",type="primary"):
        navigate("supplier_page")
    

# Add page supplier-----------
if st.session_state.page == "add_supplier":
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
    if st.button("Back",key="add_supplier",type="primary"):
        st.session_state.sup_name = ""
        st.session_state.sup_age= ""
        st.session_state.sup_contact = ""
        navigate("supplier_page")
    








#--------------------------category-------------

if st.session_state.page=="category_page":
    st.write("category here")
    if st.button("add category",use_container_width=True):
        navigate("category_add")
    if st.button("go to home",key="category_home"):
        navigate("home")
#--------------category Add page
if st.session_state.page=="category_add":
    st.title('Add Category')
    new_category_name=st.text_input("ENTER NEW CATEGORY",placeholder='enter here')
    new_category_desc=st.text_input("ENTER ITS DESCREPTION",placeholder='enter here')
    if st.button("ADD",key="add category"):
        if new_category_desc and new_category_name:
            responce=requests.post(f"http://127.0.0.1:8000/category/create?name={new_category_name}&desc={new_category_desc}")
            if responce.status_code==200:
                st.write(responce.json()[0])

    if st.button("Go back",key="categoty_add",use_container_width=True):
        navigate("category_page")

