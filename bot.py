import telebot

bot = telebot.Telebot('5195333026:AAFyPOxPjzXMEHKbWaGYrMhtaFqh2l3oqm')

@bot.message_handlers(commands=['start'])
