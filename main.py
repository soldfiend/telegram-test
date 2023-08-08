import telebot
from telebot import types

bot = telebot.TeleBot('6671431226:AAHHShH1L2z7mLn5FHMsLg1gUK0tZKxXtEQ')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('site')
    markup.row(btn1)
    btn2 = types.KeyboardButton('delete')
    btn3 = types.KeyboardButton('Change text')
    markup.row(btn2, btn3)
    file = open('./Python_urok_01_1580308407.pdf', 'rb')
    bot.send_document(message.chat.id, file)
    # bot.send_message(message.chat.id, 'Hello', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'site':
        bot.send_message(message.chat.id, 'Web site is open')
    elif message.text == 'delete':
        bot.send_message(message.chat.id, 'delete')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Go site', url='https://google.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Delete photo', callback_data='Delete')
    btn3 = types.InlineKeyboardButton('Change text', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


# @bot.message_handler(commands=['site'])
# def site(message):
#     webbrowser.open('http:/google.com')
#
#
# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}')
#
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'hello':
#         bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)
