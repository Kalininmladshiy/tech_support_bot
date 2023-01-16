import os
from dotenv import load_dotenv
from google.cloud import dialogflow


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

    return response.query_result
