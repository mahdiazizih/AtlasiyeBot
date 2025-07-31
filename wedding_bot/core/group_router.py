# wedding_bot/core/group_router.py

from aiogram import Router
from groups.group_-1002787279234 import group_-1002787279234_router  # 🟢 خط 2

def setup_group_routers(dp: Router):  # 🟢 خط 4
    dp.include_router(group_-1002787279234_router)  # 🟢 خط 5

from aiogram.types import Message
from importlib import import_module
import logging

router = Router()
logger = logging.getLogger(__name__)

# تعریف لیست گروه‌های مجاز (chat_id ها)
VALID_GROUPS = [
    -1002787279234,   # گروه تالار
    -4818872906       # گروه صندوق
]

@router.message()
async def handle_group_message(message: Message):
    chat_id = message.chat.id

    if chat_id not in VALID_GROUPS:
        logger.warning(f"دریافت پیام از گروه ناشناس: {chat_id}")
        return  # نادیده گرفتن پیام

    try:
        # ماژول پیکربندی گروه را بارگذاری کن
        module_name = f"wedding_bot.groups.group_{chat_id}"
        group_module = import_module(module_name)

        # ثبت روت مناسب گروه در Dispatcher
        if hasattr(group_module, "register"):
            await group_module.register(message)
        else:
            logger.warning(f"ماژول {module_name} تابع register ندارد")

    except Exception as e:
        logger.exception(f"خطا در بارگذاری تنظیمات گروه {chat_id}: {e}")
