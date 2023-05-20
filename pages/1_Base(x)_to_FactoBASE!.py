#### Import Modules ####
import streamlit as st
import FactoBASE




#### Global Objects ####
status = 0




#### Define Functions ####
def base_to_facto(userNum, baseNum):
    userNum = str(userNum)
    baseNum = str(baseNum)
    dec = FactoBASE.numbase_to_decimal(baseNum, userNum)
    factoLen = FactoBASE.find_factobase_length(dec)
    facto = FactoBASE.decimal_to_factobase(dec, factoLen)
    return dec, factoLen, facto




#### Page Layout ####
st.set_page_config(page_title="Convert something!", page_icon=":two:", layout="wide")

colA, colB, colC = st.columns([3, 1, 1], gap="large")
with colA:
    st.title(":blue[Convert from Base(x) to FactoBASE!]")
with colC:
    st.image("FactoLOGO.png", width=75)
st.write("Give me a number and tell me its base-number, and I'll convert it to FactoBASE! for you.  I'll even give you the decimal representation and the length for free.  If you don't provide a base number, I'll just assume it's 10.")

col1, col2, col3 = st.columns(3, gap="large")
with col1:
    st.title("")
    st.text("What is your number?")
    st.title("")
    st.write("")
    st.text("What base is it in?")
with col2:
    user_num = st.number_input("Gimme nums", min_value=0, step=1,
                               help="Letters are not allowed.")
    user_base = st.number_input("Feel the base", min_value=0, step=1, 
                                help="... You tried it didn't you?")
    if user_base < 1:
        user_base = 10
with col3:
    st.title(" ")
    button_press = st.button(label="Calculate", help="I wouldn't recommend it.")
    if button_press:
        dec_num, facto_len, facto_num = base_to_facto(user_num, user_base)

col4, col5 = st.columns([1, 2], gap="large")
with col4:
    if button_press:
        st.title(" ")
        st.title(" ")
        st.text("Your FactoBASE! result is:")
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
        st.text(facto_num if facto_num else 0)
        st.subheader(" ")
        st.text(facto_len if facto_num else 1)
        st.subheader(" ")
        st.text(dec_num)
        st.subheader(" ")
        st.text(len(dec_num))