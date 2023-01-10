import telegram
import os
import time
from dotenv import load_dotenv
from google.cloud import dialogflow
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram.ext import MessageHandler, Filters


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Бот запущен!")


def dialog(update: Update, context: CallbackContext):
    message_from_bot = detect_intent_texts(
        session_id=update.effective_chat.id,
        text=update.message.text,
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=message_from_bot)


def detect_intent_texts(session_id, text, language_code='ru'):
    load_dotenv()
    project_id = os.getenv("PROJECT_ID")

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result.fulfillment_text


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
