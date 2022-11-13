# import dateparser
import requests
import datetime
import dateConvert

# The start!
f = open("PH141Syllabus_Fall2022.txt", "r")

events = []

temp = {
    "month": None,
    "day": None,
    "year": datetime.date.today().year,
    "details": ""
}

temp2 = {
  'summary': 'Lecture',
  'location': '',
  'description': '',
  'start': {
    'dateTime': '2015-05-28T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2015-05-28T17:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
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
url = 'https://www.googleapis.com/calendar/v3/calendars/c_f526f9e05146fa83817f80d3e2a28dc10451d71d3e7641f455bea2deaa6cce53@group.calendar.google.com/events'

for event in events:
    requests.post(url, json = event)