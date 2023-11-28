import telebot

bot = telebot.TeleBot('6882889245:AAEgnCKrNC4LRwXW1sENuXoZLJ173npDF_A')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Я заждался твоего сообщения!!')



bot.infinity_polling()