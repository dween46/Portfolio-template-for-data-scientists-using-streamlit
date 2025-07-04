import streamlit as st
from utils import sidebar, footer, last_updated

def show_page():
    """Shows the home page of the portfolio."""
    st.set_page_config(page_title="Home", layout="wide")
    last_updated()

    # --- HERO SECTION ---
    st.title("Your Name")
    st.subheader("Your Title (e.g., Data Scientist, Software Engineer)")
    
    # Placeholder for headshot
    st.image("https://via.placeholder.com/150", width=150)

    st.write(
        """
        **Introduction:**
        
        A brief and engaging introduction about yourself. 
        Highlight your key skills and what you are passionate about.
        """
    )

# --- MAIN ---
if __name__ == "__main__":
    sidebar()
    show_page()
    footer()
