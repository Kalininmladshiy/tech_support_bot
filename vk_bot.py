import random
import vk_api as vk
import os
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType
from google.cloud import dialogflow
from utils.dialogflow_tools import detect_intent_texts


def dialog(event, vk_api):
    if detect_intent_texts(event.user_id, event.text).intent.is_fallback:
        pass
    else:
        message_from_bot = detect_intent_texts(event.user_id, event.text).fulfillment_text
        vk_api.messages.send(
                user_id=event.user_id,
                message=message_from_bot,
                random_id=random.randint(1,1000)
            )


if __name__ == "__main__":
    load_dotenv()
    vk_token = os.getenv("VK_BOT_TOKEN")
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            dialog(event, vk_api)
