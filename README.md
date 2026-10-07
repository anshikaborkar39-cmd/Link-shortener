# 🔗 Linkly – URL Shortener

Linkly is a full-stack URL Shortener application that converts long URLs into short, easy-to-share links.

## 🚀 Features

- Convert long URLs into short links
- Generate unique 6-character short codes
- Store URLs in PostgreSQL
- Redirect short URLs to the original URL
- Copy shortened URLs easily
- Simple and responsive user interface

## 🛠️ Technologies Used

### Frontend
- React.js
- Vite
- JavaScript
- HTML
- CSS

### Backend
- Python
- FastAPI
- PostgreSQL

## 🔄 How It Works

1. User enters a long URL.
2. React sends the URL to the FastAPI backend.
3. The backend generates a unique short code.
4. The URL and short code are stored in PostgreSQL.
5. The backend returns the shortened URL.
6. Opening the shortened URL redirects the user to the original URL.

## 📁 Project Structure

```text
Link-shortener/
│
├── public/
├── src/
│   ├── App.jsx
│   ├── App.css
│   ├── index.css
│   └── main.jsx
│
├── main.py
├── package.json
├── package-lock.json
├── vite.config.js
├── eslint.config.js
├── .gitignore
└── README.md
⚙️ Setup
Frontend
npm install
npm run dev
Frontend:
http://localhost:5173
Backend
Install the required packages:
pip install fastapi uvicorn psycopg2-binary python-dotenv
Run the backend:
http://127.0.0.1:8000
🗄️ Database
PostgreSQL is used to store the original URLs and generated short codes.

🔐 Security

Database credentials are stored in a .env file and excluded from GitHub using .gitignore.

👩‍💻 Author

Anshika Borkar
