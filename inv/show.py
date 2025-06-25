import streamlit as st 
import requests 

# if 'is_clicked' not in st.session_state:
#     st.session_state.is_clicked = ""


# def show_supplier():
#     responce=requests.post(f'http://127.0.0.1:8000/supplier')
#     return responce.json()
# st.write("SHOW SUPPLIER")

# st.session_state.is_clicked=st.button("SHOW",use_container_width=True)
# if st.session_state.is_clicked:
#         sup_show=show_supplier()

#         # st.write(sup_show['data'])
#         cols= st.columns([5,2,2])
        
#         for key in sup_show['data']:
#             cols= st.columns([5,2,2])    
#             for a in key.items() :
#                 with cols[0]:
#                     if a[0]=="supplier_name":
#                         st.markdown(f"SUPPLER NAME :{a[1]}")
#                     if a[0]=="supplier_age":
#                         st.write(f" AGE :{a[1]}")
#                     if a[0]=="contact_info":
#                         st.write(f"CONTACT :{a[1]}")
#             with cols[1]:
#                 is_clicked_delete=st.button(f"Update {key['supplier_name']}")

#             with cols[2]:
#                 st.button(f"Delete {key['supplier_name']}")
#             st.divider()  
              











# import streamlit as st 
# import requests 

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
        st.success(f"{action.capitalize()} button clicked for {name}")