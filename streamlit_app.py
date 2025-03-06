import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.write(st.secrets["code"])
vv = eval(st.secrets["vals"])
#exec, compile etc
st.write(vv)


title = st.text_input("Input - use a num", "1")
title  = int(title)
out = exec(f'st.secrets["compute"]')
st.write("Output", out)

hide_streamlit_styles = """
    <style>
    ._container_gzau3_1._viewerBadge_nim44_23 {
        visibility: hidden;
    }
    </style>
    """
st.html(hide_streamlit_styles)
