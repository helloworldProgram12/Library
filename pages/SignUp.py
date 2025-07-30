import streamlit as st
import re
from sql_connection import crsr,con
st.title("👉 Sign up from here")
# create column for first and last name
col1,col2=st.columns(2)
 
with col1:
    First=st.text_input("Enter Your First name:")

with col2:
    last=st.text_input("Enter Your Last name:")    

col3,col4=st.columns(2)
with col3:
    class1=st.text_input("Enter Your Class:")

with col4:
    Roll_no=st.text_input("Enter Your Roll No. :") 

phone=st.number_input("Enter Mobile Number:",min_value=1000000000)
email=st.text_input("Login With email 📧:")
btn1=st.button("Sign up")
# syntax to check the email pattern
syntax=r"[a-z]+[0-9]*[a-z]*[@][a-z]{5}[.][a-z]{3}"
if btn1:
     if First=="" or last=="" or class1=="" or Roll_no=="" or phone==" ":
        st.error("All Fields are mandatory,Fill them...")
     else:
         
        if re.match(syntax, email):
           try:
                crsr.execute(f"insert into signup(First,last,email,phone,Roll_no,class1)values('{First}','{last}','{email}','{phone}','{Roll_no}','{class1}')")
                con.commit()
                st.write("succesfully")
                st.markdown("[Go to Login](./Login)")
           except Exception as e:
              st.error("something wrong in your fieds")
        else:
            st.error("❌ Enter a valid Email")
            
         