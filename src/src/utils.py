from random import choice

# Заглушка для ChatGPT
def ask_chatgpt(question: str) -> str:
    answers = {
        "этические проблемы": "Пример ответа ChatGPT: Проблемы включают предвзятость данных и приватность пользователей.",
        "многозначные запросы": "ChatGPT может использовать контекст диалога для уточнения.",
        "NLP-технологии": "Основные технологии: трансформеры, токенизация, attention-механизмы."
    }
    return answers.get(question.lower(), "Ответ не найден.")

# Заглушка для Yandex GPT
def ask_yandex_gpt(question: str) -> str:
    answers = {
        "этические проблемы": "Yandex GPT: Этические аспекты требуют контроля за генерацией вредоносного контента.",
        "многозначные запросы": "Yandex GPT анализирует интенты пользователя через Яндекс.Поиск.",
        "NLP-технологии": "Yandex GPT использует YaBERT и YaT5."
    }
    return answers.get(question.lower(), "Ответ не найден.")

# Заглушка для DeepSeek
def ask_deepseek(question: str) -> str:
    answers = {
        "этические проблемы": "DeepSeek: В Китае акцент на соблюдении государственных норм.",
        "многозначные запросы": "DeepSeek применяет алгоритмы перефразирования.",
        "NLP-технологии": "DeepSeek основан на модификациях BERT."
    }
    return answers.get(question.lower(), "Ответ не найден.")
