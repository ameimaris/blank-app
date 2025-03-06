import streamlit as st


import streamlit.components.v1 as components

# Inject HTML and CSS using st.components.v1.html to hide the element on page load
components.html(
    """
    <style>
    ._container_gzau3_1._viewerBadge_nim44_23 {
        display: none !important;
    }
    </style>
    """,
    height=0,  # Set a minimal height since it's just for styling
    scrolling=False
)

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.write(st.secrets["code"])
vv = eval(st.secrets["vals"])
#exec, compile etc
st.write(vv)

st.write(st.secrets["compute"])

title = st.text_input("Input - use a num", "1")
st.write(title)
title  = int(title)
st.write(title)

out = eval(eval(st.secrets["compute"]))
st.write("Output", out)

hide_streamlit_styles = """
    <style>
    ._container_gzau3_1._viewerBadge_nim44_23 {
        visibility: hidden;
    }
    </style>
    """
st.markdown(hide_streamlit_styles,unsafe_allow_html=True)
