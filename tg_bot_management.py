import telegram
import time
import random
import argparse
import os
from dotenv import load_dotenv
load_dotenv()
tg_token = os.getenv('TG_TOKEN')
bot = telegram.Bot(token = tg_token)
updates = bot.get_updates()
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
            bot.send_document(chat_id=os.getenv('CHAT_ID'), document=open(path, "rb"))
            time.sleep(2)
    time.sleep(args.delay)
