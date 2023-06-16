from telebot import TeleBot
from telebot.types import (Message,
                           ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup)
import random

bot = TeleBot("5821770300:AAFHKkXxwHJ633H-h4RzHwMWwcTVu7O9yFQ")
BAZE_FILES_DIR = r'C:\Users\user\PycharmProjects\pythonProject1\12311\lesson 2\extra'

def welcome_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = KeyboardButton('/cats')
    button2 = KeyboardButton('/poem')
    button3 = KeyboardButton('/stiker')
    button4 = KeyboardButton('/musik')
    button5 = KeyboardButton('/games')
    keyboard.add(button1, button2, button3, button4, button5)
    return keyboard
@bot.message_handler(commands=["start", "help",])
def welcome(message: Message):
    keyboard = welcome_keyboard()
    bot.send_message(message.from_user.id, "Привет, Выбери команду", reply_markup=keyboard)


@bot.message_handler(commands=["cats",])
def cats(message: Message):
    random_img_number = random.randint(1,9)
    random_img = open(fr'{BAZE_FILES_DIR}\{random_img_number}.jpg', 'rb')
    bot.send_photo(message.from_user.id, random_img)

@bot.message_handler(commands=["musik",])
def music(message: Message):
    audio = open(fr'{BAZE_FILES_DIR}\happy.mp3', 'rb')
    bot.send_audio(message.from_user.id, audio)

@bot.message_handler(commands=["poem"])
def poem(message: Message):
    bot.send_message(message.from_user.id, 'Висит груша, нельзя скушать')
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton(text='Перейти', url='https://stihi.ru')
    keyboard.add(button)
    bot.send_message(message.from_user.id, 'больше Стихов тут:', reply_markup=keyboard)
@bot.message_handler(commands=["stiker"])
def stiker(message: Message):
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAEG-AljpcsAAcPVqQt-8h2F1BLTovynlBwAAugcAAK97flJQpbz0pPKvAwsBA')
@bot.message_handler(commands=["games"])
def poem(message: Message):
    bot.send_message(message.from_user.id, 'Поиграть можно много во что')
    keyboard = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text='Экшены', url='https://store.steampowered.com/category/action/?snr=1_stats_7001__12')
    button2 = InlineKeyboardButton(text='Приключенческие игры', url='https://store.steampowered.com/category/adventure/?snr=1_stats_7001__12')
    button3 = InlineKeyboardButton(text='Ролевые игры', url='https://store.steampowered.com/category/rpg/?snr=1_stats_7001__12/')
    button4 = InlineKeyboardButton(text='Симуляторы', url='https://store.steampowered.com/category/simulation/?snr=1_stats_7001__12')
    button5 = InlineKeyboardButton(text='Стратегии', url='https://store.steampowered.com/category/strategy/?snr=1_stats_7001__12')
    button6 = InlineKeyboardButton(text='Спорт и гонки ', url='https://store.steampowered.com/category/sports_and_racing/?snr=1_stats_7001__12')
    keyboard.add(button1,button2,button3,button4,button5,button6)
    bot.send_message(message.from_user.id, 'Игры в стиме:', reply_markup=keyboard)


bot.polling()