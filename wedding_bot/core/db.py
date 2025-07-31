
# wedding_bot/core/db.py

import os
import psycopg2
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

# تابع اتصال به دیتابیس
def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

# تابعی برای اجرای کوئری ساده (در آینده می‌تونیم گسترش بدیم)
def execute_query(query, params=None, fetch=False):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            if fetch:
                return cur.fetchall()
            conn.commit()
    except Exception as e:
        print(f"DB Error: {e}")
    finally:
        conn.close()
