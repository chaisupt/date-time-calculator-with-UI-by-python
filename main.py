# from mservice import *
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import string
import os
import time
from datetime import timedelta
from datetime import datetime
# geocoder
# pytz
# tzwhere
# brew install python-tk 

#microservice prototype
# my_d=curr_time_service()
# print(my_d)

#main cal window setup
root_cal=Tk()
root_cal.title("Clocksys.Calculator")
# root_cal.geometry("500x500")
root_cal.configure(bg="white")
menu_cal=Menu()
root_cal.config(menu=menu_cal)

#main world window setup
root_wd=Tk()
root_wd.title("Clocksys.World_Clock")
# root_wd.geometry("500x500")
root_wd.configure(bg="white")
menu_wd=Menu()
root_wd.config(menu=menu_wd)

#button function
def lastup():
    wd_up=Tk()
    wd_up.title("Last update")
    wd_up.configure(bg="white")

    lb_update_content=Label(wd_up,text="this is version 0.0 there is no any update yet",font=("Arial",14)).pack()

    wd_up.mainloop()

def helpWindow():
    wd_help=Tk()
    wd_help.title("Help page")
    wd_help.geometry("1200x700")
    wd_help.configure(bg="white")
    
    lb_helpcontent=Label(wd_help,text="The help instruction picture will be here" , font=("Arial",60)).pack()

    wd_help.mainloop()


def exit_cal():
    root_cal.destroy()

def exit_wd():
    root_wd.destroy()

def confirmemail():
    input_email_io=cal_email.get()
    input_email=cal_input_email.get()
    if input_email_io=="yes" and input_email!="":
        tkinter.messagebox.showinfo("email confirmation","the result has been sent!")
    elif input_email_io=="yes" and input_email=="":
        tkinter.messagebox.showerror("Error: email confirmation","Sorry! the result email cannot be sent")

def submit_func():
    from_input_time=cal_input_time.get()
    from_input_date=cal_input_date.get()
    from_input_timezone=cal_input_tz.get()
    from_input_daytime=cal_input_daytime.get()
    to_input_timezone=cal_output_tz.get()
    to_input_daytime=cal_output_daytime.get()
    input_email_io=cal_email.get()
    input_email=cal_input_email.get()


    if from_input_time=="" or from_input_date=="" or from_input_timezone=="" or from_input_daytime=="" or to_input_timezone=="" or to_input_daytime==""or input_email_io=="" :
        tkinter.messagebox.showerror("Error: not enough input","Your input is not enough for the calculation")
    else :
        confirmemail()

def date_time_return():
    commanding_word="req"
    fs=open("command_dtz.txt","w")
    fs.write(commanding_word)
    fs.close()
    time.sleep(4)
    fs=open("dtz_res.csv","r")
    reading=fs.readline()
    reading=fs.readline()
    fs.close()
    reading=reading.replace("\n","")
    string_group=reading.split(",")
    s_date=string_group[0]
    # s_date=str(s_date)
    s_time=string_group[1]
    # s_time=str(s_time)
    # s_year=s_date[:4]
    # s_year=int(s_year)
    # s_month=s_date[5:]
    # s_month=s_month[:2]
    # s_month=int(s_month)
    # s_day=s_date[8:]
    # s_day=int(s_day)
    # s_hr=s_time[:2]
    # s_hr=int(s_hr)
    # s_min=s_time[3:]
    # s_min=s_min[:2]
    # s_min=int(s_min)
    # s_sec=s_time[6:]
    # s_sec=int(s_sec)
    # date_result=datetime(s_year,s_month,s_day,s_hr,s_min,s_sec)
    s_tz=string_group[2]
    # return date_result,s_tz
    return s_date,s_time,s_tz
    

def current_loc_time():    
    s_date,s_time,s_tz=date_time_return()
    et_wd_rstime.delete(0,"end")
    et_wd_rstime.insert(0,s_time)
    et_wd_rsdate.delete(0,"end")
    et_wd_rsdate.insert(0,s_date)
    et_wd_rstz.delete(0,"end")
    et_wd_rstz.insert(0,"UTC"+s_tz)


