import streamlit as st
import pandas as pd
import numpy as np



st.title('aurorae cerebrum')


title = st.text_input('search')


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}


	    a {visiblity: hidden;}



            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.set_page_config(page_title='aurorae cerebrum', page_icon=””)
