import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram.ext import MessageHandler, Filters
from utils.dialogflow_tools import detect_intent_texts


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Бот запущен!')


def dialog(update: Update, context: CallbackContext, project_id):
    message_from_bot = detect_intent_texts(
        project_id=project_id,
        session_id=update.effective_chat.id,
        text=update.message.text,
    ).fulfillment_text
    context.bot.send_message(chat_id=update.effective_chat.id, text=message_from_bot)


def main():
    load_dotenv()
    tg_token = os.getenv('TG_BOT_TOKEN')
    project_id = os.getenv('PROJECT_ID')

    updater = Updater(token=tg_token)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    dialog_handler = MessageHandler(
        Filters.text & (~Filters.command),
        lambda update, context: dialog(update, context, project_id),
    )
    dispatcher.add_handler(dialog_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()
