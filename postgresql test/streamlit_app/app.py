import streamlit as st
import mysql.connector

st.title("📊 MySQL Data Viewer")

conn = mysql.connector.connect(
    host="mysql-db",
    user="user",
    password="pass",
    database="testdb"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

st.write("Data from 'users' table:")
st.table(rows)

cursor.close()
conn.close()
