import json

name = input("What's the meeting name? ")
time = input("What time is the meeting at? (e.g. '16:30 2022.05.21') ")

with open("meetings.json", "r+") as f:
    content = json.load(f)

    if name in content:
        print("This meeting already exists. Please choose another name.")

    else:

        content[name] = time
        json.dump(content, f)
