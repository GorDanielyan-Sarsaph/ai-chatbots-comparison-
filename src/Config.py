import os
from dotenv import load_dotenv

load_dotenv()

# Конфиг с проверкой наличия ключей
CONFIG = {
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", None),
    "YANDEX_IAM_TOKEN": os.getenv("YANDEX_IAM_TOKEN", None),
    "YANDEX_FOLDER_ID": os.getenv("YANDEX_FOLDER_ID", None),
    "DEEPSEEK_API_KEY": os.getenv("DEEPSEEK_API_KEY", None)
}
