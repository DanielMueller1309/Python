import time

# add new timemark for start time in  + "X" Minutes and Secounds
# add with "+" after "int(time.strftime("%M"))" the houres the start date is in future
hours = int(time.strftime("%H")) + 0
# add with "+" after "int(time.strftime("%M"))" the minutes the start date is in future
minute = int(time.strftime("%M")) + 0
# add with "+" after "int(time.strftime("%M"))" the secounds the start date is in future
secounds = int(time.strftime("%S")) + 0
start_date = time.strftime("%G-%m-%dT") + str(hours) + ':' + str(minute) + ':' + str(secounds)
#time.strftime("%m-%d-%y_%H-%M-%S")
#2021-04-28T07:52:50.2538139
print(start_date)
print(time.asctime())