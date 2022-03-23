import telebot

bot = telebot.TeleBot('5195333026:AAFyPOxPjzXMEHKbWaGYrMhtaFqh2l3oqmg')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Hello!</b>', parse_mode='html')

bot.polling(none_stop=True)

