import json
import time

name = input("What's the name of the meeting? ")

with open("meetings.json", "r+") as f:
    content = json.load(f)

if name not in content:
    print("This meeting doesn't exist.")

else:
    with open("meetings.json", "r+") as f:
        del content[name]
        f.truncate(0)
        json.dump(content, f)
