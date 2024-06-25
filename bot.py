from telebot import TeleBot
from telebot.types import (Message, InlineKeyboardMarkup,
                           InlineKeyboardButton, WebAppInfo)


bot = TeleBot('https://kasramoradi-0.github.io/notcoin/')


@bot.message_handler(commands=['start'])
def start(message: Message):
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Your MiniApp',
                              web_app=WebAppInfo(
                                  ''
                              ))]
    ])

    bot.send_message(chat_id=message.chat.id, text='بفرمایید وب اپ شما:', reply_markup=markup)


if __name__ == '__main__':
    bot.polling(skip_pending=True)
