
# # note
# please do pip/pip3 install the following
# geocoder
# pytz
# tzwhere

# from geopy.geocoders import Nominatim
import geocoder
from datetime import datetime
import pytz
from tzwhere import tzwhere

def curr_time_service() :
    # get current longitude latitude
    g = geocoder.ip('me')
    # print(g.latlng)
    the_set=g.latlng

    #initial tzwhere
    global tzwhere
    tzwhere= tzwhere.tzwhere()
    #find the timezone from current latitude / longitude
    timezone_str = tzwhere.tzNameAt(the_set[0], the_set[1]) # Seville coordinates
    #set the timezone into appropriate format
    timezone = pytz.timezone(timezone_str)
    #show the timezone
    # print(datetime.now(timezone))
    dict_result={}
    dict_result['date']=str(datetime.now(timezone).date())
    dict_result['time']=str(datetime.now(timezone).time())
    dict_result['timezone']=str(datetime.now(timezone).tzname())
    # print(dict_result)
    return dict_result
