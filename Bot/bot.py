from telegram.ext import Updater
from handlers.commands import start, suggest_meeting
from handlers.conversation import conv_handler

def main():
    updater = Updater("TOKEN", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(start)
    dispatcher.add_handler(suggest_meeting)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
