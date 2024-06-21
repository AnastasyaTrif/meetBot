from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import MessageHandler, Filters, CommandHandler, ConversationHandler, CallbackContext
from utils.db import add_meeting

DATE, PREFERENCE = range(2)

def start_conversation(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Пожалуйста, введите дату, которая вам удобна (в формате ГГГГ-ММ-ДД):')
    return DATE

def date(update: Update, context: CallbackContext) -> int:
    context.user_data['date'] = update.message.text
    reply_keyboard = [['Прогулка в парке', 'Поход в ресторан', 'Поход в кино', 'Посидеть дома']]
    update.message.reply_text('Спасибо! Теперь выберите вариант встречи:',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return PREFERENCE

def preference(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['preference'] = update.message.text
    add_meeting(update.message.from_user.id, user_data['date'], user_data['preference'])
    update.message.reply_text('Спасибо! Ваши данные сохранены.')
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Действие отменено.')
    return ConversationHandler.END

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('plan', start_conversation)],
    states={
        DATE: [MessageHandler(Filters.text & ~Filters.command, date)],
        PREFERENCE: [MessageHandler(Filters.text & ~Filters.command, preference)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)
