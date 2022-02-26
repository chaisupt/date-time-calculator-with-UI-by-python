
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
import string
import os
import time
import sys
import select
from urllib.request import urlopen
from datetime import timedelta


def curr_time_service() :
    # get current longitude latitude
    g = geocoder.ip('me')
    # print(g.latlng)
    the_set=g.latlng

    #initial tzwhere
    # global tzwhere
    t_tz= tzwhere.tzwhere()
    #find the timezone from current latitude / longitude
    timezone_str = t_tz.tzNameAt(the_set[0], the_set[1]) # Seville coordinates
    # timezone_str = t_tz.tzNameAt(44.566922, -123.304536) # Seville coordinates
    #set the timezone into appropriate format
    timezone = pytz.timezone(timezone_str)
    # print(timezone)
    # print("here there is ...................localize")
    mydt = timezone.localize(datetime.now())
    # print(mydt)
    mydt=str(mydt)
    mydt=mydt[-6:]
    # print(mydt)
    timezoneint=int(mydt[:3])
    dif_min=int(mydt[-2:])
    str_hr_tz=str(timezoneint)
    str_min_tz=str(dif_min)
    str_thetz=""
    if dif_min ==0:
        str_thetz=str_hr_tz
    elif dif_min == 45 or dif_min == 30 :
        str_thetz=str_hr_tz+str_min_tz
    

    #show the timezone by datetime
    # print(datetime.now(timezone))
    # dict_result={}
    # dict_result['date']=str(datetime.now(timezone).date())
    # dump=str(datetime.now(timezone).time())
    # dict_result['time']=dump[:8]
    # dict_result['timezone']=str(datetime.now(timezone).tzname())
    # print(dict_result)

    #show time by internet url
    res = urlopen('http://just-the-time.appspot.com/')
    result = res.read().strip()
    time_str = result.decode('utf-8') #2017-07-28 04:53:46
    ye=time_str[:4]
    ye=int(ye)
    mt=time_str[5:]
    mt=mt[:2]
    mt=int(mt)
    dy=time_str[8:]
    dy=dy[:2]
    dy=int(dy)
    hrs=time_str[11:]
    hrs=hrs[:2]
    hrs=int(hrs)
    mins=time_str[14:]
    mins=mins[:2]
    mins=int(mins)
    secs=time_str[17:]
    secs=secs[:2]
    secs=int(secs)
    current_time=datetime(ye,mt,dy,hrs,mins,secs)
    # print("test datatime.......................")
    # print(current_time)
    negat=False
    if(timezoneint<0):
        negat=True
        timezoneint=timezoneint*(-1)
    if negat == True:
        current_time=current_time-timedelta(hours=timezoneint)    
        if dif_min != 0:
            current_time=current_time-timedelta(minutes=dif_min)
    else :
        current_time=current_time+timedelta(hours=timezoneint)
        if dif_min != 0:
            current_time=current_time+timedelta(minutes=dif_min)

    dict_result={}
    dict_result['date']=str(current_time.date())
    dict_result['time']=str(current_time.time())
    # dict_result['timezone']=str(datetime.now(timezone).tzname())     
    dict_result['timezone']=str_thetz
    # print(dict_result)
    return dict_result

def doit():
    #setup output
    firstline="date,time,time_zone\n"
    ddict=curr_time_service()
    secondline=ddict["date"] + ","+ ddict["time"] + "," + ddict["timezone"]
    # print(secondline)
    rs_file=open("dtz_res.csv","w")
    rs_file.write(firstline)
    rs_file.write(secondline)
    rs_file.flush()
    rs_file.close()

def check_commandfile():
    command_file=open("command_dtz.txt","r")
    commander=command_file.readline()
    commander=commander.replace("\n","")
    command_file.close()
    if(commander=="req"):
        command_file=open("command_dtz.txt","w")
        command_file.write(" ")
        command_file.flush()
        command_file.close()
        doit()


print("service is running please press control+c to quit system")
while True:
    try:
        check_commandfile()
    except KeyboardInterrupt:
        print(" \nthe service was closed thank you for using time service")
        break
