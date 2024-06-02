"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def findOutGoing(data):
    call = set()
    take = set()
    for row in data:
        call.add(row[0])
        take.add(row[1])
    return call, take


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    outgoing, non_tele0 = findOutGoing(calls)


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    non_tele1, non_tele2= findOutGoing(texts)
    tele_num = outgoing - non_tele0 - non_tele1 - non_tele2
    sorted_list = sorted(tele_num)
    print("These numbers could be telemarketers: ")
    for num in sorted_list:
        print(num)
