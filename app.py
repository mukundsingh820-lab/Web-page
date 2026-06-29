import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="All About SDGs & AI", layout="wide")

with open("all-about-sdgs-ai.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=2000, scrolling=True)
