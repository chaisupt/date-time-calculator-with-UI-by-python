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







    
    
    