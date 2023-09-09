#!/home/nincepython/.Python311/FlaskTuts/.venv/bin/python3
##  app.run(debug=True, host='0.0.0.0', port=5000)
from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)
app.debug = True  # Enable debug mode


@app.route('/')
@app.route('/index')
def index():
    # return "CKEMI USTA. ME REAL-TIME me app.debug = True  # Enable debug mode"
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    # E MARRIM NGA FORMA KETE INFO
    city = request.args.get('city')

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        print("MEQE FUTET HAPESIRA BOSHE, DO ZGJEDHIM KUCOVA")
        # You could render "City Not Found" instead like we do below
        city = "Maarssen"

    weather_data = get_current_weather(city)

    # City is not found by API, kodi 200 eshte ook
    if not weather_data['cod'] == 200:
        return render_template('qyteti-nuk-u-gjet.html')
        # return "QYTETI-NUK-U-GJET"
    
    
    # Convert temperature to Celsius
    # temp_celsius = f"(weather_data['main']['temp'] - 32) * 5/9)"
    # Convert temperature to Celsius using the formula
    temperature_fahrenheit = weather_data['main']['temp']
    temperature_celsius = (temperature_fahrenheit - 32) * 5/9

    feels_like_F = weather_data['main']['feels_like']
    feels_like_C = (feels_like_F - 32) * 5/9

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{temperature_celsius:.1f}",        
        feels_like=f"{feels_like_C:.1f}"
    )


if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=5000)
    # serve(app, host="0.0.0.0", port=5000, debug=True)

    app.run(debug=True, host="0.0.0.0", port=5000)

