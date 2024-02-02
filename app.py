import google.generativeai as genai
import os
import streamlit as st

genai.configure(api_key="AIzaSyCmDlamc5RplOiui_I0pM-Jj5qGD4ZGW40")

model = genai.GenerativeModel("gemini-pro")

def get_email( src, dest, subject, tone, about):
    prompt = "Write an email from{} to {}. Subject line is {}, Keep the E-mail {}. The email is ragarding{}.".format(src,dest,subject,tone,about) 
    response = model.generate_content(prompt)
    return response.text
    
print(get_email("student", "principal","leave for 3 days","formal","I cannot attend college for 3 days"))

st.set_page_config(
    page_title = "Email generator",
    page_icon = ":email:",
    layout = "centered",
    initial_sidebar_state = "collapsed"
)

st.header("Write emails like a professional")
st.write("Desribe the type of email you want. Gemini will write it for you.")

col1, col2 = st.columns(2)


with col1:
    src = st.text_input("Who is this E-mail from? E.g Student")
    subject = st.text_input("Subject")
with col2:
    dest = st.text_input("Who is email for? Eg.HOD" )  
    tone = st.selectbox("Choose the tone of your argument", ["Formal","Informal","Casual","Funny","Angry"])
    
about = st.text_area("What is the E-mail about?")

send_request = st.button("Generate E-mail")

if send_request:
    if src and subject and dest and tone and about:
        st.write(get_email(src, dest, subject, tone, about))
    else:
        st.error("Please fill all the fields.")
    
    