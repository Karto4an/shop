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

name_keyboard_choise_1 = "Windows"
name_keyboard_choise_2 = "Office"
name_inlinekeyboard_versionchoise_1 = "Home"
name_inlinekeyboard_versionchoise_2 = "Profesional"
name_inlinekeyboard_callback_1 = "invoice_windowshome"
name_inlinekeyboard_callback_2 = "invoice_windowspro"
name_inlinekeyboard_versionchoise_3 = "Home"
name_inlinekeyboard_versionchoise_4 = "Profesional"
name_inlinekeyboard_callback_3 = "invoice_officehome"
name_inlinekeyboard_callback_4 = "invoice_officepro"

price_1_title = "Microsoft Windows 10 Home"
price_1_description = "Version of Windows 10 for home usage"
price_1_currency = "uah"

price_1 = types.LabeledPrice(label = "MS Windows Home", amount = 10000)

price_2_title = "Microsoft Windows 10 Profesional"
price_2_description = "Version of Windows 10 for profesional usage"
price_2_currency = "uah"

price_2 = types.LabeledPrice(label = "MS Windows Pro", amount = 14000)

price_3_title = "Microsoft Office Home"
price_3_description = "Version of MS Office for home usage"
price_3_currency = "uah"

price_3 = types.LabeledPrice(label = "MS Office Home", amount = 8000)

price_4_title = "Microsoft Office Profesional"
price_4_description = "Version of MS Office for profesional usage"
price_4_currency = "uah"

price_4 = types.LabeledPrice(label = "MS Office Pro", amount = 12000)
#--------------------------------------------------------------

welcome_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
welcome_keyboard_btn_1 = types.KeyboardButton(name_keyboard_choise_1)
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



@bot.message_handler(commands = ["start"])
def welcome(message):
	bot.send_message(message.chat.id, "Hello, chose product please", reply_markup = welcome_keyboard)

@bot.message_handler(content_types = ["text"])
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
		if call.data == name_inlinekeyboard_callback_1:
			bot.send_invoice(
				call.message.chat.id,
				title = price_1_title,
				description = price_1_description,
				provider_token = provider_payment_token,
				currency = price_1_currency,
				photo_url = "photo.jfif",
				photo_height = 800,
				photo_width = 600,
				photo_size =750,
				is_flexible = False,
				prices = [price_1],
				start_parameter = "time-machine-example",
				invoice_payload = 1)
		elif call.data == name_inlinekeyboard_callback_2:
			bot.send_invoice(
				call.message.chat.id,
				title = price_2_title,
				description = price_2_description,
				provider_token = provider_payment_token,
				currency = price_2_currency,
				photo_url = "photo.jfif",
				photo_height = 800,
				photo_width = 600,
				photo_size =750,
				is_flexible = False,
				prices = [price_2],
				start_parameter = "time-machine-example",
				invoice_payload = 1)
		elif call.data == name_inlinekeyboard_callback_3:
			bot.send_invoice(
				call.message.chat.id,
				title = price_3_title,
				description = price_3_description,
				provider_token = provider_payment_token,
				currency = price_3_currency,
				photo_url = "photo.jfif",
				photo_height = 800,
				photo_width = 600,
				photo_size =750,
				is_flexible = False,
				prices = [price_3],
				start_parameter = "time-machine-example",
				invoice_payload = 1)
		elif call.data == name_inlinekeyboard_callback_4:
			bot.send_invoice(
				call.message.chat.id,
				title = price_4_title,
				description = price_4_description,
				provider_token = provider_payment_token,
				currency = price_4_currency,
				photo_url = "photo.jfif",
				photo_height = 800,
				photo_width = 600,
				photo_size =750,
				is_flexible = False,
				prices = [price_4],
				start_parameter = "time-machine-example",
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
