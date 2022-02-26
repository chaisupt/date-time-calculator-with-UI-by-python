
"""Sample program in Python for sending a request to the email microservice to send an email.  Email account used for sending the email is cs361avengers@gmail.com"""
"""Note that you may need to install the requests module for python first."""
"""Sample usage to install requests: From the command line: C:\\Users\your_User_Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install requests"""
"""Note that the exact path may be something different, depending on which version of python you are using and where you installed python to begin with."""
"""For example, on my computer the path is C:\Python39\Scripts"""
import requests
import string
import os
import time
import sys
import select

def sendtheemail(email_address,the_mess):
    """The first url is a way to test that the server is up and running. Make sure you are logged in to the OSU VPN.  Comment out the next 6 lines when using for production."""
    url = 'http://flip3.engr.oregonstate.edu:5101/'
    send_message = requests.get(url) 
    """The print statement below prints a message from the email microservice.  This shows that the server is running."""
    print(send_message.text)
    """This print statement prints the status number of the request."""
    print(send_message)

    """Used for sending an email using the email microservice.  Sample email content provided below."""
    """Change to the email address you want to send the email to."""
    # email_address = "chaisupt@oregonstate.edu" 
    message_to_send = "Hello from the group project email microsservice.  Here is your clock calculation result\n"+the_mess
    this_subject = "timezone calculation result!"

    """Use this format to send data required for the email microservice"""
    send_object = {'to': email_address, 'message': message_to_send, 'subject': this_subject}
    url2 = 'http://flip3.engr.oregonstate.edu:5101/sendemail'

    """This statement will send the data in send_object back to you, and send the email using the email microservice"""
    next_message = requests.post(url2, data=send_object)
    """This statement will print the data in send_object;  The server is set up to send the object it receives in the request body back to you.  
    If you only want the request status sent back, change the statement to print(next_message)"""
    print(next_message.text)

    """If you want to access or use the status code directly to check if the request was successful, you can use the line below"""
    if next_message.status_code == 200:
        print("Request successful")
        return "Request succesful"
    else:
        return "Request error!!!"

def doit(email_addr,content):
    #setup output
    func_recv=sendtheemail(email_addr,content)
    firstline="status"
    secondline=func_recv
    # print(secondline)
    rs_file=open("dtz_res.csv","w")
    rs_file.write(firstline)
    rs_file.write("\n")
    rs_file.write(secondline)
    rs_file.flush()
    rs_file.close()

def check_commandfile():
    command_file=open("command_dtz.txt","r")
    commander=command_file.readline()
    commander=commander.replace("\n","")
    command_file.close()
    if(commander=="req_mail"):
        command_file=open("command_dtz.txt","r")
        reader=command_file.readline()
        reader=command_file.readline()
        email_addr=reader.replace("\n","")
        reader=command_file.readline()
        content=reader.replace("\n","")
        command_file.close()
        command_file=open("command_dtz.txt","w")
        command_file.write(" ")
        command_file.flush()
        command_file.close()
        doit(email_addr,content)


print("Email service is running @ please press control+c to quit system")
while True:
    try:
        check_commandfile()
    except KeyboardInterrupt:
        print(" \nthe service was closed thank you for using email service")
        break