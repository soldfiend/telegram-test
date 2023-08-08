import telebot
import webbrowser

bot = telebot.TeleBot('6671431226:AAHHShH1L2z7mLn5FHMsLg1gUK0tZKxXtEQ')


@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('http:/google.com')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)
