import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

from core.group_router import setup_group_routers  # روتر گروه‌ها

# بارگذاری متغیرهای محیطی از .env
load_dotenv()

# پیکربندی لاگ‌ها
logging.basicConfig(level=logging.INFO)

# توکن ربات از .env
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ساخت Bot و Dispatcher
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# راه‌اندازی روت‌های گروه‌ها
setup_group_routers(dp)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
