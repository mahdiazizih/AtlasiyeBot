from telegram import Update
from telegram.ext import ContextTypes
import os
import mysql.connector

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # اتصال به دیتابیس
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", 3306)),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM customers")  # جدول نمونه برای تست
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()

        await update.message.reply_text(
            f"✅ Bot is working fine!\n🛢 DB connected.\n📦 Total customers: {count}"
        )

    except Exception as e:
        await update.message.reply_text(
            f"⚠️ Bot is working, but DB connection failed:\n{e}"
        )
