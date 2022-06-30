import telebot

bot = telebot.TeleBot('5460437461:AAGKzDqtx7togFZNRcrWsH6tUTN3VGLoPNQ')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'hi, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True)
