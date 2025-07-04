import streamlit as st
import re

# Sample blog content in markdown
blog_content = """
# Introduction
Welcome to the blog.

## What is Streamlit?
Streamlit is a Python library.

## Benefits
- Easy to use
- Fast development

# Features
## Widgets
## Layouts
### Columns
### Expanders

# Conclusion
"""

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

# Function to add HTML anchors in content
def add_anchors(markdown_text):
    def replace_heading(match):
        hashes = match.group(1)
        title = match.group(2).strip()
        anchor = re.sub(r'\s+', '-', title.lower())
        return f'{hashes} <a name="{anchor}"></a>{title}'
    return re.sub(r"^(#{1,6})\s(.+)", replace_heading, markdown_text, flags=re.MULTILINE)

# Display in Streamlit
st.title("📚 Blog Page")

with st.expander("📌 Table of Contents"):
    st.markdown(generate_toc(blog_content), unsafe_allow_html=True)

st.markdown(add_anchors(blog_content), unsafe_allow_html=True)
