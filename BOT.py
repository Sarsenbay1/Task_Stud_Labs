import telebot, random
import requests
from bs4 import BeautifulSoup
from config import TOKEN
import config
import pars


def telegramBot():

    bot = telebot.TeleBot(TOKEN)  # указать полное имя класса TeleBot


    @bot.message_handler(commands=['start'])
    def start(message):
        mess = f'Привет, {message.from_user.first_name}'
        bot.send_message(message.chat.id, f'{mess}\n\n{config.comm}')


    @bot.message_handler(commands=['help'])
    def help(message):
        bot.send_message(message.chat.id, config.comm)


    @bot.message_handler(commands=['weather'])
    def weather(message):
        chat_id = message.chat.id
        city = telebot.util.extract_arguments(message.text)
        bot.send_message(message.chat.id, pars.parsWeather(city), parse_mode='html')



    @bot.message_handler(commands=['echo'])
    def echo_1(message):
        word = telebot.util.extract_arguments(message.text)
        if word !="":
            bot.send_message(message.chat.id, word)
        else:
            bot.send_message(message.chat.id, "Чтобы получить ответ - эхо, после коммндаы /echo"
                                              "добавьте текст\n\nНапример:"
                                              "/echo <текст>")

    @bot.message_handler(commands=['news'])
    def News(massage):
        news = pars.parserNews(config.urlNews)
        bot.send_message(massage.chat.id, news)


    @bot.message_handler(commands=['joke'])
    def jokes(message):
        list_of_jokes = pars.parserJoke(config.urlJoke)
        random.shuffle(list_of_jokes)

        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]

    @bot.message_handler(commands=['stop'])
    def stop_com(message):
        mess = f'Пока, {message.from_user.first_name}'
        bot.send_message(message.chat.id, f'{mess}, заходи ещё!!!')
        bot.stop_polling()




    bot.polling(none_stop=True)
