
from aiogram import Router
from core.command_router import register_common_commands  # فراخوانی دستورات مشترک

group_-4818872906_router = Router(name="group_-4818872906")

# ثبت دستورات مشترک برای این گروه
register_common_commands(group_-4818872906_router)