def wd_reset_clock(h1,m1,s1,d1,z1):
    #hr min sec
    h1=int(h1)
    m1=int(m1)
    s1=int(s1)
    #year
    ye1=d1[:4]
    ye1=int(ye1)
    #month
    mt1=d1[5:]
    mt1=mt1[:2]
    mt1=int(mt1)
    #day
    dy1=d1[8:]
    dy1=int(dy1)
    current_time=datetime(ye1,mt1,dy1,h1,m1,s1)
    #checkzone
    z1=int(z1)
    negat=False
    dif_min=0
    if(z1<0):
        negat=True
        z1=z1*(-1)
    if(z1%100==30 or z1%100==45):
        dif_min=z1%100
        z1=z1/100
    
    #main calculation part
    if negat is True:
        current_time=current_time+timedelta(hours=z1)
        if dif_min != 0 :
            current_time=current_time+timedelta(minutes=dif_min)
    else :
        current_time=current_time-timedelta(hours=z1)
        if dif_min != 0:
            current_time=current_time-timedelta(minutes=dif_min)
    
    return current_time
    
def time2zone(std_time,tz_hr,tz_min,dsaving1,dsaving2):
    negat=False
    if(tz_hr<0):
        negat=True
        tz_hr=tz_hr*(-1)
    if dsaving1 == "yes":
        std_time=std_time-timedelta(hours=1)
    #main coverter
    if negat is True:
        std_time=std_time-timedelta(hours=tz_hr)
        if tz_min != 0:
            std_time=std_time-timedelta(minutes=tz_min)
    else:
        std_time=std_time+timedelta(hours=tz_hr)
        if tz_min != 0:
            std_time=std_time+timedelta(minutes=tz_min)
    if dsaving2 == "yes":
        std_time=std_time+timedelta(hours=1)
    
    return std_time

def wd_search_command():
    s_date,s_time,s_tz=date_time_return()
    #hr min sec
    hr=s_time[:2]
    minute=s_time[3:]
    minute=minute[:2]
    sec=s_time[6:]
    result_time=wd_reset_clock(hr,minute,sec,s_date,s_tz)
    wanted_timezone=cm_adv.get()
    print(wanted_timezone)
    wanted_timezone=wanted_timezone[:10]
    wanted_timezone=wanted_timezone[4:]
    tz_hr=wanted_timezone[:3]
    tz_hr=int(tz_hr)
    tz_min=wanted_timezone[4:]
    tz_min=int(tz_min)
    result_time=time2zone(result_time,tz_hr,tz_min,"no","no")
    et_wd_rstime.delete(0,"end")
    et_wd_rstime.insert(0,str(result_time.time()))
    et_wd_rsdate.delete(0,"end")
    et_wd_rsdate.insert(0,str(result_time.date()))
    et_wd_rstz.delete(0,"end")
    dummytz="UTC"+str(tz_hr)
    et_wd_rstz.insert(0,dummytz)
    


#main cal
# menu
menu_cal.add_command(label="History")
menu_cal.add_command(label="last update info",command=lastup)
menu_cal.add_command(label="help",command=helpWindow)
menu_cal.add_command(label="exit",command=exit_cal)

#pseudo menu for mac
bt_cal_history=Button(root_cal,text="History").grid(row=17,column=0)
bt_cal_lastup=Button(root_cal,text="last update info",command=lastup).grid(row=18,column=0)
bt_cal_help=Button(root_cal,text="help",command=helpWindow).grid(row=19,column=0)
bt_cal_exit=Button(root_cal,text="exit",command=exit_cal).grid(row=20,column=0)

