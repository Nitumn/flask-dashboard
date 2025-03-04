# Flask Dashboard with Chart.js and MySQL

## Overview

This project is a Flask-based dashboard that visualizes data from a MySQL database using Chart.js. It allows users to interact with graphical representations of data stored in MySQL.

## Features

- 📊 Interactive charts powered by Chart.js
- 🛢️ MySQL database integration
- 🌐 Flask backend
- 🚀 Deployable to Heroku

---

## Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure MySQL Database

1. Import `jsondata.sql` into phpMyAdmin.
2. Update your database credentials in `config.py` or `.env`.

### 5️⃣ Run Flask App Locally

```bash
python app.py
```

Then, open `http://127.0.0.1:5000/` in your browser.

---

## Deployment to Heroku

### 1️⃣ Login to Heroku

```bash
heroku login
```

### 2️⃣ Create a Heroku App

```bash
heroku create flask-chart-view
```

### 3️⃣ Add a `Procfile`

Create a `Procfile` in the root directory with:

```
web: gunicorn app:app
```

### 4️⃣ Push to Heroku

```bash
git add .
git commit -m "Deploy Flask dashboard"
git push heroku main
```

### 5️⃣ Open the Deployed App

```bash
heroku open
```

---

## Usage

- Navigate to `/dashboard` to view the data visualizations.
- Ensure MySQL is running and accessible.

## Troubleshooting

Check Heroku logs if there are issues:

```bash
heroku logs --tail
```

## License

This project is open-source under the MIT License.

---

### 🚀 Happy Coding! 
