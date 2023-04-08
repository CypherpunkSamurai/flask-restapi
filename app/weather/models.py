# file ./app/weather/models.py
import os
from requests import get

OPENWEATHERMAP_KEY = os.getenv("OPENWEATHERMAP_KEY", "")


def openweathermap_query(lat: float, lon: float):
    """
    Get the weather at latitude and longitude

    :param lat:
    :param lon:
    :return:
    """

    # check for key
    if not len(OPENWEATHERMAP_KEY):
        raise Exception("OPENWEATHERMAP_KEY is not provided")

    # compose query url
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHERMAP_KEY}"

    # get weather
    with get(url, headers={"user-agent": "twitter-clone 1.0"}) as _r:
        # check error codes
        _r.raise_for_status()
        # return api response as json
        return _r.json()
