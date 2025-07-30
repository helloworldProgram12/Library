import streamlit as st
from sql_connection import crsr,con
st.header("📚Book Record...")

if "check_v"  not in st.session_state:
    st.session_state.check_v=False

if "Roll_no" not in st.session_state:
    st.session_state.Roll_no= ""

if st.session_state.check_v:
    st.subheader(f"{st.session_state.email}")
    Serial_no = st.text_input("Enter Serial no. of Book:")
    Title=st.text_input("Enter Book Title")
    Writer = st.text_input("Enter Writer of Book:")
    btn2=st.button("Add")
    if btn2:
        if  Serial_no=="" or Title=="" or Writer=="":
             st.warning("⚠️ Please fill all fields.")
        else:    
            try:   
              crsr.execute("INSERT INTO books (Roll_no, Serial, Title, Writer) VALUES (%s, %s, %s, %s)",(st.session_state.Roll_no,Serial_no, Title, Writer) )
              already_serial=crsr.execute("select serial_no from books ")
              con.commit()
              st.success(f"'{Title}' has been added to your library.")
              st.rerun()
            except Exception as e:
                if "Duplicate entry" in str(e) and "Serial" in str(e):
                      st.error(f"⚠️ A book with Serial No '{Serial_no}' already issued.")
           
                # print(str(e))
                # if e==1062 (23000):
                    #  st.write("book issued by other student")

    st.subheader("📖 Books Issued by You...")
    crsr.execute("SELECT * FROM books WHERE Roll_no = %s", (st.session_state.Roll_no,))
    all_books = crsr.fetchall()

    for i, book in enumerate(all_books):
        roll_no, serial, writer, title = book  

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write(serial)
        with col2:
            st.write(title)
        with col3:
            st.write(writer)
        with col4:
            if st.button("🗑️ Delete", key=f"delete_{serial}_{i}"):
                try:
                    crsr.execute("DELETE FROM books WHERE Serial = %s AND Roll_no = %s", (serial, st.session_state.Roll_no))
                    con.commit()
                    st.success(f"'{title}' has been deleted.")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error deleting book: {e}")



