from flask import jsonify
from apis.yandex_weahter import Get_weather
import logging

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

GEOCODER_API_KEY = 'e60936ce-1b32-4fde-af6b-5f331d3e0cb7' # from https://developer.tech.yandex.com/services/3
WEATHER_ACCESS_KEY = '96a20efc-e156-473a-8fe0-89c630d2b4ac' # https://yandex.ru/pogoda/b2b/console/api-page
CITY_NAME = 'Москва'
MAX_WIND_SPEED = 10

def weathercheck():
    def decorator(func):
        def wrapper(*args, **kwargs):
            GEOCODER_API_KEY = 'e60936ce-1b32-4fde-af6b-5f331d3e0cb7' # from https://developer.tech.yandex.com/services/3
            WEATHER_ACCESS_KEY = '96a20efc-e156-473a-8fe0-89c630d2b4ac' # https://yandex.ru/pogoda/b2b/console/api-page
            CITY_NAME = 'Москва'
            get_weather = Get_weather(CITY_NAME, GEOCODER_API_KEY,WEATHER_ACCESS_KEY)
            coords = get_weather.get_coordinates_by_city_name()
            wind_speed = float(get_weather.get_weather())
            logging.info(wind_speed)
            if wind_speed > MAX_WIND_SPEED:
                logging.info(f"Полет запрещен: нелетная погода. Скорость веьтра: {wind_speed}")
                return jsonify({"index": "Полет запрещен: нелетная погода"}), 200
            logging.info("Полет разрешен: летная погода")
            return func(*args, **kwargs)
        return wrapper 
    return decorator