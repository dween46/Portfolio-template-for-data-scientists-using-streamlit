import streamlit as st
import re
from datetime import datetime

def sidebar():
    """Creates a sidebar with a title."""
    # st.sidebar.title("Navigation")


# Function to generate nested HTML Table of Contents
def generate_toc(markdown_text):
    toc = []
    for match in re.finditer(r"^(#{1,6})\s(.+)", markdown_text, flags=re.MULTILINE):
        level = len(match.group(1))
        title = match.group(2).strip()
        anchor = re.sub(r'\s+', '-', title.lower())
        toc.append((level, title, anchor))

    html = "<ul>"
    prev_level = 1
    for level, title, anchor in toc:
        if level > prev_level:
            html += "<ul>" * (level - prev_level)
        elif level < prev_level:
            html += "</ul>" * (prev_level - level)
        html += f'<li><a href="#{anchor}">{title}</a></li>'
        prev_level = level
    html += "</ul>" * prev_level
    return html

# def generate_toc(markdown_text):
#     toc = []
#     for match in re.finditer(r"^\s*(#{1,6})\s(.+)", markdown_text, flags=re.MULTILINE):
#         level = len(match.group(1))
#         title = match.group(2).strip()
#         anchor = re.sub(r'\s+', '-', title.lower())
#         toc.append((level, title, anchor))

#     html = '<div style="font-size: 15px; line-height: 1.6;">'
#     for level, title, anchor in toc:
#         indent_px = (level - 1) * 15  # increase for deeper indentation
#         bullet = "•" if level <= 3 else "◦"
#         html += f'<div style="margin-left: {indent_px}px;"><a href="#{anchor}" style="text-decoration: none; color: #1a73e8;">{bullet} {title}</a></div>'
#     html += "</div>"
#     return html

# Function to add HTML anchors in content
def add_anchors(markdown_text):
    def replace_heading(match):
        hashes = match.group(1)
        title = match.group(2).strip()
        anchor = re.sub(r'\s+', '-', title.lower())
        return f'{hashes} <a name="{anchor}"></a>{title}'
    return re.sub(r"^(#{1,6})\s(.+)", replace_heading, markdown_text, flags=re.MULTILINE)


# def add_anchors(markdown_text):
#     def replace_heading(match):
#         hashes = match.group(1)
#         title = match.group(2).strip()
#         anchor = re.sub(r'\s+', '-', title.lower())
#         return f'{hashes} <a name="{anchor}"></a>{title}'
#     return re.sub(r"^\s*(#{1,6})\s(.+)", replace_heading, markdown_text, flags=re.MULTILINE)


def last_updated():
    """Displays the last updated date."""
    # Get the current date and format it
    updated_date = "July 3, 2025"
    st.markdown(f"<p style='text-align: right;'>Last updated: {updated_date}</p>", unsafe_allow_html=True)


def footer():
    """Creates a footer for each page."""
    st.markdown("---")
    st.markdown("© 2025 Your Name | Built with Streamlit")

