#!/home/nincepython/.Python311/FlaskTuts/.venv/bin/python3

from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# NGARKOJME ENV, KU KEMI API PER WEATHERIN
load_dotenv()

def get_current_weather(city="Maarssen, NL"):
    # &q eshte query
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    # i marrim te dhenat dhe i kalojme ne json
    weather_data = requests.get(request_url).json()

    return weather_data
    
if __name__ == "__main__":
    print('\n*** MARRIM KUSHTET E MOTIT ***\n')

    city = input("\n FUSNI QYTETIN: \n")

    # Check for empty strings or string with only spaces
    # This step is not required here
    if not bool(city.strip()):
        # JEPI NJE DEFAULT QYTET
        city = "Maarssen"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)


# FUSNI QYTETIN: 
# Kucove


# {'base': 'stations',
#  'clouds': {'all': 0},
#  'cod': 200,
#  'coord': {'lat': 40.8003, 'lon': 19.9167},
#  'dt': 1694301035,
#  'id': 3185060,
#  'main': {'feels_like': 70.92,
#           'grnd_level': 1008,
#           'humidity': 50,
#           'pressure': 1015,
#           'sea_level': 1015,
#           'temp': 71.69,
#           'temp_max': 71.69,
#           'temp_min': 71.69},
#  'name': 'Kuçovë',
#  'sys': {'country': 'AL', 'sunrise': 1694319339, 'sunset': 1694365181},
#  'timezone': 7200,
#  'visibility': 10000,
#  'weather': [{'description': 'clear sky',
#               'icon': '01n',
#               'id': 800,
#               'main': 'Clear'}],
#  'wind': {'deg': 86, 'gust': 4.54, 'speed': 5.08}}