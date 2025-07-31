# wedding_bot/core/group_router.py

from aiogram import Router
from core.config.groups_config import GROUP_CONFIG
import importlib

router = Router()

def setup_group_routers(dp: Router):
    for chat_id, cfg in GROUP_CONFIG.items():
        module_name = cfg["router_module"]
        try:
            # ماژول را از پوشه groups ایمپورت می‌کنیم
            module = importlib.import_module(f"wedding_bot.groups.{module_name}")
            
            # نام متغیر روتری که در فایل ماژول تعریف شده (مثلاً group_atlas_router)
            router_instance = getattr(module, f"{module_name}_router")

            # اضافه کردن router به Dispatcher
            dp.include_router(router_instance)
        except Exception as e:
            print(f"[ERROR] Cannot load router for group {chat_id} ({cfg['name']}): {e}")
