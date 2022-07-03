from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery, InputMedia
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from aiogram.utils import callback_data

from aiogram.types.message import ContentType
from config import PAYMENTS_TOKEN
from shop import keyboard, cb
from main import dp, bot

import sqlite3


@dp.message_handler(commands=['start'])  # Меню
async def start(message):
	connect = sqlite3.connect('Accountant/accountant.db')
	cursor = connect.cursor()
	cursor.execute("""INSERT OR IGNORE INTO users (user_id, name) VALUES (?, ?)""", (message.chat.id, message.chat.first_name))
	cursor.close()
	connect.commit()
	connect.close()

	bs = types.InlineKeyboardMarkup()
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	bs.add(types.InlineKeyboardButton('Каталог', callback_data='asd'))
	item1 = types.KeyboardButton('Каталог')
	item2 = types.KeyboardButton('О нас')
	item3 = types.KeyboardButton('Контакты')
	item4 = types.KeyboardButton('Необходимо сделать')

	markup.add(item1, item2, item3, item4)
	photo = open('images/jopa.jpg', 'rb')
	await bot.send_photo(message.chat.id, photo)
	await bot.send_message(message.chat.id, """Приветствую тебя, Дорогой друг!
Рады видеть тебя в нашей грибной аптеке)
Это официальный магазин в телеграмме! 

ПРОМО-КОД fungi10 предоставит тебе скидку 10%
на покупку товаров любой категории.

В нашем магазине вы можете легко оформить и оплатить 
ваш заказ он-лайн. 

ПО любым вопросам работы магазина писать и звонить 
по номерам в разделе КОНТАКТЫ

_____________________________________________

??  Продукция не является лекарственным препаратом.""".format(message.from_user), reply_markup=markup)


# @dp.message_handler(content_types=['text'])  # Обработчик текста
# async def bot_message(message):
# 	if message.chat.type == 'private':
# 		if message.text == 'Каталог':
# 			keyboard = types.InlineKeyboardMarkup(row_width=3)
#
# 			btn10 = types.InlineKeyboardButton(text='ЛСД', callback_data='btn10')
# 			btn20 = types.InlineKeyboardButton(text='Грибосы', callback_data='btn20')
# 			btn30 = types.InlineKeyboardButton(text='ЭКСЕТЗИ', callback_data='btn30')
# 			btn40 = types.InlineKeyboardButton(text='СОЛЬКА', callback_data='btn40')
# 			btn50 = types.InlineKeyboardButton(text='\U0001F331 ГАШИК \U0001F331', callback_data='btn50')
# 			btn60 = types.InlineKeyboardButton(text='Мефедрон', callback_data='btn60')
# 			btn70 = types.InlineKeyboardButton(text='\U0001F33F Шишки \U0001F33F', callback_data='btn70')
#
# 			keyboard.add(btn10, btn20, btn30, btn40, btn50, btn60, btn70)
#
# 			await bot.send_message(message.chat.id, 'Каталог товаров', reply_markup=keyboard)
# 		elif message.text == 'О нас':
# 			await bot.send_message(message.chat.id, 'dsadasd')
# 		elif message.text == 'Контакты':
# 			await bot.send_message(message.chat.id, 'Мой телефон 89508621838')
# 		elif message.text == 'Назад':
# 			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# 			item1 = types.KeyboardButton('Каталог')
# 			item2 = types.KeyboardButton('О нас')
# 			item3 = types.KeyboardButton('Контакты')
#
# 			markup.add(item1, item2, item3)
#
# 			await bot.send_message(message.chat.id, 'Назад', reply_markup=markup)
# 		elif message.text == 'Необходимо сделать':
# 			await bot.send_message(message.chat.id,
# 								   '1. Реализация корзины: [(Добавить\убрать кол-во товара)(Возможность видеть количество выведенного на экран товара в корзине)(Удалить выведенный на экран товар из корзины)(Листать товары корзины если их больше одного)(Возможность перейти к оформлению заказа)(Возможность видеть сколько товаров в корзине и их общую стоимость)]')
# 			primer = open('images/primer.png', 'rb')
# 			await bot.send_photo(message.chat.id, primer)
# 		else:
# 			await bot.send_message(message.chat.id, 'Я не понимаю, выберете пункт из предоставленных команд')
#
#
# @dp.callback_query_handler(lambda call: True)
# async def inline(c):
# 	btn11 = types.InlineKeyboardButton(text='190.00 * 1 → 190 руб', callback_data='btn11')
# 	btn21 = types.InlineKeyboardButton(text='⨉', callback_data='btn21')
# 	btn31 = types.InlineKeyboardButton(text='▼', callback_data='btn31')
# 	btn41 = types.InlineKeyboardButton(text='1', callback_data='btn41')
# 	btn51 = types.InlineKeyboardButton(text='▲', callback_data='btn51')
# 	btn61 = types.InlineKeyboardButton(text='<<', callback_data='btn61')
# 	btn71 = types.InlineKeyboardButton(text='1 из 2', callback_data='btn71')
# 	btn81 = types.InlineKeyboardButton(text='>>', callback_data='btn81')
# 	btn91 = types.InlineKeyboardButton(text='✔️Оформить - 190 руб', callback_data='btn91')
#
# 	markup = types.InlineKeyboardMarkup(resize_keyboard=True).add(btn11).row(btn21, btn31, btn41, btn51).row(btn61,btn71,btn81).add(btn91)
#
# 	if c.data == 'btn10':
# 		await bot.send_photo(c.message.chat.id, photo=open('images/lsd.jpg', 'rb'),
# 							 caption='ЛСД • 20 таблеток \n\n\n Это полусинтетическое психоактивное вещество из семейства лизергамидов. '
# 									 'Химические названия: N,N-диэтиламид лизергиновой кислоты; N,N-диэтиллизергоиламид. '
# 									 'Условные названия и шифры: LSD; LSD-25; Lysergide, Delysid. Химическая формула вещества: C20H25N3O. '
# 									 '\n\n\n Остаток: неограничено', reply_markup=markup)
# 	elif c.data == 'btn20':
# 		await bot.send_photo(c.message.chat.id, photo=open('images/lsd.jpg', 'rb'), caption='Я работаю',
# 							 reply_markup=markup)
# 	elif c.data == 'btn30':
# 		await bot.send_photo(c.message.chat.id, photo=open('images/lsd.jpg', 'rb'), caption='Я работаю',
# 							 reply_markup=markup)
# 	elif c.data == 'btn40':
# 		await bot.send_photo(c.message.chat.id, photo=open('images/lsd.jpg', 'rb'), caption='Я работаю',
# 							 reply_markup=markup)
# 	elif c.data == 'btn50':
# 		await bot.send_photo(c.message.chat.id, photo=open('images/lsd.jpg', 'rb'), caption='Я работаю',
# 							 reply_markup=markup)
# 	elif c.data == 'btn60':
# 		await bot.send_photo(c.message.chat.id, photo=open('images/lsd.jpg', 'rb'), caption='Я работаю',
# 							 reply_markup=markup)
# 	elif c.data == 'btn70':
# 		await bot.send_photo(c.message.chat.id, photo=open('images/lsd.jpg', 'rb'), caption='Я работаю',
# 							 reply_markup=markup)
# 	if c.data == 'btn81':
# 		foto2 = open('images/lsd2.jpg', 'rb')
# 		await bot.edit_message_media(media=InputMedia(type='photo', media=foto2,
# 													  caption="вания: N,N-диэтиламид лизергиновой кислоты; N,N-диэтиллизергоиламид.Условные названия и "),
# 									 chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=markup)



