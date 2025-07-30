import streamlit as st
import re
from sql_connection import crsr,con


def logout():
   st.session_state.check_v=False
   st.session_state.class1=""
   st.session_state.Roll_no=""
   st.session_state.email=""
   st.rerun()

if "check_v"  not in st.session_state:
    st.session_state.check_v=False

if "Roll_no" not in st.session_state:
    st.session_state.Roll_no= ""

if st.session_state.check_v:
    
    st.write( f"Roll no. {st.session_state.Roll_no} from {st.session_state.class1} , You are already Login....")
    st.write("click on Log out to exit..")
    if st.button("Logout"):
       logout()
else:
      
   st.title("👉 Login  from here")
   col3,col4=st.columns(2)
   with col3:
    class1=st.text_input("Enter Your Class:")

   with col4:
    Roll_no=st.text_input("Enter Your Roll No. :") 
   email=st.text_input("Login With email 📧:")


# syntax=r"[a-z]+[0-9]*[a-z]*[@][a-z]{5}[.][a-z]{3}"

   btn2=st.button("Log in")
   if btn2:
  
      if  email=="" or class1==""or Roll_no=="":
         st.error("enter all fields")
      else:
          student=crsr.execute(f"select * from signup where Roll_no='{Roll_no}' and class1='{class1}' and email='{email}'")
          check=crsr.fetchone()
          
    #    st.write(check)
          if check is  None:
             st.warning("student  not exist")
             
          else:
             st.session_state.check_v=True
             
             st.session_state.class1=check[2]
             st.session_state.Roll_no=check[3]
             st.session_state.email=check[5]
             st.write(f"congrats ,Succesfull login {check[0]+" "+check[1]}")   
             st.write(check)
             st.rerun()
           


  

       
      
