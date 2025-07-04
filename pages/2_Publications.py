import streamlit as st
from utils import footer, last_updated, sidebar

def show_page():
    """Shows the publications page."""
    st.set_page_config(page_title="Publications", layout="wide")
    last_updated()
    st.title("Publications")

    # --- PUBLICATION 1 ---
    st.write(
        """
        - **Author(s). (Year).** *Title of the paper.*
          *Journal/Conference Name*, Volume(Issue), pages.
          [DOI/URL](https://your-publication-link.com)
        """
    )

    # --- PUBLICATION 2 ---
    st.write(
        """
        - **Author(s). (Year).** *Title of the paper.*
          *Journal/Conference Name*, Volume(Issue), pages.
          [DOI/URL](https://your-publication-link.com)
        """
    )

# --- MAIN ---
if __name__ == "__main__":
    sidebar()
    show_page()
    footer()
