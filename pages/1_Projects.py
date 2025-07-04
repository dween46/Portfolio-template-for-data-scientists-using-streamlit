import streamlit as st
from utils import footer, last_updated, sidebar

def show_page():
    """Shows the projects page."""
    st.set_page_config(page_title="Projects", layout="wide")
    last_updated()
    st.title("Projects")

    # --- PROJECT 1 ---
    st.subheader("Project Title 1")
    st.write("A short description of your project.")
    st.write("**Tech Stack:** Python, Streamlit, Pandas")
    st.write("[Link to Project](https://your-project-link.com)")

    # --- PROJECT 2 ---
    st.subheader("Project Title 2")
    st.write("A short description of your project.")
    st.write("**Tech Stack:** JavaScript, React, Node.js")
    st.write("[Link to Project](https://your-project-link.com)")

    # --- PROJECT 3 ---
    st.subheader("Project Title 3")
    st.write("A short description of your project.")
    st.write("**Tech Stack:** R, Shiny, ggplot2")
    st.write("[Link to Project](https://your-project-link.com)")

# --- MAIN ---
if __name__ == "__main__":
    sidebar()
    show_page()
    footer()
