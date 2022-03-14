
# # note
# please do pip/pip3 install the following
# geocoder
# pytz
# tzwhere


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

    #get IP address (current) & get latitude
    g = geocoder.ip('me')
    the_set=g.latlng

    #initial tzwhere
    t_tz= tzwhere.tzwhere()
    #find the timezone from current latitude / longitude
    
    #put location inside tzwhere
    timezone_str = t_tz.tzNameAt(the_set[0], the_set[1]) # Seville coordinates
    #for mannual debug latitude/longtude
    # timezone_str = t_tz.tzNameAt(44.566922, -123.304536) # Seville coordinates
    
    #set the timezone into appropriate format
    timezone = pytz.timezone(timezone_str)
    
    #do localize to get time offset
    mydt = timezone.localize(datetime.now())
    mydt=str(mydt)
    mydt=mydt[-6:]
    timezoneint=int(mydt[:3])
    dif_min=int(mydt[-2:])
    str_hr_tz=str(timezoneint)
    str_min_tz=str(dif_min)
    str_thetz=""
    if dif_min ==0:
        str_thetz=str_hr_tz
    elif dif_min == 45 or dif_min == 30 :
        str_thetz=str_hr_tz+str_min_tz
    

    #show the timezone by datetime (offline version)
    # print(datetime.now(timezone))
    # dict_result={}
    # dict_result['date']=str(datetime.now(timezone).date())
    # dump=str(datetime.now(timezone).time())
    # dict_result['time']=dump[:8]
    # dict_result['timezone']=str(datetime.now(timezone).tzname())
    # print(dict_result)

    #get time by internet url (UTC +0)
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
    #put UTC +00 time in datetime class
    current_time=datetime(ye,mt,dy,hrs,mins,secs)

    #calculate the difference between UTC+00 and the user's timezone
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

    #send output inform of dictionary
    dict_result={}
    dict_result['date']=str(current_time.date())
    dict_result['time']=str(current_time.time())   
    dict_result['timezone']=str_thetz
    return dict_result

#print output into the file
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

#check the command file function
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

#main infinity loop until user click enter
i = 0
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("date/time microservice is running Press Enter to stop it!")
    print (i)
    check_commandfile()
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        # line = raw_input()
        print("thanks for using date/time service")
        print("the microservice was closed")
        break
    i += 1