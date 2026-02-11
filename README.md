
# University Placement Assistant (up assistant)

A web-based system built to simplify the student university placement process.
Originally developed in high school to replace manual paper submissions and Excel-based workflows used by IT departments.

## Features

* **Student Portal:** Search and select preferred universities, view details, and submit choices online.
* **Admin Dashboard:** Import student lists from Excel, monitor submissions, and export final placement data.
* **Automation:** Generates ready-to-submit Excel files for ministry upload.
* **Error Prevention:** Eliminates mismatched or missing student choices through digital verification.

## Setup and Installation(linux/ubuntu)

1. **Create a virtual environment**

   ```bash
   python3 -m venv .venv
   ```

2. **Activate the virtual environment**

   ```bash
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Once setup is complete, start the app with:

### local test
```bash
gunicorn app:app --bind 0.0.0.0:5000 --workers 3
```

### production
```bash
gunicorn app:app --bind 0.0.0.0:$PORT --workers 3
```


Here’s a cleaner and more readable version of your section while keeping your original tone and intent:

---

## 🚀 Usage (Local Test URLs)

1. **Login as Admin**
   Go to:
   👉 `http://{domain}:{port}/admin`

   ```
   username: upadmin  
   password: upadmin123  
   ```

2. **Get a Sample Student**
   From the admin panel, copy any sample student’s full name and ID.

3. **Login as Student**
   Visit:
   👉 `http://{domain}:{port}/login/student/`
   Use the copied full name and ID to log in and explore the student portal.






## 💡 About

This project was built from a real-world need to fix inefficient university placement workflows in my school. It’s a reminder that innovation doesn’t need fancy tools i just built it by using flask and jquery — just a clear problem and the will to solve it.
