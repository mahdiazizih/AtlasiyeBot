from aiogram import Router
from core.command_router import register_common_commands  # دستورات مشترک

group_-1002787279234_router = Router(name="group_-1002787279234")

# ثبت دستورات مشترک برای این گروه
register_common_commands(group_-1002787279234_router)
