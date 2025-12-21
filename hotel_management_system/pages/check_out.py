import streamlit as st 
import pymysql


db=pymysql.connect(host="localhost",user="root",password="",database="sakshi_hotel_management_system")
cursor=db.cursor()


class check:
      def __init__(self):
            rid=st.number_input(label="ROOM NUMBER",placeholder="enter your room number here")
            avail_button=st.button(label="CHECK OUT")
            if avail_button:
                self.room_available(rid)
                st.success("check out successfully!!")



      def room_available(self,rid):
        room_update="update room set room_available ='available' where room_number =%s"

        try:
            cursor.execute(room_update,(rid))
            db.commit()
           
        except Exception as e:
            st.error(f"error {e}")
            db.rollback()
           
                    
obj=check()