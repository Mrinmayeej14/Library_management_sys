Library Management System
Overview
The Library Management System is a multi-user application designed to streamline the management of books and user interactions within a library. It caters to two types of users: general users and administrators. The system provides a variety of features tailored to each user type, enhancing the overall library experience.

Features
General User
Request a Book: Users can request books they wish to borrow.
Read Book: Users can read the available books online.
Download Book: Users have the option to download books for offline reading.
Give Feedback: Users can provide feedback on books they have read.
View Book Details: Users can view detailed information about books.
Search for a Book: Users can search for books based on name, author, or genre.
Admin
Approve/Reject/Revoke Book Requests: Admins can manage user book requests.
Add/Remove/Edit Books/Genres: Admins have control over the book and genre catalog.
View Books/Genres: Admins can view the list of available books and genres.
View Issued Books: Admins can track books that have been issued to users.
Tech Stack
Frontend: HTML, CSS, Bootstrap
Backend: Python, Flask, SQLite, SQLAlchemy
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/library-management-system.git
Navigate to the project directory:
bash
Copy code
cd library-management-system
Set up a virtual environment and install dependencies:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
Set up the database:
bash
Copy code
python setup_database.py
Run the application:
bash
Copy code
python app.py
Usage
Access the application through your web browser at http://localhost:5000.
Sign up or log in as a general user or admin to access the respective features.
