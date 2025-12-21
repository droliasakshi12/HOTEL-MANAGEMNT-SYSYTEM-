import streamlit as st
import pymysql 

db=pymysql.connect(host="localhost",user="root",password="",database="sakshi_hotel_management_system")
cursor=db.cursor()

class login:
    def __init__(self):
        username=st.text_input(label="USERNAME",placeholder="enter your username here")
        password=st.text_input(label="PASSWORD",placeholder="enter your password here",type="password")

        guest_login_button=st.button(label="GUEST LOGIN")
        if guest_login_button:
            self.user_login(username,password)


    
    def user_login(self,username,password):
        user="SELECT * FROM guest where username=%s and password=%s"

        try:
            cursor.execute(user,(username,password))
            db.commit()
            fetch=cursor.fetchone()
            if fetch:
                st.switch_page("pages/check_room.py")
            

        except Exception as e :
            st.error(f"error {e}")
            db.rollback()

obj=login()