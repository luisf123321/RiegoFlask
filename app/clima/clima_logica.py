
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
    def clima(cls):

        print("*"*30)
        weather_by_lat_and_lon = mgr.weather_at_coords(
            lat=2.88313745918226, lon=-75.2663908840393)
        
        weather_by_lat_and_lon = weather_by_lat_and_lon.weather
        print(weather_by_lat_and_lon)
        pressure_dict = weather_by_lat_and_lon.barometric_pressure()
        forecast = mgr.forecast_at_coords(lat=2.88313745918226, lon=-75.2663908840393, interval= '3h').forecast
        print(forecast)
        for weather in forecast:
            print(weather.status,weather.reference_time("iso")) 
            for x in weather:
                print(x)
        return dict({"temp": weather_by_lat_and_lon.temperature('celsius'),
                     "detail_status": weather_by_lat_and_lon.detailed_status,
                     "status": weather_by_lat_and_lon.status,
                     "pressure": [pressure_dict['press'],
                                  pressure_dict['sea_level']],
                     "wind": weather_by_lat_and_lon.wind(),
                     "rain": weather_by_lat_and_lon.rain,
                     "clouds": weather_by_lat_and_lon.clouds,
                     "humedad": weather_by_lat_and_lon.humidity})
