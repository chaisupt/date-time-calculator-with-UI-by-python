# from tkinter import *

# root = Tk()
# root.title("Test")
# root.geometry("500x500")

# def the_set():
#     testEx.delete(0,"end")
#     testEx.insert(0, "hello world")
#     et_wd_rstime.delete(0,"end")
#     et_wd_rstime.insert(0,"test complete")

# wd_rstime=StringVar()
# et_wd_rstime=Entry(root,textvariable=wd_rstime,width=10)
# et_wd_rstime.pack()
# testEx=Entry(root)
# testEx.pack()
# btEx=Button(root,text="set",command=the_set)
# btEx.pack()


# root.mainloop()

# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x50")

# def setTextInput(text):
#     textExample.delete(0,"end")
#     textExample.insert(0, text)

# textExample = tk.Entry(root)
# textExample.pack()

# btnSet = tk.Button(root, height=1, width=10, text="Set", 
#                     command=lambda:setTextInput("new content"))
# btnSet.pack()

# root.mainloop()

# x=input("x: ")
# y=input("y: ")
# z=int(x)-int(y)
# print(z)

# r=input("xx: ")
# print(r[:2])
# print(r[3:])

# from datetime import datetime
# import pytz
# from tzwhere import tzwhere

# t_tz= tzwhere.tzwhere()
# #find the timezone from current latitude / longitude
# timezone_str = t_tz.tzNameAt(27.714643, 85.308833) # Seville coordinates
# #set the timezone into appropriate format
# timezone = pytz.timezone(timezone_str)
# #show the timezone
# # print(datetime.now(timezone))
# print(str(datetime.now(timezone).tzname()))
# numbe=int(datetime.now(timezone).tzname())
# print(numbe%100)

# from mservice import *
from datetime import datetime
from datetime import timedelta

def plus_date(d1):
    return "the day after "+str(d1)
def minus_date(d1):
    return "the day before "+str(d1)

def wd_clock_reset(h1,m1,z1,d1):
    d1_ori=d1
    d1_edited=0 # 0=not edited 1=edited+1 2=edited-1
    z1=int(z1)
    negat=False
    if(z1<0):
        negat=True
        z1=z1*(-1)
    if(z1%100==30 or z1%100==45):
        d_m=z1%100
        if(negat is True):
            d_m=d_m*(-1)
        m1=m1-d_m
        if(m1<0):
            h1=h1-1
            m1=60+m1
            if(h1<0):
                ####
                h1=h1+24
                d1=minus_date(d1)
                d1_edited=2

        if(m1>0):
            h1=h1+1
            m1=m1-60
        if(m1==0 and (negat is True)):
            h1=h1+1
        if(h1>23):
            ###
            h1=h1-24
            d1=plus_date(d1)
            d1_edited=1
        

    


    return h1,m1,d1

def wd_clock_cal(z2):
    #form of t1 hh:mm
    #form of z1 +hh:mm (current base)
    #form of z2 +hh:mm (selection)
    h1=t1[:2]
    m1=t1[3:]
    # print(h_t1)
    # print(m_t1)
    curr_time_pack=curr_time_service()
    h1,m1,d1 = wd_clock_reset(h1,m1,curr_time_pack["timezone"],curr_time_pack["date"])


def wd_reset_clock(h1,m1,s1,d1,z1):
    #hr min sec
    h1=int(h1)
    m1=int(m1)
    s1=int(s1)
    #year
    ye1=d1[:4]
    ye1=int(y1)
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
        







    
    
    