import streamlit as st
import pymysql
import connectmysql as con

st.title("CRUD MySQL App with Streamlit")
connection = con.connectdb()
cursor = connection.cursor()


def read_person():
    cursor.execute("select * from person order by id desc")
    persons = cursor.fetchall()
    return persons


def create_person(fullname="", email="", age=0):
    try:
        cursor.execute(
            "insert into person(fullname ,email ,age)values (%s,%s,%s)", (
                fullname, email, age)
        )
        connection.commit()
        st.success("บันทึกข้อมูลเรียบร้อย")
    except pymysql.Error:
        st.error(f'เกิดข้อผิดพลาด:{pymysql.Error}')


def update_person(id=0, fullname="", email="", age=0):
    try:
        cursor.execute(
            " update person set fullname = %s,email = %s,age= %s where id =%s", (
                fullname, email, age, id)
        )
        connection.commit()
        st.success("อัพเดทข้อมูลเรียบร้อย")
    except pymysql.Error:
        st.error(f'เกิดข้อผิดพลาด:{pymysql.Error}')


def delete_person(id=0):
    try:
        cursor.execute(
            "delete from person where id =  %s", (id)
        )
        connection.commit()
        st.success("ลบข้อมูลเรียบร้อย")
    except pymysql.Error:
        st.error(f'เกิดข้อผิดพลาด:{pymysql.Error}')


menu = ["Home", "Insert", "Update", "Delete"]

choice = st.sidebar.selectbox("Menu", menu)
# เมื่อผู้ใช้เลือกเมนู
if choice == "Home":
    st.write("### Person List")
    persons = read_person()
    table_data = []
    if persons:
        for person in persons:
            row = person
            table_data.append(row)
        st.table(table_data)

    else:
        st.write("## ยังไม่มีข้อมูลในตาราง Person")

elif choice == "Insert":
    st.write("## Add new Person")
    fullname = st.text_input("Fullname")
    email = st.text_input("email")
    age = st.number_input("Age", 1, 100, 1)

    if st.button("Create"):
        if fullname and email and age:
            create_person(fullname, email, age)

        else:
            st.warning("กรุณากรอกข้อมูลให้ครบถ้วน")

elif choice == "Update":
    st.write("## Update new Person")
    id = st.number_input("ID", 1, 100, 1)
    fullname = st.text_input("Fullname")
    email = st.text_input("email")
    age = st.number_input("age", 1, 100, 1)

    if st.button("Update"):
        if fullname and email and age:
            update_person(id, fullname, email, age)

        else:
            st.warning("กรุณากรอกข้อมูลให้ครบถ้วน")

elif choice == "Delete":
    st.write("## Delete new Person")
    id = st.number_input("ID", 1, 100, 1)

    if st.button("Delete"):
        if id:
            delete_person(id)

        else:
            st.warning("กรุณากรอกข้อมูลให้ครบถ้วน")
