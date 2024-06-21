from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я помогу вам с планированием прогулок. Используйте команду /plan для начала.')

def suggest_meeting(update: Update, context: CallbackContext) -> None:
    from utils.db import get_meetings

    meetings = get_meetings()
    if not meetings:
        update.message.reply_text('Нет данных для предложений.')
        return

    dates = [meeting[0] for meeting in meetings]
    common_date = max(set(dates), key=dates.count)

    preferences = [meeting[1] for meeting in meetings if meeting[0] == common_date]
    common_preference = max(set(preferences), key=preferences.count)

    update.message.reply_text(f'Предлагаемая дата: {common_date}\nПредлагаемый вариант встречи: {common_preference}')

start = CommandHandler('start', start)
suggest_meeting = CommandHandler('suggest', suggest_meeting)
