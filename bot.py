import telebot
from bot_token import token, file_path
import matplotlib.pyplot as plt
from samila import GenerativeImage

#bot init
bot = telebot.TeleBot(token)

#start
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Generate art!', callback_data='art'))
    bot.send_message(message.chat.id, text="This bot makes beauty out of pure math", reply_markup=markup) 

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    markup = telebot.types.InlineKeyboardMarkup()
    if call.data == 'art':
        bot.send_message(call.message.chat.id, text="Moments of creation.. doing some magic..", reply_markup=markup) 
        g = GenerativeImage()
        g.generate()
        g.plot()
        g.save_image(file_adr=file_path)

        markup.add(telebot.types.InlineKeyboardButton(text='I want more =)', callback_data='art'))
        img = open(file_path, 'rb')
        bot.send_photo(call.message.chat.id, img, reply_markup=markup)


bot.polling(none_stop=True, interval=0)
