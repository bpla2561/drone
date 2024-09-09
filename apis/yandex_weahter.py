import requests


GEOCODER_API_KEY = 'e60936ce-1b32-4fde-af6b-5f331d3e0cb7' # from https://developer.tech.yandex.com/services/3
WEATHER_ACCESS_KEY = '96a20efc-e156-473a-8fe0-89c630d2b4ac' # https://yandex.ru/pogoda/b2b/console/api-page
CITY_NAME = 'Москва'


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
