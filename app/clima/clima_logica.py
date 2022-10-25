
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'es'
owm = OWM('827dcd9f3e9640860a2d33906a40ea39', config_dict)
mgr = owm.weather_manager()


class ClimaLogica:

    @classmethod
    def clima(cls, lat, long):

        print("*"*30)
        weather_by_lat_and_lon = mgr.weather_at_coords(
            lat=lat, lon=long)
        
        weather_by_lat_and_lon = weather_by_lat_and_lon.weather
        print(weather_by_lat_and_lon)
        pressure_dict = weather_by_lat_and_lon.barometric_pressure()
        
        return dict({"temp": weather_by_lat_and_lon.temperature('celsius'),
                     "detail_status": weather_by_lat_and_lon.detailed_status,
                     "status": weather_by_lat_and_lon.status,
                     "pressure": [pressure_dict['press'],
                                  pressure_dict['sea_level']],
                     "wind": weather_by_lat_and_lon.wind(),
                     "rain": weather_by_lat_and_lon.rain,
                     "clouds": weather_by_lat_and_lon.clouds,
                     "humedad": weather_by_lat_and_lon.humidity})

    @classmethod
    def forecast(cls, lat, long):
        forecast = mgr.forecast_at_coords(lat=lat, lon=long, interval= '3h').forecast
        print(forecast)
        humedad = []
        temp = []
        fecha = []
        for weather in forecast:
            clima = {}
            print(weather.status,weather.reference_time("iso")) 
            print(weather.temperature('celsius'),weather.humidity )
            temp.append( weather.temperature('celsius')['temp'])
            humedad.append( weather.humidity)
            fecha.append( weather.reference_time("iso"))
        return dict({"humedad":humedad, "temp":temp, "fecha":fecha})