import string
import os
import time
commanding_word="req"
fs=open("command_dtz.txt","w")
fs.write(commanding_word)
fs.close()
time.sleep(4)
fs=open("dtz_res.csv","r")
reading=fs.readline()
print(reading)
reading=fs.readline()
print(reading)
fs.close()