import telegram
import time
import random
import argparse
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    tg_token = os.getenv('TELEGRAM_TOKEN_BOT')
    chat_id = os.getenv('TG_CHAT_ID')
    bot = telegram.Bot(token = tg_token)
    parser = argparse.ArgumentParser(
        description='Программа отправляет все фото из директории с задержкой, которую задают при запуске в секундах.'
    )
    parser.add_argument('delay', help='Задержка между отпрвкой фото в секундах', type=int, default = 14400)
    args = parser.parse_args()
    while True:
        for dirpath, dirnames, filenames in os.walk("images"):
            random.shuffle(filenames)
            for filename in filenames:
                path = f"images/{filename}"
                with open(path, "rb") as file:
                    bot.send_document(chat_id, document=file)
                time.sleep(2)
        time.sleep(args.delay)


if __name__ == '__main__':
    main()
