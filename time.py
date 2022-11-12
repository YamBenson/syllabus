import datetime
import time

def isTimeFormat(input): 
    if input.count(" ")>=2:
        if input.count("M")==2:
            start = ' '.join(input.split()[0:2])  
            end = ' '.join(input.split()[3:])
            try:
                if input.count(":")==1:
                    time.strptime(start, '%H:%M %p')
                    return start
                else :
                    time.strptime(start, '%H:%M %p')
                    time.strptime(end, '%H:%M %p')
                    s=start.split(":")
                    hour=s[0]+':00'
                    minute=s[1]
                    ta=minute.split(" ")
                    e=end.split(":")
                    eHour=e[0]+':00'
                    eMinute=e[1]
                    t=eMinute.split(" ")
                    print('start: hour =', hour,'minute =', ta[0],ta[1])
                    print('end: hour =', eHour,'minute =', t[0],t[1])
                    return start + ' - ' + end
            except ValueError:
                return False
        else:
            start = ' '.join(input.split()[0:1])  
            end = ' '.join(input.split()[2:])
            try:
                if input.count(":")==1:
                    start = ' '.join(input.split()[0:2])  
                    end = ' '.join(input.split()[3:])
                    time.strptime(start, '%H:%M %p')
                    s=start.split(":")
                    hour=s[0]+':00'
                    minute=s[1]
                    ta=minute.split(" ")
                    e=end.split(":")
                    eHour=e[0]+':00'
                    eMinute=e[1]
                    t=eMinute.split(" ")
                    print('start: hour =', hour,'minute =', ta[0],ta[1])
                    print('end: hour =', eHour,'minute =', t[0],t[1])
                    return start
                else :
                    time.strptime(start, '%H:%M')
                    time.strptime(end, '%H:%M %p')
                    s=start.split(":")
                    hour=s[0]+':00'
                    minute=s[1]
                    ta=minute.split(" ")
                    e=end.split(":")
                    eHour=e[0]+':00'
                    eMinute=e[1]
                    t=eMinute.split(" ")
                    print('start: hour =', hour,'minute =', ta[0])
                    print('end: hour =', eHour,'minute =', t[0],t[1])
                    return start + ' - ' + end
            except ValueError:
                return False
    else:
        if input.count("M")==2:
            start = ' '.join(input.split()[0:2])  
            end = ' '.join(input.split()[3:])
            try:
                if input.count(":")==1:
                    time.strptime(start, '%H:%M %p')
                    return start
                else :
                    time.strptime(start, '%H:%M %p')
                    time.strptime(end, '%H:%M %p')
                    s=start.split(":")
                    hour=s[0]+':00'
                    minute=s[1]
                    ta=minute.split(" ")
                    e=end.split(":")
                    eHour=e[0]+':00'
                    eMinute=e[1]
                    t=eMinute.split(" ")
                    print('start: hour =', hour,'minute =', ta[0],ta[1])
                    print('end: hour =', eHour,'minute =', t[0],t[1])
                    return start + ' - ' + end
            except ValueError:
                return False
        else:
            if input.count(":")!=2:
                start = ' '.join(input.split()[0:1])  
                end = ' '.join(input.split()[2:])
                try:
                    if input.count(":")==1:
                        start = ' '.join(input.split()[0:2])  
                        end = ' '.join(input.split()[3:])
                        s=start.split(":")
                        hour=s[0]+':00'
                        minute=s[1]
                        ta=minute.split(" ")
                        print('start: hour =', hour,'minute =', ta[0],ta[1])
                        time.strptime(start, '%H:%M %p')
                        return start
                    else :
                        time.strptime(start, '%H:%M')
                        time.strptime(end, '%H:%M %p')
                        s=start.split(":")
                        s=start.split(":")
                        hour=s[0]+':00'
                        minute=s[1]
                        ta=minute.split(" ")
                        e=end.split(":")
                        eHour=e[0]+':00'
                        eMinute=e[1]
                        t=eMinute.split(" ")
                        print('start: hour =', hour,'minute =', ta[0],ta[1])
                        print('end: hour =', eHour,'minute =', t[0],t[1])
                        return start + ' - ' + end
                except ValueError:
                    return False
            else:
                newinput = input.split('-')  
                start = newinput[0]
                end = newinput[1]
                try:
                    if input.count(":")==1:
                        start = ' '.join(input.split()[0:2])  
                        end = ' '.join(input.split()[3:])
                        s=start.split(":")
                        hour=s[0]+':00'
                        minute=s[1]
                        ta=minute.split(" ")
                        e=end.split(":")
                        eHour=e[0]+':00'
                        eMinute=e[1]
                        t=eMinute.split(" ")
                        print('start: hour =', hour,'minute =', ta[0],ta[1])
                        print('end: hour =', eHour,'minute =', t[0],t[1])
                        time.strptime(start, '%H:%M %p')
                        return start
                    else :
                        time.strptime(start, '%H:%M')
                        time.strptime(end, '%H:%M %p')
                        s=start.split(":")
                        hour=s[0]+':00'
                        minute=s[1]
                        ta=minute.split(" ")
                        e=end.split(":")
                        eHour=e[0]+':00'
                        eMinute=e[1]
                        t=eMinute.split(" ")
                        print('start: hour =', hour,'minute =', ta[0])
                        print('end: hour =', eHour,'minute =', t[0],t[1])
                        return start + ' - ' + end
                except ValueError:
                    return False
    


   
print(isTimeFormat('2:30 AM - 3:30 PM'))
print(isTimeFormat('9:30 AM - 10:20 AM'))
print(isTimeFormat('10:30 AM - 20:20 AM'))
print(isTimeFormat('9:30 AM'))
print(isTimeFormat('9:30 - 10:20 AM'))
print(isTimeFormat('10:30-10:40 AM'))
print(isTimeFormat('10:30-10:40 AM'))