@dp.message_handler(Command('cart'))
async def cart(message: Message):
	await message.answer('Что хотите купить?', reply_markup = keyboard)


@dp.callback_query_handler(cb.filter(id = '1'))
async def smart(call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time = 10)

	product_id = callback_data.get('id')
	user_id = call.message.chat.id

	connect = sqlite3.connect('Accountant/accountant.db')
	cursor = connect.cursor()
	cursor.execute("""INSERT INTO cart (user_id, product_id) VALUES (?, ?)""", [user_id, product_id])
	cursor.close()
	connect.commit()
	connect.close()

	await call.message.answer('Added!')


	"""___Создание корзины___"""
@dp.callback_query_handler(cb.filter(id = '2'))
async def smart(call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time = 10)

	product_id = callback_data.get('id')
	user_id = call.message.chat.id

	connect = sqlite3.connect('Accountant/accountant.db')
	cursor = connect.cursor()
	cursor.execute("""INSERT INTO cart (user_id, product_id) VALUES (?, ?)""", [user_id, product_id])
	cursor.close()
	connect.commit()
	connect.close()

	await call.message.answer('Added!')


@dp.message_handler(Command('buy'))
async def buy(message: Message):
	connect = sqlite3.connect('Accountant/accountant.db')
	cursor = connect.cursor()
	"""Достаем товары из корзины, касающиеся нас"""
	data = cursor.execute("""SELECT * FROM cart WHERE user_id=(?)""", [message.chat.id]).fetchall()
	cursor.close()
	connect.commit()
	cursor = connect.cursor()
	new_data = []
	"""Достаём имя и цену товаров зарегестрированных на наше имя"""
	for i in range(len(data)):
		new_data.append(cursor.execute("""SELECT * FROM product WHERE id =(?)""", [data[i][1]]).fetchall())
	cursor.close()
	connect.commit()
	connect.close()
	new_data = [new_data[i][0] for i in range(len(new_data))]
	"""Создаём список цен"""
	prices = [LabeledPrice(label = i[1], amount = i[2]) for i in new_data]

	await bot.send_invoice(message.chat.id,
						   title = 'Cart',
						   description = 'Description',
						   provider_token = PAYMENTS_TOKEN,
						   currency = 'rub',
						   need_email = True,
						   prices = prices,
						   start_parameter = 'example',
						   payload = 'some_invoice')


@dp.pre_checkout_query_handler(lambda q: True)
async def checkout_process(pre_checkout_query: PreCheckoutQuery):
	await bot.answer_pre_checkout_query(pre_checkout_query.id, ok = True)

	"""Подтверждение оплаты платежа"""
@dp.message_handler(content_types = ContentType.SUCCESSFUL_PAYMENT)
async def s_pay(message: Message):
	connect = sqlite3.connect('Accountant/accountant.db')
	cursor = connect.cursor()
	cursor.execute("""DELETE FROM cart WHERE user_id(?)""", [message.chat.id])
	cursor.close()
	connect.commit()
	connect.close()
	await bot.send_message(message.chat.id, 'Платеж прошел успешно')

	"""Фильтр файлов"""
@dp.message_handler(
	content_types=["audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
				   "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
				   "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
				   "migrate_from_chat_id", "pinned_message"])
async def get_user_content(message):
	await bot.send_message(message.chat.id, 'Я не понимаю, выберете пункт из предоставленных команд')