from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import openai
from PIL import Image

image = Image.open('producttoer.jpeg')
st.set_page_config(
        page_title="Berend-Botje Skills",
        page_icon="👋",
        layout="wide",
        initial_sidebar_state="collapsed"
)

col1, col2 = st.columns(2)

with col1:
    st.header("📖Berend-Botje Skills" )
    st.subheader("De ChatGPT kloon\n*waarom zou je moeilijk doen ....?*")
with col2:
   st.image(image, caption=None, width=240, use_column_width=True, clamp=True, channels="RGB", output_format="auto")

openai.api_key = st.secrets["OPENAI_API_KEY"]