#content
lb_cal_main=Label(root_cal ,text="Clock Calculator",fg="black",bg="white",font=("Arial",18)).grid(row=0,column=0)
lb_cal_from=Label(root_cal,text="From",fg="black",bg="white",font=("Arial",14)).grid(row=1,sticky=W)
lb_cal_input_time=Label(root_cal,text="time in 24hr (XX:XX): ",fg="black",bg="white").grid(row=2,sticky=W)
cal_input_time=StringVar()
et_cal_input_time=Entry(root_cal,textvariable=cal_input_time,width=10).grid(row=2,column=1,sticky=W)
lb_cal_input_date=Label(root_cal,text="date (YYYY/MM/DD): ",fg="black",bg="white").grid(row=3,sticky=W)
cal_input_date=StringVar()
et_cal_input_date=Entry(root_cal,textvariable=cal_input_date,width=15).grid(row=3,column=1,sticky=W)
lb_cal_input_tz=Label(root_cal,text="timezone: ",fg="black",bg="white").grid(row=4,sticky=W)
cal_input_tz=StringVar()
cm_input_tz=ttk.Combobox(root_cal,textvariable=cal_input_tz,width=45)
cm_input_tz["values"]=("(UTC-12:00) International Date Line West","(UTC-11:00) Coordinated Universal Time-11","(UTC-10:00) Hawaii","(UTC-09:00) Alaska","(UTC-08:00) Baja California","(UTC-08:00) Pacific Time (US and Canada)","(UTC-07:00) Chihuahua, La Paz, Mazatlan","(UTC-07:00) Arizona","(UTC-07:00) Mountain Time (US and Canada)","(UTC-06:00) Central America","(UTC-06:00) Central Time (US and Canada)","(UTC-06:00) Saskatchewan","(UTC-06:00) Guadalajara, Mexico City, Monterey","(UTC-05:00) Bogota, Lima, Quito","(UTC-05:00) Indiana (East)","(UTC-05:00) Eastern Time (US and Canada)","(UTC-04:30) Caracas","(UTC-04:00) Atlantic Time (Canada)","(UTC-04:00) Asuncion","(UTC-04:00) Georgetown, La Paz, Manaus, San Juan","(UTC-04:00) Cuiaba","(UTC-04:00) Santiago","(UTC-03:30) Newfoundland","(UTC-03:00) Brasilia","(UTC-03:00) Greenland","(UTC-03:00) Cayenne, Fortaleza","(UTC-03:00) Buenos Aires","(UTC-03:00) Montevideo","(UTC-02:00) Coordinated Universal Time-2","(UTC-01:00) Cape Verde","(UTC-01:00) Azores","(UTC+00:00) Casablanca","(UTC+00:00) Monrovia, Reykjavik","(UTC+00:00) Dublin, Edinburgh, Lisbon, London","(UTC+00:00) Coordinated Universal Time","(UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna","(UTC+01:00) Brussels, Copenhagen, Madrid, Paris","(UTC+01:00) West Central Africa","(UTC+01:00) Belgrade, Bratislava, Budapest, Ljubljana, Prague","(UTC+01:00) Sarajevo, Skopje, Warsaw, Zagreb","(UTC+01:00) Windhoek","(UTC+02:00) Athens, Bucharest, Istanbul","(UTC+02:00) Helsinki, Kiev, Riga, Sofia, Tallinn, Vilnius","(UTC+02:00) Cairo","(UTC+02:00) Damascus","(UTC+02:00) Amman","(UTC+02:00) Harare, Pretoria","(UTC+02:00) Jerusalem","(UTC+02:00) Beirut","(UTC+03:00) Baghdad","(UTC+03:00) Minsk","(UTC+03:00) Kuwait, Riyadh","(UTC+03:00) Nairobi","(UTC+03:30) Tehran","(UTC+04:00) Moscow, St. Petersburg, Volgograd","(UTC+04:00) Tbilisi","(UTC+04:00) Yerevan","(UTC+04:00) Abu Dhabi, Muscat","(UTC+04:00) Baku","(UTC+04:00) Port Louis","(UTC+04:30) Kabul","(UTC+05:00) Tashkent","(UTC+05:00) Islamabad, Karachi","(UTC+05:30) Sri Jayewardenepura Kotte","(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi","(UTC+05:45) Kathmandu","(UTC+06:00) Astana","(UTC+06:00) Dhaka","(UTC+06:00) Yekaterinburg","(UTC+06:30) Yangon","(UTC+07:00) Bangkok, Hanoi, Jakarta","(UTC+07:00) Novosibirsk","(UTC+08:00) Krasnoyarsk","(UTC+08:00) Ulaanbaatar","(UTC+08:00) Beijing, Chongqing, Hong Kong, Urumqi","(UTC+08:00) Perth","(UTC+08:00) Kuala Lumpur, Singapore","(UTC+08:00) Taipei","(UTC+09:00) Irkutsk","(UTC+09:00) Seoul Osaka Sapporo Tokyo","(UTC+09:30) Darwin","(UTC+09:30) Adelaide","(UTC+10:00) Hobart Yakutsk Brisbane Guam","(UTC+10:00) Canberra, Melbourne, Sydney","(UTC+11:00) Vladivostok","(UTC+11:00) Solomon Islands, New Caledonia","(UTC+12:00) Coordinated Universal Time+12","(UTC+12:00) Fiji, Marshall Islands Magadan Auckland Wellington","(UTC+13:00) Nuku'alofa Samoa")
cm_input_tz.grid(row=4,column=1,sticky=W)
lb_cal_input_daytime=Label(root_cal,text="day-time saving(yes/no): ",fg="black",bg="white").grid(row=5,sticky=W)
cal_input_daytime=StringVar()
cm_input_daytime=ttk.Combobox(root_cal,textvariable=cal_input_daytime,width=5)
cm_input_daytime["values"]=("yes","no")
cm_input_daytime.grid(row=5,column=1,sticky=W)
lb_cal_to=Label(root_cal,text="To",fg="black",bg="white",font=("Arial",14)).grid(row=6,sticky=W)
lb_cal_output_tz=Label(root_cal,text="timezone: ",fg="black",bg="white").grid(row=7,sticky=W)
cal_output_tz=StringVar()
cm_output_tz=ttk.Combobox(root_cal,textvariable=cal_output_tz,width=45)
cm_output_tz["values"]=("(UTC-12:00) International Date Line West","(UTC-11:00) Coordinated Universal Time-11","(UTC-10:00) Hawaii","(UTC-09:00) Alaska","(UTC-08:00) Baja California","(UTC-08:00) Pacific Time (US and Canada)","(UTC-07:00) Chihuahua, La Paz, Mazatlan","(UTC-07:00) Arizona","(UTC-07:00) Mountain Time (US and Canada)","(UTC-06:00) Central America","(UTC-06:00) Central Time (US and Canada)","(UTC-06:00) Saskatchewan","(UTC-06:00) Guadalajara, Mexico City, Monterey","(UTC-05:00) Bogota, Lima, Quito","(UTC-05:00) Indiana (East)","(UTC-05:00) Eastern Time (US and Canada)","(UTC-04:30) Caracas","(UTC-04:00) Atlantic Time (Canada)","(UTC-04:00) Asuncion","(UTC-04:00) Georgetown, La Paz, Manaus, San Juan","(UTC-04:00) Cuiaba","(UTC-04:00) Santiago","(UTC-03:30) Newfoundland","(UTC-03:00) Brasilia","(UTC-03:00) Greenland","(UTC-03:00) Cayenne, Fortaleza","(UTC-03:00) Buenos Aires","(UTC-03:00) Montevideo","(UTC-02:00) Coordinated Universal Time-2","(UTC-01:00) Cape Verde","(UTC-01:00) Azores","(UTC+00:00) Casablanca","(UTC+00:00) Monrovia, Reykjavik","(UTC+00:00) Dublin, Edinburgh, Lisbon, London","(UTC+00:00) Coordinated Universal Time","(UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna","(UTC+01:00) Brussels, Copenhagen, Madrid, Paris","(UTC+01:00) West Central Africa","(UTC+01:00) Belgrade, Bratislava, Budapest, Ljubljana, Prague","(UTC+01:00) Sarajevo, Skopje, Warsaw, Zagreb","(UTC+01:00) Windhoek","(UTC+02:00) Athens, Bucharest, Istanbul","(UTC+02:00) Helsinki, Kiev, Riga, Sofia, Tallinn, Vilnius","(UTC+02:00) Cairo","(UTC+02:00) Damascus","(UTC+02:00) Amman","(UTC+02:00) Harare, Pretoria","(UTC+02:00) Jerusalem","(UTC+02:00) Beirut","(UTC+03:00) Baghdad","(UTC+03:00) Minsk","(UTC+03:00) Kuwait, Riyadh","(UTC+03:00) Nairobi","(UTC+03:30) Tehran","(UTC+04:00) Moscow, St. Petersburg, Volgograd","(UTC+04:00) Tbilisi","(UTC+04:00) Yerevan","(UTC+04:00) Abu Dhabi, Muscat","(UTC+04:00) Baku","(UTC+04:00) Port Louis","(UTC+04:30) Kabul","(UTC+05:00) Tashkent","(UTC+05:00) Islamabad, Karachi","(UTC+05:30) Sri Jayewardenepura Kotte","(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi","(UTC+05:45) Kathmandu","(UTC+06:00) Astana","(UTC+06:00) Dhaka","(UTC+06:00) Yekaterinburg","(UTC+06:30) Yangon","(UTC+07:00) Bangkok, Hanoi, Jakarta","(UTC+07:00) Novosibirsk","(UTC+08:00) Krasnoyarsk","(UTC+08:00) Ulaanbaatar","(UTC+08:00) Beijing, Chongqing, Hong Kong, Urumqi","(UTC+08:00) Perth","(UTC+08:00) Kuala Lumpur, Singapore","(UTC+08:00) Taipei","(UTC+09:00) Irkutsk","(UTC+09:00) Seoul Osaka Sapporo Tokyo","(UTC+09:30) Darwin","(UTC+09:30) Adelaide","(UTC+10:00) Hobart Yakutsk Brisbane Guam","(UTC+10:00) Canberra, Melbourne, Sydney","(UTC+11:00) Vladivostok","(UTC+11:00) Solomon Islands, New Caledonia","(UTC+12:00) Coordinated Universal Time+12","(UTC+12:00) Fiji, Marshall Islands Magadan Auckland Wellington","(UTC+13:00) Nuku'alofa Samoa")
cm_output_tz.grid(row=7,column=1,sticky=W)
lb_cal_output_daytime=Label(root_cal,text="day-time saving(yes/no): ",fg="black",bg="white").grid(row=8,sticky=W)
cal_output_daytime=StringVar()
cm_output_daytime=ttk.Combobox(root_cal,textvariable=cal_output_daytime,width=5)
cm_output_daytime["values"]=("yes","no")
cm_output_daytime.grid(row=8,column=1,sticky=W)
lb_cal_email=Label(root_cal,text="Email result(yes/no): ",fg="black",bg="white").grid(row=9,sticky=W)
cal_email=StringVar()
cm_email=ttk.Combobox(root_cal,textvariable=cal_email,width=5)
cm_email["values"]=("yes","no")
cm_email.grid(row=9,column=1,sticky=W)
lb_cal_email_txt=Label(root_cal,text="Email(if need): ",fg="black",bg="white").grid(row=10,sticky=W)
cal_input_email=StringVar()
et_cal_input_email=Entry(root_cal,textvariable=cal_input_email,width=30).grid(row=10,column=1,sticky=W)
bt_cal_submit=Button(root_cal,text="submit",command=submit_func).grid(row=11,sticky=W)
lb_cal_sp1=Label(root_cal,text=" ",fg="black",bg="white").grid(row=12,column=0)
lb_cal_rs=Label(root_cal,text="Result",fg="black",bg="white",font=("Arial",14)).grid(row=13,sticky=W)
lb_cal_rs_time=Label(root_cal,text="time in 24hr (XX:XX): ",fg="black",bg="white").grid(row=14,sticky=W)
cal_rs_time=StringVar()
et_cal_rs_time=Entry(root_cal,textvariable=cal_rs_time,width=10).grid(row=14,column=1,sticky=W)
lb_cal_rs_date=Label(root_cal,text="date (YYYY/MM/DD): ",fg="black",bg="white").grid(row=15,sticky=W)
cal_rs_date=StringVar()
et_cal_rs_date=Entry(root_cal,textvariable=cal_rs_date,width=15).grid(row=15,column=1,sticky=W)
lb_cal_sp2=Label(root_cal,text=" ",fg="black",bg="white").grid(row=16,column=0)




