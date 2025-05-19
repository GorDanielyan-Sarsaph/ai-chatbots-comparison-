import openai
import requests
from random import choice
from config import CONFIG

# Режим моков (если нет ключей)
USE_MOCKS = not any(CONFIG.values())

# Моки ответов
MOCK_ANSWERS = {
    "этические проблемы": {
        "chatgpt": "Проблемы: предвзятость данных, приватность, дезинформация.",
        "yandex": "Важно контролировать генерацию вредоносного контента.",
        "deepseek": "Соблюдение государственных норм в Китае."
    },
    "многозначные запросы": {
        "chatgpt": "Используется контекст диалога для уточнения.",
        "yandex": "Анализ интентов через Яндекс.Поиск.",
        "deepseek": "Алгоритмы перефразирования запросов."
    },
    "nlp-технологии": {
        "chatgpt": "Трансформеры, токенизация, attention-механизмы.",
        "yandex": "YaBERT, YaT5.",
        "deepseek": "Модификации BERT."
    }
}

def get_mock_answer(question: str, model: str) -> str:
    key = next((k for k in MOCK_ANSWERS if k in question.lower()), "default")
    return MOCK_ANSWERS.get(key, {}).get(model, "Ответ не найден.")

# Функции для ботов
def ask_chatgpt(question: str) -> str:
    if CONFIG["OPENAI_API_KEY"]:
        try:
            openai.api_key = CONFIG["OPENAI_API_KEY"]
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}]
            )
            return response.choices[0].message['content']
        except Exception:
            return "Ошибка API ChatGPT"
    return get_mock_answer(question, "chatgpt")

def ask_yandex_gpt(question: str) -> str:
    if CONFIG["YANDEX_IAM_TOKEN"] and CONFIG["YANDEX_FOLDER_ID"]:
        try:
            headers = {"Authorization": f"Bearer {CONFIG['YANDEX_IAM_TOKEN']}"}
            data = {
                "modelUri": f"gpt://{CONFIG['YANDEX_FOLDER_ID']}/yandexgpt-lite",
                "messages": [{"role": "user", "text": question}]
            }
            response = requests.post(
                "https://llm.api.cloud.yandex.net/llm/v1alpha/instruct",
                json=data,
                headers=headers
            )
            return
