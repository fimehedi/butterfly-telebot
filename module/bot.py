import telebot
from dotenv import dotenv_values

config = dotenv_values('.env')

TOKEN = config['TOKEN']

Bot = telebot.TeleBot(TOKEN)