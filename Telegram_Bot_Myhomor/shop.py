from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

cb = CallbackData('buy', 'id')
keyboard = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton('Grib: 10000p', callback_data = 'buy:1'),
			InlineKeyboardButton('LSD: 100000p', callback_data = 'buy:2')
		]
	]
)
