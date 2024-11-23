import streamlit as st
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost", 
            user="root",  
            password="root", 
            database="anuj_db" 
        )
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None

def insert_data(name, email, password):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, password))
            connection.commit()
            st.success("Data inserted successfully!")
        except Error as e:
            st.error(f"Error inserting data: {e}")
            st.write("Debugging details:", e)
        finally:
            cursor.close()
            connection.close()
    else:
        st.error("Failed to connect to the database.")


st.title("Data Entry Form")

name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
password = st.text_input("Enter your password", type="password")  # Mask the password input

if st.button("Submit"):
    if name and email and password:
        insert_data(name, email, password)
    else:
        st.warning("Please fill in all fields.")
