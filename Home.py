#### Import Modules ####
import streamlit as st
import time
from datetime import datetime
from random import randrange as rnd




#### Generate Global Objects ####
with open("Intro.txt") as file1:
    intro_text = file1.read()
with open("HowItWorks.txt") as file2:
    explain_text = file2.read()
image_path = "FactoLOGO.png"
facto_list = [0, 1, 10, 11, 20, 21, 100, 101, 110, 111, 120, 121, 200, 
              201, 210, 211, 220, 221, 300, 301, 310, 311, 320, 321]
        



#### Page Layout ####
st.set_page_config(page_title="Welcome to FactoBASE!", page_icon=":exclamation:", layout="wide")
col1, col2, col3 = st.columns(3, gap="large")
with col1:
    st.title(":blue[FactoBASE!]")
with col2:
    i = rnd(24)
    if i < 6:
        color = "green"
    elif 6 < i < 12:
        color = "blue"
    elif 12 < i < 18:
        color = "violet"
    else:
        color = "red"
    sentence = f":{color}[{i}  =  {facto_list[i]}]"
    st.title(sentence)
with col3:
    st.image(image_path, width=110)
st.subheader(":blue[Introduction]")
st.write(intro_text)
st.subheader(":blue[An Insufficient Explanation]")
st.write(explain_text)
