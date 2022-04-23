import logging
from telegram.ext import *

API_KEY = '5367816326:AAFzA7BtsiVObDgKvdPqLpARbYfzi4zvzaU'

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('Купи слона!')


def help_command(update, context):
    update.message.reply_text('Помощь в покупке слонов!')


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    response = f'Все говорят {text}, а ты купи слона!'

    # Bot response
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    # Commands
    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('help', help_command))

    # Messages
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
