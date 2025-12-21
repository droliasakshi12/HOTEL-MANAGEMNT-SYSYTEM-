import streamlit as st
import pymysql 

db=pymysql.connect(host="localhost",user="root",password="",database="sakshi_hotel_management_system")
cursor=db.cursor()


class signup:
    def __init__(self):
        name=st.text_input(label="GUEST NAME",placeholder= "enter your name")
        contact=st.text_input(label="CONTACT",placeholder="enter your contact")
        email=st.text_input(label="EMAIL ID ",placeholder="enter your email is here")
        dob=st.date_input(label="DATE OF BIRTH")
        address=st.text_input(label="ADDRESS" , placeholder="enter your address here ")
        username=st.text_input(label="USERNAME",placeholder="create your username here")
        password=st.text_input(label="PASSWORD",placeholder="enter your password here")

        signup_button=st.button(label="GUEST SIGNUP")
        if signup_button:
            self.guest_signup(name,contact,email,dob,address,username,password)
            st.success("you have successfully signed up !!")

            login_button=st.button(label="LOGIN")
            if login_button:
                st.switch_page("pages/guest_login.py")

    


    def guest_signup(self,name,contact,email,dob,address,username,password):
        insert_guest="INSERT INTO guest(name,contact,email,date_of_birth,address,username,password) VALUES(%s,%s,%s,%s,%s,%s,%s)"

        try:
            cursor.execute(insert_guest,(name,contact,email,dob,address,username,password))
            db.commit()
        
        except Exception as e :
            st.error(f"error {e}")
            db.rollback()



obj=signup()