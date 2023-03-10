import random
import vk_api as vk
import os
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType
from utils.dialogflow_tools import detect_intent_texts


def dialog(event, vk_api, project_id):
    message_from_bot = detect_intent_texts(project_id, event.user_id, event.text)
    if not message_from_bot.intent.is_fallback:
        vk_api.messages.send(
                user_id=event.user_id,
                message=message_from_bot.fulfillment_text,
                random_id=random.randint(1, 1000),
            )


def main():
    load_dotenv()
    vk_token = os.getenv("VK_BOT_TOKEN")
    project_id = os.getenv("PROJECT_ID")
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            dialog(event, vk_api, project_id)


if __name__ == "__main__":
    main()
