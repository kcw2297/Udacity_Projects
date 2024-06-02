"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

# Check if it is september
def isSeptember(row):
    period = row[2]
    if period[3:5] == "09":
        return True
    else:
        return False

# Find the longest duration
def findLongest(dict):
    num_dict = dict
    max_dur = max(num_dict.values())
    return max_dur

# Add all the duration
def addDuration(data):
    num_dict = {}
    for row in data:
        if isSeptember(row):
            call = row[0]
            take = row[1]
            duration = row[3]
            num_dict[call] = num_dict.get(call,0) + int(duration)
            num_dict[take] = num_dict.get(take,0) + int(duration)
    # Find the phone number of max duration
    max_dur = findLongest(num_dict)
    for num in num_dict:
        #if int(num_dict[num]) == findLongest(num_dict):
        #    return num
        if num_dict[num] == max_dur:
            max_num = num
    print(f'{max_num} spent the longest time, {max_dur} seconds, on the phone during September 2016.')


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    addDuration(calls)

"""
with open('test.csv','r') as f:
    reader = csv.reader(f)
    call = list(reader)
    addDuration(call)
"""
