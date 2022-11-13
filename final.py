# import dateparser
import requests
import datetime
from cal_setup import get_calendar_service

import PyPDF2
import sys
    
# creating a pdf file object 
pdfFileObj = open('PH141Syllabus_Fall2022.pdf', 'rb')

if len(sys.argv) == 2:
    pdfFileObj = open(sys.argv[1], 'rb')
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# printing number of pages in pdf file 
# print(pdfReader.numPages) 
if len(sys.argv) == 2:
    file1=open(sys.argv[1][0:len(sys.argv[1])-3] + "txt","w")
else:
    file1=open(r"PH141Syllabus_Fall2022.txt","w")
    
for i in range(pdfReader.numPages):
    # creating a page object 
    pageObj = pdfReader.getPage(i) 
        
    # extracting text from page 
    # print(pageObj.extractText()) 
    file1.writelines(pageObj.extractText())
    
# closing the pdf file object 
pdfFileObj.close()
file1.close()

# The start!
f = open(sys.argv[1][0:len(sys.argv[1])-3] + "txt", "r")

events = []

temp = {
    "month": None,
    "day": None,
    "year": datetime.date.today().year,
    "details": ""
}

lines = f.readlines()

# print(lines)

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

service = get_calendar_service()

# print(events)

for event in events:
    start = str(event["year"]) + "-" + str(event["month"]) + "-" + str(event["day"]) + "T11:00:00-05:00"
    end = str(event["year"]) + "-" + str(event["month"]) + "-" + str(event["day"]) + "T12:00:00-05:00"
    desc = event["details"]

    event_result = service.events().insert(calendarId='primary',
        body={
            "summary": 'PH141',
            "description": desc,
            "start": {"dateTime": start, "timeZone": 'America/New_York'},
            "end": {"dateTime": end, "timeZone": 'America/New_York'},
        }
    ).execute()