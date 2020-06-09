import json

with open("meetings.json", "r+") as f:
    content = json.load(f)
    if content == {}:
        print("No meetings")

    else:
        for k, v in zip(list(content.keys()), list(content.values())):
            print(f"- meeting {k} at {v}")
