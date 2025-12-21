import streamlit as st 
import pymysql 

db=pymysql.connect(host="localhost",user="root",password="",database="sakshi_hotel_management_system")
cursor=db.cursor()


class room:
    def __init__(self):
        check_button=st.button(label="CHECK ROOM OPTIONS")
        if check_button:
            self.check_room()
        
        book_room=st.button(label="BOOK ROOM")
        if book_room:
            st.switch_page("pages/book_room.py")


    def check_room(self):
        select="SELECT * FROM room"
        try:
            cursor.execute(select)
            db.commit()
            fetch_room=cursor.fetchall()
            for i in fetch_room:
                  st.table(i)

        except Exception as e :
            st.error(f"error {e}")
            db.rollback()


    
   
obj=room()