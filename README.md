# University Placement Assistant (up assistant)

A web-based system built to simplify the student university placement process.
Originally developed in high school to replace manual paper submissions and Excel-based workflows used by IT departments.

## Features

* **Student Portal:** Search and select preferred universities, view details, and submit choices online.
* **Admin Dashboard:** Import student lists from Excel, monitor submissions, and export final placement data.
* **Automation:** Generates ready-to-submit Excel files for ministry upload.
* **Error Prevention:** Eliminates mismatched or missing student choices through digital verification.

## Setup and Installation

1. **Create a virtual environment**

   ```bash
   python3 -m venv .
   ```

2. **Activate the virtual environment**

   ```bash
   source bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Once setup is complete, start the app with:

```bash
python app.py
```

Then open your browser and go to:
👉 `http://127.0.0.1:5000`

## 💡 About

This project was built from a real-world need to fix inefficient university placement workflows in my school. It’s a reminder that innovation doesn’t need fancy tools i just built it by using flask and jquery — just a clear problem and the will to solve it.