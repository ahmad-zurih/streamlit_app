import streamlit as st
import spacy
from spacy import displacy as ds


nlp = spacy.load("en_core_web_sm")

st.markdown("# Insert a string to output the name entities in it")


text = st.text_input("type here")

if text:
    doc = nlp(text)
    out = ds.render(doc, style="ent")
    st.markdown(out, unsafe_allow_html=True)