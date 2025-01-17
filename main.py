import telegram

bot = telegram.Bot(token='8067618575:AAGa5VrBMRVecIxNWtRy1_Grsufc3D5dJJk')
updates = bot.get_updates()
print(bot.get_me())
bot.send_message(chat_id="@dvmn_tg", text="I'm sorry Dave I'm afraid I can't do that.")