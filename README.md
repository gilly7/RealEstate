Flask Real Estate Application
This is a simple Flask application for managing real estate listings. Users can sign up, log in, create land listings, and browse the catalog.

Features
User authentication: Sign up, log in, and log out functionality.
CRUD operations for managing land listings.
Email notifications for new land listings.
Simple user interface for browsing listings.
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/gilly7/RealEstate.git
Navigate to the project directory:

bash
Copy code
cd flask-real-estate
Install the required dependencies:

Copy code
pip install -r requirements.txt
Run the Flask application:

arduino
Copy code
python run.py
Access the application in your web browser at http://localhost:5000.

#Usage
Register a new account using the sign-up form.
Log in with your credentials.
Create new land listings from the dashboard.
Browse existing listings in the catalog.
Log out when done.
Configuration
The application uses a SQLite database by default. You can change the database configuration in app/__init__.py.
Configure email settings in app/utils.py for sending notifications.
Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

