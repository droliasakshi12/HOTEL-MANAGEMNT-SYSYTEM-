 # 🏨 Hotel Management System

 A simple **Python console application** for managing basic hotel operations like guest signup, login, room booking, room availability, and check-out.

This README explains what the project does, how to use it, and how others can contribute. A good README helps people understand your project quickly, and GitHub displays it automatically on the repo page.

---
### 🔗Prerequisites
- <b>Python version</b><br>
  -Python **3.8+** installed
- <b>IDE/Code Editor</b><br>
   -VS Code
 </br>

# 🖥️Tech Stack
- python

<h1>📑About the project</h1>
   <p>Hotel Management System is (GUI) based project using streamlit.<br>
    This includes Database connectivity.<br>
    It Includes Guest Signup and Login options<br>
    Here when user check in the room is updated to "not available"<br>
   </p>
   
### 📁Run File
<pre><code>welcome.py</code></pre>

### 📂Create a 'pages' folder which will include all the other .py files 
In pages folder below files will be included :
<p><pre>book_room.py<br>
check_out.py<br>
check_room.py<br>
guest_login.py<br>
guest_signup.py<br>
</pre></p>


## 📃welcome.py
#### 👩‍💻Code 

<pre>
 <code>

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
 </code>
</pre>
<br>


## 📗book_room.py
#### 👩‍💻Code 

<pre><code>
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
</code></pre>


## ☑️check_out.py
#### 👩‍💻Code
<pre>
 <code>
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
 </code>
</pre>

## 🏨check_room.py
#### 👩‍💻Code
<pre>
 <code>
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
 </code>
</pre>

## 👤guest_login.py
#### 👩‍💻Code

<pre>
 <code>
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
 </code>
</pre>

## 👤guest_signup.py
#### 👩‍💻Code

<pre>
 <code>
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
 </code>
</pre>

<b><p>⭐ If you found this repository useful, consider giving it a star!</p>
<p>Happy Coding 🐍✨</p></b>

👤 Github  : [@droliasakshi12](https://github.com/droliasakshi12)<br>
📩 Email   : sakshidrolia12@gmail.com <br>
🔗 Linkdin : https://www.linkedin.com/in/sakshi-drolia12<br>
<h4>Credits</h4>
<b></b>Future Vision Computer Institute</b><BR>
🌐 Website : https://futurevisioncomputers.com/
<br>
<b><h5>Author</h5></b>
<b>Sakshi Drolia</b>
