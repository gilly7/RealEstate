import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            name TEXT,
            email TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS land_listings (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            price REAL,
            contact_email TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to create a new user
def create_user(username, password, name, email):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        print("Username already exists. Please choose a different username.")
    else:
        cursor.execute('''
            INSERT INTO users (username, password, name, email)
            VALUES (?, ?, ?, ?)
        ''', (username, password, name, email))
        conn.commit()
        print("User created successfully.")
    conn.close()

# Function to authenticate user
def login(username, password):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Function to send email
# Function to send email
# Function to send email
def send_email(subject, body):
    sender_email = 'ngenogilbert254@example.com'
    receiver_email = 'hr@username.co.ke'
    password = 'ngeno@4real77'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    body = body

    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())



# Function to create a new land listing
def create_listing(title, description, price, contact_email):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO land_listings (title, description, price, contact_email)
        VALUES (?, ?, ?, ?)
    ''', (title, description, price, contact_email))
    conn.commit()
    conn.close()
    send_email("New Land Listing Created", f"Title: {title}\nDescription: {description}\nPrice: {price}\nContact Email: {contact_email}")

# Initialize the database
initialize_database()

# Sign up process
def sign_up():
    print("Welcome! Please sign up.")
    username = input("Enter your desired username: ")
    password = input("Enter your password: ")
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    create_user(username, password, name, email)

# Sign up or login
while True:
    choice = input("Do you want to (1) sign up or (2) log in? ")

    if choice == '1':
        sign_up()
    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user = login(username, password)
        if user:
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Create land listing
title = input("Enter title of land listing: ")
description = input("Enter description of land listing: ")
price = float(input("Enter price of land listing: "))
contact_email = input("Enter contact email for land listing: ")
create_listing(title, description, price, contact_email)
