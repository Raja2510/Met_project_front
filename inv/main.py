import streamlit as st
cols=st.columns([0.2,5,0.2])
with cols[1]:
    st.title('SUPPLIER MANAGEMENT')
    cols2=st.columns([5,5])
    with cols2[0]:
        is_clicked_add=st.button("ADD SUPPLIERS",use_container_width=True,type="primary")
    if is_clicked_add:   
        # add_page=st.Page("add.py")
        # add_nav=st.navigation([add_page],expanded=True)
        # add_nav.run()
        st.switch_page("pages/add.py")
    with cols2[1]:
        is_clicked_show=st.button("  SHOW  SUPPLIERS",use_container_width=True,type="primary")
        if is_clicked_show:
            st.switch_page("pages/show.py")

# import streamlit as st

# # Hide sidebar
# st.markdown("""
#     <style>
#     [data-testid="stSidebar"] { display: none; }
#     </style>
# """, unsafe_allow_html=True)

# # Initialize page state
# if "page" not in st.session_state:
#     st.session_state.page = "home"

# # Navigation buttons
# def navigate(page_name):
#     st.session_state.page = page_name

# # Home page
# if st.session_state.page == "home":
#     st.title("🏠 Home Page")
#     if st.button("Go to Add Page"):
#         navigate("add")

# # Add page
# elif st.session_state.page == "add":
#     st.title("➕ Add Page")
#     if st.button("Back to Home"):
#         navigate("home")
