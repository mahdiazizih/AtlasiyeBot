# wedding_bot/groups/group_sandoogh.py

from telegram import Update
from telegram.ext import ContextTypes
from wedding_bot.core.command_router import handle_command

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(update, context)
