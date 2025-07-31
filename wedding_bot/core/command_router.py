from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

# ایمپورت دستورات
from commands import save, show, edit, del , test  # این خط را به‌روزرسانی کن

def register_command_handlers(application):
    application.add_handler(CommandHandler("save", save.save_command))
    application.add_handler(CommandHandler("show", show.show_command))
    application.add_handler(CommandHandler("edit", edit.edit_command))
    application.add_handler(CommandHandler("del", delete.delete_command))
    application.add_handler(CommandHandler("test", test.test_command))  # این خط را اضافه کن
