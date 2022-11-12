import time

def isTimeFormat(input): 
    try:
        time.strptime(input, '%I:%M %p')
        return input
    except ValueError:
        return False
   
print(isTimeFormat('2:30 PM'))
print(isTimeFormat('9:30 AM'))
print(isTimeFormat('9:30 MM'))

