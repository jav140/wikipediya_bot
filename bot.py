"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import wikipedia

import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5937814586:AAFziLVNac-7jzAvNA5fFhgXA7vBSyUeIP8'
wikipedia.set_lang('')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm WikiBot!\nPowered by aiogram.")



@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Article related to text not found!')

    # old style:
    # await bot.send_message(message.chat.id, message.text)

    # await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)