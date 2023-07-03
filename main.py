from telebot.async_telebot import AsyncTeleBot
bot = AsyncTeleBot('6311823145:AAEEgxS0m_XjlBV0yQus_eizz7NITbAooVY')

@bot.message_handler(commands=['help','start'])
async def send_welcome(message):
    await bot.reply_to(message, 'Приветствую тебя новый пользователь!')


@bot.message_handler(func=lambda message: True)
# async def echo_message(message):
# await bot.reply_to(message, message.text)
async def echo_message(message):
    text_message = message.text
    text_message = text_message.lower()
    if 'дела' in text_message or 'настроение' in text_message:
        await bot.reply_to(message, 'Хорошо, а у тебя?')
    elif 'шутка' in text_message or 'анекдот' in text_message:
        await bot.reply_to(message, 'i')
    else:
        await bot.reply_to(message, 'я не понимаю')


@bot.message_handler(commands=['finish'])
async def send_welcome(message):
    await bot.reply_to(message, 'Конец')


import asyncio

asyncio.run(bot.polling())