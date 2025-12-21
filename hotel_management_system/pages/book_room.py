import streamlit as st 
import pymysql


db=pymysql.connect(host="localhost",user="root",password="",database="sakshi_hotel_management_system")
cursor=db.cursor()

class book_room:
    def __init__(self):

        room_no=st.number_input(label="ROOM NUMBER",placeholder="enter room number here")
        rid="select room_id from room where room_number=%s"
        cursor.execute(rid,(room_no))
        db.commit()
        fetch_rid=cursor.fetchone()
        

        name=st.text_input(label="GUEST NAME",placeholder="enter guest name here")
        gid="select guest_id from guest where name=%s"
        cursor.execute(gid,(name))
        db.commit()
        fetch_gid=cursor.fetchone()
        

        check_in=st.date_input(label="CHECK IN DATE")
        check_out=st.date_input(label="CHECK OUT DATE")


        self.update_room(room_no)
        


        book_room_button=st.button(label="BOOK ROOMS")
        if book_room_button:
            self.bookroom(fetch_rid[0],fetch_gid[0],check_in,check_out)
            st.success("room booked successfully!!")
        
        avail_button=st.button(label="CHECK OUT")
        if avail_button:
            st.switch_page("pages/check_out.py")
           



    def bookroom(self,fetch_rid,fetch_gid,check_in,check_out):
        room_booking="INSERT INTO room_bookings(room_id , guest_id , check_in , check_out) VALUES(%s,%s,%s,%s)"
        try:
            cursor.execute(room_booking,(fetch_rid,fetch_gid,check_in,check_out))
            db.commit()
            
        except Exception as e:
            st.error(f"error {e}")
            db.rollback()



    def update_room(self,room_no):
        update="update room set room_available='not available' where room_number=%s"
        try:
            cursor.execute(update,(room_no))
            db.commit()
        except Exception as e:
            st.error(f"error {e}")
            db.rollback()



    


    
      

        












obj=book_room()