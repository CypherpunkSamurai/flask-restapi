"""
A weather rest api module for ../app (Twitter)

@author: Rakesh Chowdhury (github/CypherpunkSamurai)
"""
from flask import Blueprint, request
from app.weather.controller import get_weather_at

# namespace
ROUTE_NAMESPACE = 'weather'
# Blueprints for /weather
b_get_weather = Blueprint('get_weather', ROUTE_NAMESPACE)


# Methods
@b_get_weather.route("/", methods=['GET'])
def get_weather():
    """
    Get weather from given location (lat, lon). Return API response

    :return: json - Json Response from Third party API
    """

    # read args
    args = request.args

    lat = args.get("lat", default=None, type=float)
    lon = args.get("lon", default=None, type=float)

    # checks
    if not lat and not lon:
        return {"result": "error", "message": "lat and lon are required query parameters"}

    return get_weather_at(lat, lon)
