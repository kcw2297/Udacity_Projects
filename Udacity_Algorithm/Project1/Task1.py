"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

def checkNum(nums):
    check_num = set()
    for repeat in nums:
        call_num = repeat[0]
        take_num = repeat[1]
        if call_num not in check_num:
            check_num.add(call_num)
        if take_num not in check_num:
            check_num.add(take_num)
    return check_num


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    text_set = checkNum(texts)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    call_set = checkNum(calls)
    tot_set = set.union(text_set,call_set)
    count = len(tot_set)
    print(f'There are {count} different telephone numbers in the records.')

"""
Testing
with open('test.csv','r') as f:
    reader = csv.reader(f)
    call = list(reader)
    checkNum(call)
"""
