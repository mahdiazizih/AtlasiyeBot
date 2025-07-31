# wedding_bot/commands/test.py

from telegram import Update
from telegram.ext import ContextTypes
from core import db
from config.groups_config import get_group_config

async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = str(update.effective_chat.id)
    try:
        config = get_group_config(chat_id)
        db_path = config.get("db_path", None)
        if not db_path:
            raise Exception("Database path not found in group config.")
        
        conn = db.get_connection(chat_id)
        conn.execute("SELECT 1")  # تست ساده اتصال به DB
        await update.message.reply_text(f"✅ تست موفق برای گروه {chat_id}")
    except Exception as e:
        await update.message.reply_text(f"❌ خطا در تست گروه {chat_id}:\n{str(e)}")
