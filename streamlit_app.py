import streamlit as st
from app.view import render_lifebook_page

if __name__ == '__main__':
    st.set_page_config(page_title="Life Book", layout="wide")
    render_lifebook_page()

# # st.title("🎈 My new app")
# # st.write(
# #     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# # )

# # st.write("Hello Worlds")