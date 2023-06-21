"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types
wikipedia.set_lang('uz')
API_TOKEN = '6241101965:AAF_BqN_lKXVIvVxsHwZTsH9esXvGZbErFc'

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
    await message.reply("Wikipediya botga hush kelibsiz")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    try:
        response = wikipedia.summary(message.text)  

        await message.answer(response)
    except:

        await message.answer("Bu mavzuga oid maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)