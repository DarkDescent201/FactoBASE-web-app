#### Import Modules ####
import streamlit as st
import FactoBASE




#### Global Objects ####
status = 0




#### Define Functions ####
def base_to_base(userNum, baseNum, baseDes):
    userNum = str(userNum)
    baseNum = str(baseNum)
    baseDes = str(baseDes)
    dec = FactoBASE.numbase_to_decimal(baseNum, userNum)
    desLen = FactoBASE.find_numbase_length(baseDes, dec)
    desired = FactoBASE.decimal_to_numbase(dec, baseDes, desLen)
    return dec, desLen, desired




#### Page Layout ####
st.set_page_config(page_title="Convert something!", page_icon=":one:", layout="wide")

colA, colB, colC = st.columns([3, 1, 1], gap="large")
with colA:
    st.title(":blue[Convert from Base(x) to Base(y)]")
with colC:
    st.image("FactoLOGO.png", width=75)
st.write("Give me a number and tell me its base-number, and I'll convert it to any base-number you desire for you.  I'll even give you the decimal representation and the length for free.  If you don't provide a base number, I'll just assume it's 10.")

col1, col2, col3 = st.columns(3, gap="large")
with col1:
    st.title("")
    st.text("What is your number?")
    st.title("")
    st.write("")
    st.text("What base is it in?")
    st.title("")
    st.write("")
    st.text("And what base do you desire?")
with col2:
    user_num = st.number_input("Well, what is it?", min_value=0, step=1,
                               help="I can't wait to find out!")
    user_base = st.number_input("Is this your base?", min_value=0, step=1, 
                                help="I knew it!")
    desired_base = st.number_input("Now that's a nice base", min_value=0, step=1,
                                   help="I couldn't have done better myself.")
    if user_base < 1:
        user_base = 10
    if desired_base < 1:
        desired_base = 10
with col3:
    st.title(" ")
    button_press = st.button(label="Calculate", help="This is hard work, you know.")
    if button_press:
        dec_num, desired_len, desired_num = base_to_base(user_num, user_base, 
                                                         desired_base)

col4, col5 = st.columns([1, 2], gap="large")
with col4:
    if button_press:
        st.title(" ")
        st.title(" ")
        st.text(f"Your extra special Base-{desired_base} result is:")
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
        st.text(desired_num if desired_num else 0)
        st.subheader(" ")
        st.text(desired_len if desired_len else 1)
        st.subheader(" ")
        st.text(dec_num)
        st.subheader(" ")
        st.text(len(dec_num))