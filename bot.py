import os
import telebot
from telebot import types
from dotenv import load_dotenv
from aiogram.types.message import ContentType

load_dotenv()
tokentlg = os.getenv("TOKEN")
provider_payment_token = os.getenv("PAY_TOKEN")

bot = telebot.TeleBot(tokentlg)

#SETUP BLOCK

name_keyboard_choise_1 = "windows"
name_keyboard_choise_2 = "office"
name_inlinekeyboard_versionchoise_1 = "Home"
name_inlinekeyboard_versionchoise_2 = "Profesional"
name_inlinekeyboard_callback_1 = "windows_home"
name_inlinekeyboard_callback_2 = "windows_pro"
name_inlinekeyboard_versionchoise_3 = "Home"
name_inlinekeyboard_versionchoise_4 = "Profesional"
name_inlinekeyboard_callback_3 = "office_home"
name_inlinekeyboard_callback_4 = "invoice_officepro"

#--------------------------------------------------------------

welcome_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
welcome_keyboard_btn_1 = types.KeyboardButton(name_keyboard_choise_2)
welcome_keyboard_btn_2 = types.KeyboardButton(name_keyboard_choise_2)
welcome_keyboard.add(welcome_keyboard_btn_1, welcome_keyboard_btn_2)

windows_versionselect_keyboard = types.InlineKeyboardMarkup()
windows_versionselect_keyboard_home = types.InlineKeyboardButton(name_inlinekeyboard_versionchoise_1, callback_data = name_inlinekeyboard_callback_1)
windows_versionselect_keyboard_pro = types.InlineKeyboardButton(name_inlinekeyboard_versionchoise_2, callback_data = name_inlinekeyboard_callback_2)
windows_versionselect_keyboard.add(windows_versionselect_keyboard_home, windows_versionselect_keyboard_pro)

office_versionselect_keyboard = types.InlineKeyboardMarkup()
office_versionselect_keyboard_home = types.InlineKeyboardButton(name_inlinekeyboard_versionchoise_3, callback_data = name_inlinekeyboard_callback_3)
office_versionselect_keyboard_pro = types.InlineKeyboardButton(name_inlinekeyboard_versionchoise_4, callback_data = name_inlinekeyboard_callback_4)
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
		elif call.data == "invoice_officepro":
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
def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
	bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@bot.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
def process_successful_payment(message: types.Message):
	bot.send_message(message.chat.id, "Done.")


bot.polling(none_stop = True)
