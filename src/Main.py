from utils import ask_chatgpt, ask_yandex_gpt, ask_deepseek
import os

QUESTIONS = [
    "Какие этические проблемы возникают при использовании ИИ в чат-ботах?",
    "Как ИИ-боты обрабатывают многозначные запросы?",
    "Какие технологии лежат в основе современных NLP-моделей?"
]

TASKS = {
    "task1": "Как оформить возврат товара в интернет-магазине без чека?",
    "task2": "Найдите производную функции f(x) = 3x^2 + sin(x)."
}

def save_response(filename: str, content: str):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def run():
    # Ответы на вопросы
    for idx, question in enumerate(QUESTIONS):
        for model_func, model_name in [
            (ask_chatgpt, "chatgpt"),
            (ask_yandex_gpt, "yandex"),
            (ask_deepseek, "deepseek")
        ]:
            response = model_func(question)
            save_response(f"data/questions/{model_name}_q{idx+1}.txt", response)

    # Решение кейсов
    for task_name, task_text in TASKS.items():
        for model_func, model_name in [
            (ask_chatgpt, "chatgpt"),
            (ask_yandex_gpt, "yandex"),
            (ask_deepseek, "deepseek")
        ]:
            response = model_func(task_text)
            save_response(f"data/responses/{task_name}/{model_name}.txt", response)

if __name__ == "__main__":
    run()
