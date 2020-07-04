import os
import telebot
import price
from telebot import types
from dotenv import load_dotenv

load_dotenv()
tokentlg = os.getenv("TOKEN")
provider_payment_token = os.getenv("PAY_TOKEN")

bot = telebot.TeleBot(tokentlg)

welcome_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
welcome_keyboard_btn_1 = types.KeyboardButton("Windows")
welcome_keyboard_btn_2 = types.KeyboardButton("Office")
welcome_keyboard.add(welcome_keyboard_btn_1, welcome_keyboard_btn_2)

windows_versionselect_keyboard = types.InlineKeyboardMarkup()
windows_versionselect_keyboard_home = types.InlineKeyboardButton("Home", callback_data = "windows_home")
windows_versionselect_keyboard_pro = types.InlineKeyboardButton("Profesional", callback_data = "windows_pro")
windows_versionselect_keyboard.add(windows_versionselect_keyboard_home, windows_versionselect_keyboard_pro)

office_versionselect_keyboard = types.InlineKeyboardMarkup()
office_versionselect_keyboard_home = types.InlineKeyboardButton("Home", callback_data = "office_home")
office_versionselect_keyboard_pro = types.InlineKeyboardButton("Profesional", callback_data = "send_invoice_1")
office_versionselect_keyboard.add(office_versionselect_keyboard_home, office_versionselect_keyboard_pro)

price_1 = types.LabeledPrice(label='Настоящая Машина Времени', amount=4200000)

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, "Hello, chose product please", reply_markup = welcome_keyboard)

@bot.message_handler(content_types=["text"])
def choise(message):
	if message.chat.type == "private":
		if message.text == "Windows":
			bot.send_message(message.chat.id, "Chose version", reply_markup = windows_versionselect_keyboard)
		elif message.text == "Office":
			bot.send_message(message.chat.id, "Chose subscribtion type", reply_markup = office_versionselect_keyboard)
		else:
			bot.send_message(message.chat.id, "idk what to say...")
	print(message.text)

@bot.callback_query_handler(func = lambda call: True)
def callback_InlineKeyboard(call):
	try:
		if call.data == "windows_home":
			bot.send_message(call.message.chat.id, "Home")
		elif call.data == "windows_pro":
			bot.send_message(call.message.chat.id, "Pro")
		elif call.data == "office_home":
			bot.send_message(call.message.chat.id, "Home")
		elif call.data == "office_pro":
			bot.send_message(call.message.chat.id, "Pro")
		elif call.data == "send_invoice_1":
			bot.send_invoice(
				call.message.chat.id,
				title = "tm_title",
				description = "tm_description",
				provider_token = provider_payment_token,
				currency = "uah",
				photo_url = "photo.jfif",
				photo_height = 800,
				photo_width = 600,
				photo_size =750,
				is_flexible = False,
				prices = [price_1],
				start_parameter = 'time-machine-example',
				invoice_payload = 1)
	except Exception as e:
		print(repr(e))

@bot.pre_checkout_query_handler(func=lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
	bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
	bot.send_message(
		message.chat.id,
		"Succesful payment!")
	

bot.polling(none_stop = True)
