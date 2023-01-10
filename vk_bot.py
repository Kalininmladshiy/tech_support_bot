import random
import vk_api as vk
import os
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType
from google.cloud import dialogflow


def dialog(event, vk_api):
    message_from_bot = detect_intent_texts(event.user_id, event.text)
    vk_api.messages.send(
        user_id=event.user_id,
        message=message_from_bot,
        random_id=random.randint(1,1000)
    )

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

    if response.query_result.intent.is_fallback:
        return None    
    else:
        return response.query_result.fulfillment_text


if __name__ == "__main__":
    load_dotenv()
    vk_token = os.getenv("VK_BOT_TOKEN")
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            dialog(event, vk_api)
