Real Estate Listing System
This is a Python-based real estate listing system with authentication and email notification features. The system allows users to sign up, log in, create land listings, and receive email notifications when new listings are added.

Features
User Authentication: Users can sign up for an account and log in securely.
CRUD Operations: Users can create, read, update, and delete land listings.
Email Notifications: HR department receives email notifications when new land listings are added.
Prerequisites
Before running the application, ensure you have the following installed:

Python 3.x
SQLite (for database)
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/gilly7/real-estate-listing-system.git
Navigate to the project directory:
sql
Copy code
cd real-estate-listing-system
Install dependencies (if any):
Copy code
pip install -r requirements.txt
Usage
Initialize the database by running:
Copy code
python initialize_database.py
Run the main script:
Copy code
python login_system.py
Follow the on-screen instructions to sign up, log in, and create land listings.
Configuration
SMTP Server: Update the SMTP server address, port, email address, and password in login_system.py to enable email notifications.
Email Recipient: Update the recipient email address in login_system.py to specify where new listing notifications should be sent.
License
This project is licensed under the MIT License.

