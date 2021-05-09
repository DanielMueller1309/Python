import time
from datetime import datetime, timedelta


#verzögerung
def plustime_xmlsyntax(): # needed modules: from datetime import datetime, timedelta
    #set time with plustime in the brackets
    start_time = datetime.now() + timedelta(minutes=2, seconds=30)
    times = [start_time.year, start_time.month, start_time.day, start_time.hour, start_time.minute, start_time.second]
    #for loop for leading zero
    for i in range(0, len(times)-1):
        if i == 0:
            if len(str(times[0])) < 4:
                for j in range(len(str(times[0])), 5):
                    times[0] = "0" + str(times[0])
        if i > 0:
            if len(str(times[i])) < 2:
                times[i] = "0" + str(times[i])
    # new generates time in format: yyyy-mm-ddThh:mm:ss
    new_date = time.strftime(str(times[0]) + '-' + str(times[1]) + '-' + str(times[2]) + 'T' + str(times[3]) + ':' + str(times[4]) + ':' + str(times[5]))
    return new_date

print(plustime_xmlsyntax())