from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import string
import random
import psycopg2

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://linkly-tsg0.onrender.com"
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
load_dotenv()


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


def generate_shorter_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))


@app.get("/")
def home():
    return {
        "message": "Link Shortener API is running!!"
    }


@app.post("/shorten")
def shorten_url(url: str):

    try:
        short_code = generate_shorter_code()

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO url (original_url, short_code) VALUES (%s, %s)",
            (url, short_code)
        )

        conn.commit()

        cursor.close()
        conn.close()

        return {
            "original_url": url,
            "short_url": f"https://link-shortener-5xh7.onrender.com/{short_code}"
        
        }

    except Exception as e:

        return {
            "error": str(e)
        }


@app.get("/{short_code}")
def redirect_to_url(short_code: str):

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT original_url FROM url WHERE short_code = %s",
            (short_code,)
        )

        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result is None:
            return {
                "error": "Short URL not found"
            }

        return RedirectResponse(url=result[0])

    except Exception as e:

        return {
            "error": str(e)
        }
