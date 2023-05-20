#### Import Modules ####
import streamlit as st
import FactoBASE




#### Global Objects ####
status = 0




#### Define Functions ####
def facto_to_base(userNum, baseNum):
    userNum = str(userNum)
    baseNum = str(baseNum)
    dec = FactoBASE.factobase_to_decimal(userNum)
    baseLen = FactoBASE.find_numbase_length(baseNum, dec)
    base = FactoBASE.decimal_to_numbase(dec, baseNum, baseLen)
    return dec, baseLen, base




#### Page Layout ####
st.set_page_config(page_title="Convert something!", page_icon=":three:", layout="wide")

colA, colB, colC = st.columns([3, 1, 1], gap="large")
with colA:
    st.title(":blue[Convert from FactoBASE! to Base(x)]")
with colC:
    st.image("FactoLOGO.png", width=75)
st.write("Give me a FactoBASE! number and tell me your desired base-number, and I'll convert it for you.  I'll even give you the decimal representation and the length for free.  If you don't provide a base number, I'll just assume it's 10.")

col1, col2, col3 = st.columns(3, gap="large")
with col1:
    st.title("")
    st.text("What is your FactoBASE! number?")
    st.title("")
    st.write("")
    st.text("What base would you like your answer in?")
with col2:
    user_num = st.number_input("Gimme nums", min_value=0, step=1, 
                               help="It's not perfect.")
    user_base = st.number_input("Feel the base", min_value=0, step=1, 
                                help="Think really hard.")
    if user_base < 1:
        user_base = 10
with col3:
    st.title(" ")
    button_press = st.button(label="Calculate", help="...are you sure about this?")
    if button_press:
        dec_num, base_len, base_num = facto_to_base(user_num, user_base)

col4, col5 = st.columns([1, 2], gap="large")
with col4:
    if button_press:
        st.title(" ")
        st.title(" ")
        st.text(f"Your personalized Base-{user_base} result is:")
        st.subheader(" ")
        st.text("Its length is:")
        st.subheader(" ")
        st.text("The base-10 form is:")
        st.subheader(" ")
        st.text("The base-10 length is:")
with col5:
    if button_press:
        st.title(" ")
        st.title(" ")
        st.text(base_num if base_num else 0)
        st.subheader(" ")
        st.text(base_len if base_len else 1)
        st.subheader(" ")
        st.text(dec_num)
        st.subheader(" ")
        st.text(len(dec_num))