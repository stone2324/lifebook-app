import streamlit as st
from app.view import render_lifebook_page

if __name__ == '__main__':
    st.set_page_config(page_title="Life Book", layout="wide")
    render_lifebook_page()