#main wd
# menu
# menu_wd.add_command(label="History")
menu_wd.add_command(label="last update info",command=lastup)
menu_wd.add_command(label="help",command=helpWindow)
menu_wd.add_command(label="exit",command=exit_wd)
#pseudo menu for mac
# bt_wd_history=Button(root_wd,text="History").grid(row=19,column=0)
bt_wd_lastup=Button(root_wd,text="last update info",command=lastup).grid(row=20,column=0)
bt_wd_help=Button(root_wd,text="help",command=helpWindow).grid(row=21,column=0)
bt_wd_exit=Button(root_wd,text="exit",command=exit_wd).grid(row=22,column=0)

# content
lb_wd_main=Label(root_wd ,text="World Clock",fg="black",bg="white",font=("Arial",18)).grid(row=0,column=0)
# lb_wd_city_title=Label(root_wd,text="Search by location (please type in city/continent format such as Bangkok/Asia or use the current ip location",fg="black",bg="white").grid(row=1,column=0)
# city_input=StringVar()
# lb_wd_city_entry=Entry(root_wd,textvariable=city_input,width=50).grid(row=2,column=0)
# bt_wd_searchcity=Button(root_wd,text="search").grid(row=3,column=0)
# lb_wd_sp1=Label(root_wd,text=" ",fg="black",bg="white").grid(row=4,column=0)
# lb_wd_tz_title=Label(root_wd,text="Search by Standard time zone (format UTC+XX or UTC-XX)",fg="black",bg="white").grid(row=5,column=0)
# tz_input=StringVar()
# cm_tz=ttk.Combobox(root_wd,textvariable=tz_input)
# cm_tz["values"]=("UTC-12:00","UTC-11:00","UTC-10:00","UTC-09:00","UTC-08:00","UTC-07:00","UTC-06:00","UTC-05:00","UTC-04:30","UTC-04:00","UTC-03:30","UTC-03:00","UTC-02:00","UTC-01:00","UTC+00:00","UTC+01:00","UTC+02:00","UTC+03:00","UTC+03:30","UTC+04:00","UTC+04:30","UTC+05:00","UTC+05:30","UTC+05:45","UTC+06:00","UTC+06:30","UTC+07:00","UTC+08:00","UTC+09:00","UTC+09:30","UTC+10:00","UTC+11:00","UTC+12:00","UTC+13:00")
# cm_tz.grid(row=6,column=0)

