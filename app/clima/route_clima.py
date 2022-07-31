import json
from . import clima
import sys
from flask import request, jsonify

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'es'
owm = OWM('827dcd9f3e9640860a2d33906a40ea39',config_dict)
mgr = owm.weather_manager()

@clima.route('/coordenadas')
def clima():
    data = mgr.weather_around_coords(lat=2.88313745918226,lon=-75.2663908840393, limit=2)
    #weather = data.weather
    print("*"*30)
    #print(weather.status)           # short version of status (eg. 'Rain')
    #print(weather.detailed_status)
    list_of_observations = mgr.weather_around_coords(lat=2.88313745918226,lon=-75.266390884039, limit=1)
    corresponding_weathers_list = [ obs.weather for obs in list_of_observations ]
    print("*"*30)
    for d in corresponding_weathers_list:
        print(d.detailed_status)
        print(d.temperature('celsius'))
        print(d.rain)
    return "data"


