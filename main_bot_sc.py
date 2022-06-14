from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from io import BytesIO
import time

from config_sc import TOKEN
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import keyboard_sc as kb
from DeOldify.colorizer_run import colorizer
from photo_restoration.SC import scratching
from image_compress import image_compresser
from wrapper import wrapper
import os 
from image_upscaler import upscaler

#TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, я бот который умеет улучшать и колоризировать фото! "
                        "Загрузите фото для обработки!", reply_markup=kb.greet_kb1)





@dp.message_handler(content_types=['photo'])
async def get_photo(message: types.Message):
    user_id = message.from_user.id
    await message.reply("Что бы вы хотели сделать с фото?", reply_markup=kb.greet_kb1)
    img_path = f'/home/konstantin/Projects/Diploma/input_{user_id}.jpg' 
    await message.photo[-1].download(img_path)
    image_compresser(img_path, img_path)



@dp.message_handler()
async def echo_message(msg: types.Message):


    mes = msg.text
    user_id = msg.from_user.id

    if mes == 'Restore':
        img_path = f'/home/konstantin/Projects/Diploma/input_{user_id}' 
        scratching(user_id)
        photo = open(f'/home/konstantin/Projects/Diploma/photo_restoration/output_w_scratch/final_output/input_{user_id}.png', 'rb')
        await bot.send_photo(msg.from_user.id,photo)
        await msg.reply("Ваше фото после восстановления!")
        command_copy = f'cp /home/konstantin/Projects/Diploma/photo_restoration/output_w_scratch/final_output/input_{user_id}.png /home/konstantin/Projects/Diploma' 
        os.system(command_copy)
        command_del = f'rm {img_path}.jpg'
        os.system(command_del)
        command_convert = f'convert {img_path}.png {img_path}.jpg'
        os.system(command_convert)





    if mes == 'Colorize':
        img_path = f'/home/konstantin/Projects/Diploma/input_{user_id}.jpg'
        colorizer(img_path, user_id=user_id)
        # photo = open('/home/konstantin/Projects/Diploma/DeOldify/result_images/result.jpg', 'rb')
        photo = open(img_path, 'rb')
        await bot.send_photo(msg.from_user.id, photo)
        await msg.reply("Ваше фото после колоризации!")



    if mes == 'Crop':
        img_path = f'/home/konstantin/Projects/Diploma/input_{user_id}.jpg'
        wrapper(img_path, img_path)
        photo = open(img_path, 'rb')
        await bot.send_photo(msg.from_user.id, photo)
        await msg.reply("Ваше фото после обрезания!")

    
    if mes == 'Upscale':
        img_path = f'/home/konstantin/Projects/Diploma/input_{user_id}.jpg'
        upscaler(img_path, img_path)
        photo = open(img_path, 'rb')
        await bot.send_photo(msg.from_user.id, photo)
        await msg.reply("Ваше фото после после повышения качества!")



if __name__ == '__main__':
    executor.start_polling(dp)

