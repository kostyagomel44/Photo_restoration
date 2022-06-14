from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

button_h1 = KeyboardButton('Restore')
button_h2 = KeyboardButton('Colorize')
button_h3 = KeyboardButton('Crop')
button_h4 = KeyboardButton('Upscale')
greet_kb = ReplyKeyboardMarkup()

# greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_h2, button_h3, button_h4)
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_h1, button_h2, button_h3,button_h4)
