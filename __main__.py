import asyncio
import requests
import json

from random import randint
from dotenv import dotenv_values

from telebot.async_telebot import AsyncTeleBot, types
from telebot.formatting import mbold

config = dotenv_values()
bot = AsyncTeleBot(config['API_KEY'])

with open("./settings.json") as fp: settings = json.load(fp)

@bot.message_handler(commands=['Начать', 'начать', 'start'])
async def start_menu(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_lotery = types.KeyboardButton("Гача")
    button_funny = types.KeyboardButton("Разное")
    markup.add(button_funny, button_lotery)

    text='''
Мои доступные команды:

🟩<b> Категория разного </b>🟩
<blockquote> цитата, кубик </blockquote>

🟪<b> Категория гачи </b>🟪
<blockquote> профиль, работа, крутка, лидеры </blockquote>
    '''
    await bot.send_message(m.chat.id, text=text, reply_markup=markup, parse_mode="html")

@bot.message_handler(commands=['гача', 'Гача'])
async def gacha_menu(m):
    pass

@bot.message_handler(content_types=['text'])
async def main_func(m):
    if (m.text in ['цитата', 'Цитата']):
        responce = requests.get(settings['quote']['url'], params=settings['quote']['get']).json()
        text = f"<blockquote><b>{responce["quoteText"]}</b></blockquote>\n\nАвтор: <code>{responce["quoteAuthor"] if responce["quoteAuthor"] != '' else "UNKNOW"}</code>"
        await bot.send_message(m.from_user.id, text, parse_mode="html")

    elif (m.text in ['Кубик', 'кубик']):
        dice_1, dice_2 = randint(1, 6), randint(1, 6)
        text = f"⠀🎲 🎲 \n<code> ({dice_1})({dice_2}) >> [{dice_1 + dice_2}] </code>"
        await bot.send_message(m.from_user.id, text, parse_mode="html")

    else:
        pass


print("Bot started")
asyncio.run(bot.polling(none_stop=True, interval=1)) 