import streamlit as st
from PIL import Image

st.markdown("# This site does dependency parsing and named entity recognition when given a string. It uses "
            "SpaCy tool displaCy")

st.markdown("<br><br>", unsafe_allow_html=True)

image_dep = Image.open("images/dep_example.jpg")
image_ner = Image.open("images/ner_example.jpg")

st.markdown("## example using dependency parsing:")
st.image(image_dep)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("## example using NER:")
st.image(image_ner)