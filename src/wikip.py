import wikipedia
import src.config as config

wikipedia.set_lang(config.LANGUAGE)

def search_inf():
    try:
        python_page = wikipedia.page(config.NAME_MAG)
        return python_page.original_title, python_page.summary, python_page.url
    except Exception as e:
        return config.WIKIP_FAILURE