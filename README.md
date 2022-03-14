# setup4cs361_idv_project

### requirement :rocket:
------------------
python3
python plugin: geocode tzwhere pytz Pillow

### file detail :rocket:
------------------
GrabData.py --> grab internet data micro service

command_dtz.txt --> text microservice pipeline

dtz_res.csv --> text microservice pipeline

email_service.py --> email micro service

example_req.py --> sample file for using pipeline

grabdate-service.txt --> text microservice pipeline

grabdata-result.txt --> text microservice pipeline

help_cal.png --> image source

help_wd.png --> image source

main.py --> main software

mservice.py -> time micro service

mservice_sub.py --> sub version of mservice.py in case the first one cannot use

email_service_sub.py --> sub version of email_service.py in case the first one cannot use


### how to use open software :rocket:
-------------------
note** : For using email feature, it is require to use VPN from Oregon State University

step0 : install the requirement on the first section of readme file

step1 : open 4 shell such as powershell or terminal

step2: in each tab run the following command
Tab1>> python3 mservice.py
Tab2>> python3 GrabData.py
Tab3>> email_service.py
Tab4>> main.py
