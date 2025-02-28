import streamlit as st

st.title("Contact Us")

st.write("Feel free to contact us and we will get back to you as soon as possible")
st.write("📞 0752 xxx xxx")
st.write("✉️ lianamora@gmail.com")


st.image("images\header-contact.jpg", use_column_width=True)

button_css = """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
        color: white;
    }
    </style>
"""
st.markdown(button_css, unsafe_allow_html=True)

#Contact form

name = st.text_input("Name:")
email = st.text_input("Email:")
message = st.text_area("Message:")

if st.button("Submit"):
  if name and email and message:
    st.success(f"Thank you {name}! Your message has been sent succesfully.")
  else:
    st.error("Please fill all the fields!")
