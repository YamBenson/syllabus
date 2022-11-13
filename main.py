import dateparser

# The start!
f = open("PH141Syllabus_Fall2022.txt", "r")

events = []

temp = {
    "month": None,
    "day": None,
    "year": None,
    "details": ""
}

lines = f.readlines()

for line in lines:
    event = temp.copy()
    parts = line.split(" ")
    month = False
    day = False

    for part in parts:
        if day:
            event["details"] = event["details"] + " " + part
        if month:
            if part[0:2].isnumeric():
                if part[0] == "0":
                    event["day"] = int(part[1])
                else:
                    event["day"] = int(part[0:2])
            elif part[0].isnumeric():
                event["day"] = int(part[0])
            month = False
            day = True
        if len(part) >= 3 and not month and not day:
            if part[0:3].isalpha():
                if part[0:3].lower() == "jan":
                    event["month"] = 1
                elif part[0:3].lower() == "feb":
                    event["month"] = 2
                elif part[0:3].lower() == "mar":
                    event["month"] = 3
                elif part[0:3].lower() == "apr":
                    event["month"] = 4
                elif part[0:3].lower() == "may":
                    event["month"] = 5
                elif part[0:3].lower() == "jun":
                    event["month"] = 6
                elif part[0:3].lower() == "jul":
                    event["month"] = 7
                elif part[0:3].lower() == "aug":
                    event["month"] = 8
                elif part[0:3].lower() == "sep":
                    event["month"] = 9
                elif part[0:3].lower() == "oct":
                    event["month"] = 10
                elif part[0:3].lower() == "nov":
                    event["month"] = 11
                elif part[0:3].lower() == "dec":
                    event["month"] = 12
                
                if event["month"] is not None:
                    month = True

    if event["month"] != None:
        event["details"] = event["details"][0:len(event["details"])-1]
        events.append(event)

print(events)