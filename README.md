# Contact Manager Web App
A simple web application to manage your personal contacts — including adding, updating, deleting, and searching through contacts.
Built using Flask, SQLite, and Bootstrap, and deployed on Render.


##  Features
-Add new contacts
-Edit existing contacts
-Delete contacts
-Search contacts by name, email, phone, or address
-Responsive and clean UI
-Gradient header and glowing title
-Auto-created SQLite database

##  How to Use

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/sravanipotteti/contact-manager.git
   cd contact-manager
    ```
2.**Create and activate a virtual environment:**

  ```nginx
  python -m venv venv
  venv\Scripts\activate    # On Windows

  ```
3.**Install dependencies:**
  ```nginx
  pip install -r requirements.txt
```
4.**Initialize the database:**
  ```nginx
  python init_db.py
```
5.**Run the app:**
  ```nginx
  python app.py
```
6.**Open your browser and visit:**
  ```bash
  http://127.0.0.1:5000
```

##Commands

| Command | Usage Example | Description |
|---------|----------------|-------------|
| `run` | `python app.py` | Starts the Contact Manager web application |
| `init-db` | `python init_db.py` | Creates the SQLite database and contacts table |
| `add` | Use the “Add Contact” button on the UI | Adds a new contact |
| `edit` | Use the “Edit” button on any contact | Updates an existing contact |
| `delete` | Use the “Delete” button on any contact | Deletes a selected contact |
| `search` | Visit `/?q=keyword` | Searches contacts by keyword (name, email, phone, address) |


##Contact Storage
All contact data is stored in a SQLite database named:
```bash
contacts.db
```

On Render deployment, this database is automatically created using:
```bash
init_db.py  +  schema.sql
```

##Requirements
-Python 3.x
-Flask
-Gunicorn (for deployment)
-SQLite (built-in)


##Install all dependencies using:
```bash
pip install -r requirements.txt
```

##Deployment

This project is deployed on Render using:

-Procfile for Gunicorn
-Automatic build + deploy
-HTTPS enabled by default

##Live site link:
Check out the project's [Live Demo](https://contact-manager-kqub.onrender.com/)

##Project Structure
contact-manager/
│ app.py
│ db.py
│ init_db.py
│ schema.sql
│ requirements.txt
│ Procfile
│
├── templates/
│     base.html
│     list_contacts.html
│     add_contact.html
│     edit_contact.html
│
└── static/
      styles.css

##Author
Build By Sravani Potteti
Full Stack Developer • Python • Flask • Web Apps





