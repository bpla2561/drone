from dotenv import load_dotenv
from dotenv import dotenv_values
import os
import requests

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

geocoder_api_key = os.getenv('GEOCODER_API_KEY')
weather_access_key = os.getenv('WEATHER_ACCESS_KEY')
city_name = os.getenv('CITY_NAME')

class Get_weather:
    def __init__(self, city_name, geocoder_api_key, weather_access_key) -> None:
        self.city_name = city_name
        self.geocoder_api_key = geocoder_api_key
        self.weather_access_key = weather_access_key

    def get_coordinates_by_city_name(self):
        base_url = 'https://geocode-maps.yandex.ru/1.x/'
        params = {
            'format': 'json',
            'geocode': self.city_name,
            'apikey': self.geocoder_api_key
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            result = response.json()
            coords = result['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
            if coords:
                self.coords = coords
            else:
                print('Не удалось получить координаты города.')
        else:
            print(f'Ошибка при получении данных: {response.text}')
            return None, None

    def get_weather(self):

        latitude = float(self.coords[0])
        longitude = float(self.coords[1])
          
        headers = {
            'X-Yandex-Weather-Key': self.weather_access_key
        }
        url = f'https://api.weather.yandex.ru/v2/forecast?lat={latitude}&lon={longitude}'
        response = requests.get(url, headers=headers)
        return response.json()["fact"]['wind_speed']
