import streamlit as st

st.title("Give us a Feedback :)")

st.subheader("We want to know if you liked the experience of this site and that's why we would like you to evaluate our project.")

sentiment_mapping = ["one", "two", "three", "four", "five"]

selected = st.slider("Give us a rating (1 to 5 stars)", 1, 5)

if selected is not None:
    st.markdown(f"You give us {sentiment_mapping[selected - 1]} star(s).")

st.header("Thank You!")

st.image("images\heart2.png",use_column_width=True)