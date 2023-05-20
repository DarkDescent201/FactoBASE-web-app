#### Import Modules ####
import streamlit as st
import smtplib
import ssl
from email.message import EmailMessage




#### Global Objects ####
SENDER = "factobase@gmail.com"
RECEIVER = "factobase@gmail.com"
PASSWORD = "imoelxiwffffjvks"

HOST = "smtp.gmail.com"
PORT = 465
SSL_CONTEXT = ssl.create_default_context()

emotion_list = ["Great!", "Decent", "Meh", "Confused", "Very Angry", "Other"]




#### Define Functions ####
def send_email(message):
    gmail = smtplib.SMTP_SSL(host=HOST, port=PORT,
                             context=SSL_CONTEXT)
    gmail.login(SENDER, PASSWORD)
    gmail.send_message(message, SENDER, RECEIVER)
    gmail.quit()




#### Site Layout ####
st.set_page_config(page_title="Please, someone", page_icon=":four:", layout="wide")
colA, colB, colC = st.columns([3, 1, 1], gap="large")
with colA:
    st.title(":blue[Contact Me]")
    st.write("I mean, if you want to.")
with colC:
    st.image("FactoLOGO.png", width=75)

with st.form(key="form"):
    col1, col2 = st.columns(2, gap="large")
    with col1:
        first_name = st.text_input("First Name:", help="If you feel like it.",
                                   value="Human")
    with col2:
        last_name = st.text_input("Last Name:", help="It's totally optional.",
                                  value="Being")
    user_email = st.text_input("Your email address please.  Accuracy preffered but not required.",  help="Unless you want a response, of course.")
    feeling = st.selectbox("How are you today?", emotion_list,
                           help="I'm just curious.")
    subject_line = st.text_input("What would you like to talk about?",
                                 help="Hint: this is the subject line.")
    raw_message = st.text_area("Your message goes here.  It could be important.",
                               help="You never know.")
    attachments = st.file_uploader("Do you want to send me anything?", help="Well?  Do you?", accept_multiple_files=True)
    button = st.form_submit_button("All Done?", help="Only if you're sure...")

    if button:
        email_message = EmailMessage()
        email_content = str(raw_message+f"\n\nThey can be reached at {user_email}")
        email_message.set_content(email_content)
        email_message["Subject"] = subject_line if subject_line else "No subject"
        email_message["from"] = user_email
        email_message["to"] = RECEIVER
        if attachments:
            for attachment in attachments:
                name = attachment.name
                type = attachment.type
                main_type, sub_type = type.split('/', 1)
                print('\n\n', name, type, main_type, sub_type, '\n\n')
                email_message.add_attachment(attachment.read(), maintype=main_type,
                                             subtype=sub_type, filename=name)

        send_email(email_message)