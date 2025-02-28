import streamlit as st

# st.set_page_config(page_title="Thyroid Cancer AI Dashboard", layout="wide", initial_sidebar_state="expanded")

# st.sidebar.title("Navigation")
# st.sidebar.write("[🏠 Home](home)")
# st.sidebar.write("[ℹ️ About](about)")
# st.sidebar.write("[📞 Contact](contact)")

# import streamlit as st

# st.set_page_config(page_title="Thyroid Cancer AI Dashboard", layout="wide")

# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to:", ["Home", "About", "Contact"])

# if page == "Home":
#     st.title("Home")
#     st.write("Welcome to the Home Page!")
# elif page == "About":
#     st.title("About")
#     st.write("This is the About Page.")
# elif page == "Contact":
#     st.title("Contact")
#     st.write("Reach us at: contact@example.com")


st.set_page_config(page_title="Thyroid Cancer AI Dashboard", layout="wide")

st.markdown("""
    <style>
        section[data-testid="stSidebarNav"] {display: none;}
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("Navigation")



