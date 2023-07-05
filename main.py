import os

from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
TOKEN=os.getenv('TOKEN')
bot=AsyncTeleBot(TOKEN)
bot=AsyncTeleBot(TOKEN, parse_mode='HTML')#курсив

@bot.message_handler(commands=['help','start'])
async def send_welcome(message):
    await bot.reply_to(message, 'Приветствую тебя новый пользователь!')
    print(message)

@bot.message_handler(commands=['finish'])
async def send_welcome(message):
    await bot.reply_to(message, 'Конец')


@bot.message_handler(commands=['a'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id,'бб')#(увед без звука, пересылка, disable_notification=True, protect_content=True)

@bot.message_handler(commands=['k']) #кубик
async def send_welcome(message):
    chat_id = message.from_user.id
    bot_message=await bot.send_dice(chat_id,'🎲')
    print(bot_message.dice.value)

@bot.message_handler(commands=['s']) #id sticker
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_sticker(chat_id,'CAACAgIAAxkBAAIiJWSkCy4JB5GTGksYrjWQ2H4uQoJRAAITAAPANk8TqrOH9384yqUvBA')

@bot.message_handler(commands=['x'])#отправка файла
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_document(chat_id, open('text.txt','rb'))

@bot.message_handler(commands=['l'])#отправка координат
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_location(chat_id, 55.638287, 37.524232 )

@bot.message_handler(commands=['v'])#фото
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_photo(chat_id,'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0', caption='Заголовок')

@bot.message_handler(commands=['y'])#клавиатура
async def send_welcome(message):
    chat_id = message.chat.id
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('Первая кнопка')
    markup.add('Вторая кнопка')
    await bot.send_message(chat_id,'Второй вариант кнопок', reply_markup=markup)

def generate_reply_keyboard(list_buttons, row):
    markup=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*list_buttons, row_width=row)
    return markup

@bot.message_handler(commands=['y2'])#клавиатура2
async def send_welcome(message):
    chat_id = message.from_user.id
    list_buttons = 'Первая кнопка','Вторая кнопка','Третья кнопка'
    await bot.send_message(chat_id,'Второй вариант кнопок', reply_markup=generate_reply_keyboard(list_buttons,2))

@bot.message_handler(commands=['z'])#клавиатура3
async def send_welcome(message):
    chat_id = message.from_user.id
    markup = InlineKeyboardMarkup()
    button1=InlineKeyboardButton('Первая кнопка', callback_data='first')
    button2=InlineKeyboardButton('Вторая кнопка', callback_data='second')
    button3=InlineKeyboardButton('Третья кнопка', callback_data='three')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    await bot.send_message(chat_id, 'Первый вариант кнопок', reply_markup=markup)

@bot.message_handler(commands=['m'])#таймер
async def send_welcome(message):
    chat_id=message.from_user.id
    bot_message=await bot.send_message(chat_id, 'Начался таймер 5 секунд')
    for i in range (1,6):
        await asyncio.sleep(1)
        await bot.edit_message_text(f'{5-i} секунд осталось', chat_id, bot_message.id)
    await bot.delete_message(chat_id, bot_message.id)

@bot.message_handler(commands=['p'])#удалить
async def send_welcome(message):
    chat_id=message.from_user.id
    await bot.delete_message(chat_id, message.id)

@bot.message_handler(commands=['h'])#курсив
async def send_welcome(message):
    chat_id=message.from_user.id
    await bot.send_message(chat_id, '<i>текст</i>')

@bot.message_handler(commands=['zt'])#жирный шрифт
async def send_welcome(message):
    chat_id=message.from_user.id
    await bot.send_message(chat_id, '<b>текст</b>')

@bot.message_handler(commands=['zp'])#подчеркивание
async def send_welcome(message):
    chat_id=message.from_user.id
    await bot.send_message(chat_id, '<u>текст</u>')

@bot.message_handler(commands=['zt'])#подчеркивание
async def send_welcome(message):
    chat_id=message.from_user.id
    await bot.send_message(chat_id, '<u>текст</u>')

@bot.message_handler(commands=['zz'])#зачеркивание
async def send_welcome(message):
    chat_id=message.from_user.id
    await bot.send_message(chat_id, '<s>текст</s>')

@bot.message_handler(commands=['zm'])#моноширныйшрифт
async def send_welcome(message):
    chat_id=message.from_user.id
    await bot.send_message(chat_id, '<code>текст</code>')

@bot.message_handler(commands=['zm2'])#моноширныйшрифт c сохранение пробелов и переносов
async def send_welcome(message):
    chat_id=message.from_user.id
    await bot.send_message(chat_id, '<pre>текст</pre>')

@bot.message_handler(commands=['sp'])#скрывает под спойлер
async def send_welcome(message):
    chat_id=message.from_user.id
    await bot.send_message(chat_id, '<tg-spoiler>текст</tg-spoiler>')

@bot.message_handler(commands=['cc'])#гиперсылка на текст
async def send_welcome(message):
    chat_id=message.from_user.id
    await bot.send_message(chat_id, '<a href="https://www.youtube.com/?gl=RU&hl=ru">текст</a>')

@bot.message_handler(commands=['cp'])#скрывает под спойлер
async def send_welcome(message):
    chat_id=message.from_user.id
    await bot.send_message(chat_id, '<a href="tg://user?id=6159034023">inline mention of a user</a>')




@bot.message_handler(commands=['finish'])
async def send_welcome(message):
    await bot.reply_to(message, 'Конец')



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


import asyncio

asyncio.run(bot.polling())