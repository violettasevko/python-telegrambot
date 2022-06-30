import telebot

bot = telebot.TeleBot('5460437461:AAGKzDqtx7togFZNRcrWsH6tUTN3VGLoPNQ')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'hi, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == "Hi":
        bot.send_message(message.chat.id, f"Hi, {message.from_user.first_name}", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Your id is {message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Invalid input", parse_mode='html')


bot.polling(none_stop=True)
