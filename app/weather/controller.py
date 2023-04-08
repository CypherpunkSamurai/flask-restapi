# file: ./app/weather/controller.py
from app.weather.models import openweathermap_query


def get_weather_at(lat: float, lon: float):
    """
    Get weather at latitude and longitude

    :param lat:
    :param lon:
    :return:
    """

    try:
        return openweathermap_query(lat, lon)
    except Exception as e:
        return {"result": "error", "message": f"there was a error while fetching openweathermap data. {e}"}
