🧑‍🏫 Teacher-Student Repository

A Django-based web application designed to help teachers manage student academic and extracurricular data efficiently. Users can securely register/login, add new student records, and categorize entries based on various filters like internship, placement, CGPA, achievements, and more.

⸻

🚀 Features
	•	🔐 Authentication System – Secure login and registration system
	•	📝 CRUD Operations – Create, read, update, and delete student records
	•	🔍 Dynamic Filters – Filter records by category (Internship, Placement, etc.)
	•	🔄 Sync Records – Option to sync updated records (simulated for UI)
	•	📂 File Uploads – Upload and attach achievements and related documents

⸻

🖼️ Screenshots

🔐 Register Page

![Screenshot 2025-05-17 at 7 47 47 PM](https://github.com/user-attachments/assets/e298497a-7492-456e-b73a-81747ccf1543)

📥 Dashboard View

![Screenshot 2025-05-17 at 7 48 08 PM](https://github.com/user-attachments/assets/b9b2fd1a-2964-4cd6-bf1b-d2b3e37d9e58)

📄 Record Details Model

![Screenshot 2025-05-17 at 7 48 26 PM](https://github.com/user-attachments/assets/ee21180e-c45a-4856-ac60-9349e4c74cc4)



⸻

🛠️ Tech Stack
	•	Backend: Python, Django
	•	Frontend: HTML, CSS, Bootstrap
	•	Database: SQLite
	•	Others: JavaScript, Google Sheets API

⸻

🧰 Setup Instructions
	1.	Clone the repository

git clone https://github.com/AllGunsBlazing/Teacher_Student_Repo.git
cd Teacher_Student_Repo


	2.	Create and activate virtual environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


	3.	Install dependencies

pip install -r requirements.txt


	4.	Run migrations

python manage.py makemigrations
python manage.py migrate


	5.	Create a superuser (for admin access)

python manage.py createsuperuser


	6.	Run the development server

python manage.py runserver


	7.	Access the site
	•	Open http://127.0.0.1:8000

⸻

📁 Folder Structure

<pre>
```

teacher_student_repo/
├── screenshots/
│   ├── register.png
│   ├── dashboard.png
│   └── record-detail.png
├── myproject/                # (your Django project folder)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── studentapp/              # (your Django app folder)
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── static/
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
  
```
</pre>
⸻

📜 License

This project is licensed under the MIT License – see the LICENSE file for details.

Thank You!
