"""
# Our first app
"""

import time

import streamlit as st
from transformers import pipeline


def load_model():
    model = pipeline("fill-mask", model="albert-base-v2")
    return model


model = load_model()

#  логотип и название
col1, col2 = st.columns([1, 1])

with col1:
    st.header('Model "Fill mask"')

with col2:
    st.image("books.png")

# Боковая панель
st.sidebar.image("logotip.png", width=250)
st.sidebar.title("About the project:")
st.sidebar.info(
    """
    Machine learning model 'albert-base-v2' (https://huggingface.co/albert-base-v2). 
    """
)

st.sidebar.info(
    """
    The model generates a word instead of [MASK] in a sentence in English language.
    """
)

st.sidebar.info(
    """
    The model generates a word instead of [MASK] in a sentence in English language.
    """
)

st.sidebar.info(
    """
    Examples: I like apples and  [MASK]., My [MASK] often travels.,
    I always get up at 8 o’clock in the [MASK]., We have a [MASK] in London., He [MASK] football every Saturday.
    """
)

# Ввод текста

inp = st.text_input(
    "Please type the text in English using [MASK] (as shown below):",
    "I study economics at [MASK].",
)
run_button = st.button(label="Run")

if run_button:
    with st.spinner("Wait for it..."):
        time.sleep(5)

        text = model(inp)
    st.balloons()
    st.success("Possible variants for the sentence:")
    for el in text:
        st.write(el["sequence"])