lb_wd_adsearch_title=Label(root_wd,text="Please choose city/timezone then click search or click current location time",fg="black",bg="white").grid(row=5,column=0)
adv_input=StringVar()
cm_adv=ttk.Combobox(root_wd,textvariable=adv_input,width=45)
cm_adv["values"]=("(UTC-12:00) International Date Line West","(UTC-11:00) Coordinated Universal Time-11","(UTC-10:00) Hawaii","(UTC-09:00) Alaska","(UTC-08:00) Baja California","(UTC-08:00) Pacific Time (US and Canada)","(UTC-07:00) Chihuahua, La Paz, Mazatlan","(UTC-07:00) Arizona","(UTC-07:00) Mountain Time (US and Canada)","(UTC-06:00) Central America","(UTC-06:00) Central Time (US and Canada)","(UTC-06:00) Saskatchewan","(UTC-06:00) Guadalajara, Mexico City, Monterey","(UTC-05:00) Bogota, Lima, Quito","(UTC-05:00) Indiana (East)","(UTC-05:00) Eastern Time (US and Canada)","(UTC-04:30) Caracas","(UTC-04:00) Atlantic Time (Canada)","(UTC-04:00) Asuncion","(UTC-04:00) Georgetown, La Paz, Manaus, San Juan","(UTC-04:00) Cuiaba","(UTC-04:00) Santiago","(UTC-03:30) Newfoundland","(UTC-03:00) Brasilia","(UTC-03:00) Greenland","(UTC-03:00) Cayenne, Fortaleza","(UTC-03:00) Buenos Aires","(UTC-03:00) Montevideo","(UTC-02:00) Coordinated Universal Time-2","(UTC-01:00) Cape Verde","(UTC-01:00) Azores","(UTC+00:00) Casablanca","(UTC+00:00) Monrovia, Reykjavik","(UTC+00:00) Dublin, Edinburgh, Lisbon, London","(UTC+00:00) Coordinated Universal Time","(UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna","(UTC+01:00) Brussels, Copenhagen, Madrid, Paris","(UTC+01:00) West Central Africa","(UTC+01:00) Belgrade, Bratislava, Budapest, Ljubljana, Prague","(UTC+01:00) Sarajevo, Skopje, Warsaw, Zagreb","(UTC+01:00) Windhoek","(UTC+02:00) Athens, Bucharest, Istanbul","(UTC+02:00) Helsinki, Kiev, Riga, Sofia, Tallinn, Vilnius","(UTC+02:00) Cairo","(UTC+02:00) Damascus","(UTC+02:00) Amman","(UTC+02:00) Harare, Pretoria","(UTC+02:00) Jerusalem","(UTC+02:00) Beirut","(UTC+03:00) Baghdad","(UTC+03:00) Minsk","(UTC+03:00) Kuwait, Riyadh","(UTC+03:00) Nairobi","(UTC+03:30) Tehran","(UTC+04:00) Moscow, St. Petersburg, Volgograd","(UTC+04:00) Tbilisi","(UTC+04:00) Yerevan","(UTC+04:00) Abu Dhabi, Muscat","(UTC+04:00) Baku","(UTC+04:00) Port Louis","(UTC+04:30) Kabul","(UTC+05:00) Tashkent","(UTC+05:00) Islamabad, Karachi","(UTC+05:30) Sri Jayewardenepura Kotte","(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi","(UTC+05:45) Kathmandu","(UTC+06:00) Astana","(UTC+06:00) Dhaka","(UTC+06:00) Yekaterinburg","(UTC+06:30) Yangon","(UTC+07:00) Bangkok, Hanoi, Jakarta","(UTC+07:00) Novosibirsk","(UTC+08:00) Krasnoyarsk","(UTC+08:00) Ulaanbaatar","(UTC+08:00) Beijing, Chongqing, Hong Kong, Urumqi","(UTC+08:00) Perth","(UTC+08:00) Kuala Lumpur, Singapore","(UTC+08:00) Taipei","(UTC+09:00) Irkutsk","(UTC+09:00) Seoul Osaka Sapporo Tokyo","(UTC+09:30) Darwin","(UTC+09:30) Adelaide","(UTC+10:00) Hobart Yakutsk Brisbane Guam","(UTC+10:00) Canberra, Melbourne, Sydney","(UTC+11:00) Vladivostok","(UTC+11:00) Solomon Islands, New Caledonia","(UTC+12:00) Coordinated Universal Time+12","(UTC+12:00) Fiji, Marshall Islands Magadan Auckland Wellington","(UTC+13:00) Nuku'alofa Samoa")
cm_adv.grid(row=6,column=0)
bt_wd_adsearch=Button(root_wd,text="search",command=wd_search_command).grid(row=7,column=0)
lb_wd_sp2=Label(root_wd,text=" ",fg="black",bg="white").grid(row=8,column=0)
bt_wd_curloc=Button(root_wd,text="current location time",command=current_loc_time).grid(row=9)
lb_wd_sp3=Label(root_wd,text=" ",fg="black",bg="white").grid(row=10,column=0)
lb_wd_rshead=Label(root_wd,text="Result",fg="black",bg="white",font=("Arial",14)).grid(row=11)
lb_wd_rstime=Label(root_wd,text="time",fg="black",bg="white").grid(row=12)
wd_rstime=StringVar()
et_wd_rstime=Entry(root_wd,textvariable=wd_rstime,width=10)
et_wd_rstime.grid(row=13)
lb_wd_rsdate=Label(root_wd,text="date",fg="black",bg="white").grid(row=14)
wd_rsdate=StringVar()
et_wd_rsdate=Entry(root_wd,textvariable=wd_rsdate,width=10)
et_wd_rsdate.grid(row=15)
lb_wd_rstz=Label(root_wd,text="timezone",fg="black",bg="white").grid(row=16)
wd_rstz=StringVar()
et_wd_rstz=Entry(root_wd,textvariable=wd_rstz,width=10)
et_wd_rstz.grid(row=17)
lb_wd_sp4=Label(root_wd,text=" ",fg="black",bg="white").grid(row=18,column=0)

#end line
root_cal.mainloop()
root_wd.mainloop()