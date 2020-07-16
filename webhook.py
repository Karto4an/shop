import os
import telebot
from telebot import types
import requests
import json
from dotenv import load_dotenv

load_dotenv()
tokentlg = os.getenv("TOKEN")

url = "https://discordapp.com/api/webhooks/733388492431687771/C0HczHL3Y10m4pEtBn9NypMWK5mrLsAhpL3Kd5ruNgjOTqdmSPzi03XAxQEiuy-uXQ4z"

bot = telebot.TeleBot(tokentlg)

@bot.message_handler(content_types = ["text"])
def choise(message):
	if message.chat.type == "private":
		if message.text == "/start":
			pass
		else:
			data = {}
			data["content"] = message.text
			print(message.from_user.username)
			data["username"] = message.from_user.username

			#leave this out if you dont want an embed
			data["embeds"] = []
			embed = {}
			#for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
			embed["description"] = "Отправлено из Telegram с помощью подводной магии"
			embed["title"] = ""
			data["embeds"].append(embed)

			result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

			try:
			    result.raise_for_status()
			except requests.exceptions.HTTPError as err:
			    print(err)
			else:
			    print("Payload delivered successfully, code {}.".format(result.status_code))
bot.polling(none_stop = True)