import requests
import src.config as config
import telebot
import src.parser_crawler as pc
import random
import src.wikip as wikip
import json


bot = telebot.TeleBot(config.TOKEN) # WRITE TOKEN IN /src/config

@bot.message_handler(commands=['help'])
def help(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url=config.MY_URL
        )
    )
    bot.send_message(message.chat.id, config.HELP_INF, reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def welcome(message):
    form = random.randint(0, len(config.DF_FORMAT) - 1)
    sti = open(config.STIKER + f'{random.randint(0, config.SIZE_FORMAT[form] - 1)}.{config.DF_FORMAT[form]}', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton(config.SEARCH_IMAGE)
    item2 = telebot.types.KeyboardButton("STOP")
    item3 = telebot.types.KeyboardButton(config.SEARCH_INF)

    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, config.WELCOME_MESSAGE.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['find_inf'])
def find_inf(message):
    bot.send_message(message.chat.id, config.FIND_INF_TXT)
    config.WHAT_SEARCH = 2

@bot.message_handler(commands=['find_image'])
def find_inf(message):
    bot.send_message(message.chat.id, config.FIND_IMAGE_TXT, parse_mode='html')
    config.WHAT_SEARCH = 1

@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == config.SEARCH_IMAGE:
        config.WHAT_SEARCH = 1
        bot.send_message(message.chat.id, config.WHAT_SEARCH_TXT)
    elif message.text == 'STOP':
        config.WHAT_SEARCH = 0
    elif message.text == config.SEARCH_INF:
        bot.send_message(message.chat.id, config.WHAT_SEARCH_TXT)
        config.WHAT_SEARCH = 2
    elif config.WHAT_SEARCH == 1:
        url_photo = pc.find_image(message)
        if url_photo != 'not found':
            bot.send_photo(message.chat.id, requests.get(url_photo).content)
        else:
            bot.send_message(message.chat.id, config.FAILURE, parse_mode='html')
    elif config.WHAT_SEARCH == 2:
        config.NAME_MAG = message.text
        page = wikip.search_inf()
        if isinstance(page, tuple):
            bot.send_message(message.chat.id, '<b>' + page[0] + '</b>', parse_mode='html')
            bot.send_message(message.chat.id, page[1])
            bot.send_message(message.chat.id, config.REFERENCE_SOURCE + page[2])
        else:
            bot.send_message(message.chat.id, page)
    elif config.WHAT_SEARCH == 0:
        bot.send_message(message.chat.id, config.CHOOSE_CATEGORY)

@bot.message_handler(content_types=['photo'])
def to_url(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    search_url = config.SEARCH_YANDEX_URL
    files = {'upfile': ('blob', downloaded_file, 'image/jpeg')}
    params = config.PARAMS
    response = requests.post(search_url, params=params, files=files)
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url = search_url + '?' + query_string
    bot.send_message(message.chat.id, img_search_url)

@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, config.STOP_TXT)

if __name__ == '__main__':
    bot.polling(none_stop=True)
