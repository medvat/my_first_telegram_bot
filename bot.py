import telebot

bot = telebot.Telebot('5195333026:AAFyPOxPjzXMEHKbWaGYrMhtaFqh2l3oqmq')

@bot.message_handlers(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Hello!<b>', parse_mode='html')

bot.polling(none_stop=True)

