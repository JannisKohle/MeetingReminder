import os
import json
import datetime
from time import sleep

def delete(name):
    with open("meetings.json", "r+") as f:
        content = json.load(f)

    del content[name]

    with open("meetings.json", "r+") as f:
        f.truncate(0)
        json.dump(content, f)

def alarm():
    os.system("say meeting meeting meeting meeting meeting meeting meeting meeting meeting meeting")

meeting_name = input("What's the name of the meeting? ")

with open("meetings.json", "r+") as f:
    content = json.load(f)
    meeting_time = content[meeting_name].split(" ")[0] # "22:15"
    meeting_date = content[meeting_name].split(" ")[1] # "2020.10.17"

# TODO: change meeting_time to few minutes earlier

def getDate():
    return str(datetime.datetime.now()).split(" ")[0] # "2020-10-17"

def getTime():
    return str(datetime.datetime.now()).split(" ")[1][:5] # "21:30"

# Find out if same day:
if meeting_date.replace(".", "-") != getDate():
    print("Today is not the day of the meeting.")

else:
    while True:
        sleep(30)

        if getTime() == meeting_time:
            break

    alarm()
    delete(meeting_name)
