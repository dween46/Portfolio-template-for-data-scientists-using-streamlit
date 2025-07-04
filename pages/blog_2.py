import streamlit as st
from utils import footer, last_updated, sidebar, generate_toc, add_anchors
import textwrap


def show_page():
    """Shows the second blog post."""
    st.set_page_config(page_title="Blog Post 2", layout="wide")
    last_updated()
    st.title("Blog Post 2: Another Interesting Topic")
    st.write("**Date:** February 1, 2025")

    # --- HERO IMAGE ---
    st.image("https://via.placeholder.com/800x400", caption="A descriptive caption for your image.")

    # --- BLOG CONTENT ---
    blog_content = textwrap.dedent("""
    ### Section 1: Introduction

    Start with an engaging introduction to your topic.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis et quam ut nisl mollis rhoncus. Sed ac arcu a ante commodo volutpat. In hac habitasse platea dictumst. Vivamus et elit eu mauris finibus fringilla. Nullam suscipit, purus vitae feugiat tincidunt, nisi nisl facilisis magna, et lacinia elit turpis et nulla. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

    ### Section 2: Main Body

    Elaborate on your topic with more details, examples, and code snippets if necessary.

    Phasellus vel metus eget nisi porta interdum. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. 

    Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero. Sed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean quam. In scelerisque sem at dolor. Maecenas mattis. Sed convallis tristique sem. Proin ut ligula vel nunc egestas porttitor. Morbi lectus risus, iaculis vel, suscipit quis, luctus non, massa.

    #### Subsection 2.1: Another Example

    More details here.

    Ut convallis, sem sit amet interdum consectetuer, odio augue aliquam leo, nec dapibus tortor nibh sed augue. Integer eu magna sit amet metus fermentum posuere. Morbi sit amet nulla sed dolor elementum imperdiet. Quisque fermentum. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque adipiscing eros ut libero. Ut condimentum mi vel tellus. Suspendisse laoreet. Fusce ut est sed dolor gravida convallis.

    ```python
    import pandas as pd

    df = pd.DataFrame({
        'col1': [1, 2, 3],
        'col2': [4, 5, 6]
    })
    st.dataframe(df)
    ```

    ### Section 3: Conclusion

    Summarize your key points and provide a concluding thought.

    Nam nec ante. Sed lacinia, urna non tincidunt mattis, tortor neque adipiscing diam, a cursus ipsum ante quis turpis. Nulla facilisi. Ut fringilla. Suspendisse potenti. Nunc feugiat mi a tellus consequat imperdiet. Vestibulum sapien. Proin quam. Etiam ultrices. Suspendisse in justo eu magna luctus suscipit.
    """
    )
    with st.expander("📌 Table of Contents"):
        st.markdown(generate_toc(blog_content), unsafe_allow_html=True)

    st.markdown(add_anchors(blog_content), unsafe_allow_html=True)

# --- MAIN ---
if __name__ == "__main__":
    sidebar()
    show_page()
    footer()
