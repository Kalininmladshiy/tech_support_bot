import telegram
import os
import time
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram.ext import MessageHandler, Filters
from utils.dialogflow_tools import detect_intent_texts


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Бот запущен!")


def dialog(update: Update, context: CallbackContext):
    message_from_bot = detect_intent_texts(
        session_id=update.effective_chat.id,
        text=update.message.text,
    ).fulfillment_text
    context.bot.send_message(chat_id=update.effective_chat.id, text=message_from_bot)


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv("TG_BOT_TOKEN")
    tg_chat_id = os.getenv("TG_CHAT_ID")#Delet??????

    updater = Updater(token=tg_token)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    dialog_handler = MessageHandler(Filters.text & (~Filters.command), dialog)
    dispatcher.add_handler(dialog_handler)

    updater.start_polling()
