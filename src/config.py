TOKEN = # bot token from @BorFather (YOUR TOKEN)

WELCOME_MESSAGE = "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>," \
                  "бот созданный чтобы искать картинки, статьи.\nВыбери категорию, напиши слово, а я найду :)"
PATH_IMAGE = 'image'
SIZE = 15
STIKER = 'image/welcome_'
DF_FORMAT = ['webp', 'tgs']
SIZE_FORMAT = [2, 2]
LANGUAGE = 'ru'
NAME_MAG = 'Словарь'
WHAT_SEARCH = 0

FIND_INF_TXT = 'Помогу чем смогу!\nКакую информацию мне найти?'
FIND_IMAGE_TXT = 'Пиши скорее какое <b>фото</b> тебе найти!'

GPTTEXT = "gpt2-medium"
CHAT_MESSAGE = False
CHAT_HISTORY = None
YANDEX_URL = 'https://yandex.ru/images/search?text='
SEARCH_YANDEX_URL = 'https://yandex.ru/images/search'
PARAMS = {'rpt': 'imageview', 'format': 'json',
          'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'
          }
MY_URL = # YOUR REFERENCE TO tg "'telegram.me/...."

HELP_INF = "Я - умный tg-bot, способный искать изображения и статьи.\n"\
                                      "Для поиска нужно выбрать категорию, а затем просто ввести слово "\
                                      "или отправить фотографию, если хотите найти на нее ссылку"
STOP_TXT = "Пока-пока! Приходи снова :)"
FAILURE = "К сожалению, фото не найдено, попробуйте <b>еще</b> раз!"
SEARCH_INF = "Найди информацию"
SEARCH_IMAGE = "Найди фото"
WHAT_SEARCH_TXT = 'Что вы хотите найти?'
CHOOSE_CATEGORY = 'Пожалуйста, выбери категорию'
REFERENCE_SOURCE = 'Ссылка на источник:'
WIKIP_FAILURE = 'К сожалению, такой информации не найдено :('
