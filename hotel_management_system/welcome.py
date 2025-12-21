import streamlit as st 
import pymysql 

db=pymysql.connect(host="localhost",user="root",password="",database="sakshi_hotel_management_system")
cursor=db.cursor()
select=st.selectbox("GUEST",("GUEST"))

left,right=st.columns(2)

with left:
    guest_login_button=st.button(label="GUEST LOGIN")
    if guest_login_button:
        st.switch_page("pages/guest_login.py")


with right:
    signup_button=st.button(label="GUEST SIGNUP")
    if signup_button:
        st.switch_page("pages/guest_signup.py")


    

