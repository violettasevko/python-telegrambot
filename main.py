import telebot
from telebot import types

bot = telebot.TeleBot('5460437461:AAGKzDqtx7togFZNRcrWsH6tUTN3VGLoPNQ')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'hi, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


#@bot.message_handler(content_types=['text'])
#def get_user_text(message):
#    if message.text == "Hi":
#        bot.send_message(message.chat.id, f"Hi, {message.from_user.first_name}", parse_mode='html')
#    elif message.text == "id":
#        bot.send_message(message.chat.id, f"Your id is {message.from_user.id}", parse_mode='html')
#    elif message.text == "photo":
#        photo = open('icon.png', 'rb')
#        bot.send_photo(message.chat.id, photo)
#    else:
#        bot.send_message(message.chat.id, "Invalid input", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Wow!", parse_mode='html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("go to inst", url="https://instagram.com/violettaexe"))
    bot.send_message(message.chat.id, "go to site!", reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('site')
    start = types.KeyboardButton('start')
    markup.add(website, start)
    bot.send_message(message.chat.id, "go to site!", reply_markup=markup, parse_mode='html')


bot.polling(none_stop=True)
