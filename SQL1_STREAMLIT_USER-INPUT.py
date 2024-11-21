import streamlit as st
import mysql.connector
from mysql.connector import Error

# Function to establish a connection with MySQL
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your MySQL host
            user="root",  # Replace with your MySQL username
            password="root",  # Replace with your MySQL password
            database="anuj_db"  # Replace with your database name
        )
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None

# Function to insert data into the database
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

# Streamlit interface
st.title("Data Entry Form")

# Input fields
name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
password = st.text_input("Enter your password", type="password")  # Mask the password input

# Submit button
if st.button("Submit"):
    if name and email and password:
        insert_data(name, email, password)
    else:
        st.warning("Please fill in all fields.")
