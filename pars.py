from bs4 import BeautifulSoup
import requests
import config

def parserJoke(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    anekdots = soup.findAll('div', class_='text')
    return [c.text for c in anekdots]
def parserNews(url):
    page = requests.get(url)
    try:
        soup = BeautifulSoup(page.text, "html.parser")
        LastNews = soup.findAll('div', class_='cell-list__list')
        String = ''

        for n in LastNews:
            if n.findAll(class_="cell-list__item-title"):
                String = n.text
        res = String.split(':')
        sa = ''
        for i in res:
            sa += i[:len(i) - 2] + '\n\n'
    except:
        sa = 'Не удалось получить новости('
    return sa
def parsWeather(city):
    if city != '':
        try:
            res = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.OpenWetherTOKEN}',
                params={'units': 'metric', 'lang': 'ru'})
            data = res.json()
            result = f'В городе {data["name"]} сегодня ' \
                  f'<b>{data["weather"][0]["description"]}</b>\n' \
                  f'Температура составляет <b>{data["main"]["temp"]}°C</b>\n' \
                  f'Макс.: <b>{data["main"]["temp_max"]}</b>°C, ' \
                  f'мин.: <b>{data["main"]["temp_min"]}°C</b>\n' \
                  f'Ощущается как <b>{data["main"]["feels_like"]}°C</b>\n' \
                  f'Влажность - <b>{data["main"]["humidity"]} %</b>\n' \
                  f'Скорость ветра - <b>{data["wind"]["speed"]} м/с</b>'
        except KeyError:
            result = 'Не удалось получить данные о погоде в указанном городе'
    else:
        result =f'Чтобы получить текущую погоду в указанном городе, после команды /weather <b>' \
             f'добавьте название интересующего вас города</b>.\n\nНапример:' \
             f'/weather <i>Омск</i>'
    return result