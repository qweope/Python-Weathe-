import requests
from typing import Optional, Dict, Any


def get_weather(api_key: str, city: str) -> Optional[Dict[str, Any]]:
    """"
    функция для получения погоды
    """
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        return {
            'city': data['name'],
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    return None


if __name__ == '__main__':
    # пример использования
    api_key = 'da0476bc32edd94e526b4ddbfec4b95a'
    city = input('Введите название города: ')
    weather = get_weather(api_key, city)

    if weather:
        print(f"Текущая погода в городе {weather['city']}: {weather['temp']}°C, {weather['description']}")
    else:
        print('Не удалось получить данные о погоде')