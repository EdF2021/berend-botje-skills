# Run: streamlit run streamlit_app.py

import os
import streamlit as st
from PIL import Image
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

import openai

try:
    openai_api_key = os.getenv("OPENAI_API_KEY")
except Exception:
    openai_api_key = st.secrets["OPENAI_API_KEY"]


image = Image.open("images/producttoer.jpeg")
ENCODINGS = "cl100k_base"

st.set_page_config(
    page_title=":genie:Berend-Botje Skills",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://mboscrum.com/mbowoordle",
        "Report a bug": "https://mboscrum.com/mbowoordle",
        "About": "# Berend in development -  een *extremely* cool app!",
    },
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(" ### :genie::infinity: Welkom bij Berend-Botje ### ")
    st.markdown(
        """ ##### Berend-Botje is een slimme AI assistent met skills die perfect aansluiten bij het **Smart Working principle** """
    )
    st.markdown(
        """ ###### Berend-Botje Basis:male_mage:, een soort van ChatGPT kloon, staat altijd voor je klaar om snel je vragen te beantwoorden. Heb je behoefte aan hulp bij een specifieke taak, dan vraag je Berend om de bijpassende Skills voor je in te pluggen. 
    **Jij kiest op basis van je klus de bijpassende Berend Bot.**  
    :rotating_light: Belangrijk voordeel van het gebruik van Berend-Botje is dat al jouw informatie binnen jouw omgeving blijft!  *Nadat een sessie wordt afgesloren blijft er dus geen informatie achter die door ons noch door derden gebruikt kan worden!*
    >> De skills zijn **Powered By OpenAI models**.
    ------------------------------------ """
    )

with col2:
    st.image(
        image,
        caption=None,
        use_column_width=True,
        clamp=True,
        channels="RGB",
        output_format="auto",
    )
    # st.sidebar.success("Kies één van Berend's skills")
    st.markdown(
        """ ##### Voorbeelden
    **1. [De Lesplanner](Lesplan_Demo)**
    **2. [De Notulist](Mapping_Demo)**
    **3. [De Dataanalist](DataFrame_Demo)**
    **4. [De Datavormgever](Plotting_Demo)**
    **5. [De Chatbot](Chat_Demo)**
    **6. [De Samenvatter](Samenvatter_Demo)**
    """
    )
st.markdown(":red:[:genie: Berend Basis ChatBot]")
# NIEUW
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(
        {"role": "system", "content": "Geef altijd antwoord in het Nederlands"}
    )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] != "system":
            st.markdown(message["content"])

if prompt := st.chat_input("Hoe gaat het?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

st.markdown(
    """
    :angel: :gray[ *Disclaimer Aan het gebruik, of resultaten van Berend-Botje Skills kunnen geen rechten worden verleend. Noch zijn wij aansprakelijk voor enig gevolg van dit gebruik. Bedenk dat de voorbeelden die hier getoond worden nog in een premature fase verkeren: het is werk onder constructie...* ]
    """
)
