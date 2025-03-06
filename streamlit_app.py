import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

hide_streamlit_styles = """
<style>
footer {visibility: hidden;}
</style>
"""
st.html(hide_streamlit_styles)
