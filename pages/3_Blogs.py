import streamlit as st
from utils import footer, last_updated, sidebar

def show_page():
    """Shows the blog hub page."""
    st.set_page_config(page_title="Blogs", layout="wide")
    last_updated()
    st.title("Blogs")

    st.write("Click on the links below to read the blog posts.")

    # --- BLOG LINKS ---
    st.page_link("pages/blog_1.py", label="Blog Post 1: My First Blog Post")
    st.page_link("pages/blog_2.py", label="Blog Post 2: Another Interesting Topic")

# --- MAIN ---
if __name__ == "__main__":
    sidebar()
    show_page()
    footer()
