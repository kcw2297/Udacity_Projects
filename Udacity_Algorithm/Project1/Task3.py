"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""
Part A: Sort the take number code called by (080)(one num per line, no duplicate)
"""
# Check if it is 080
def check(num):
    prefix = num[0:5]
    if prefix == "(080)":
        return True
    else:
        return False

# Check the prefix
def checkPrefix(num):
    if num[0:5] == "(022)":
        return True
    if num[0] in ("7","8","9"):
        return True
    if num[0:2] == "140":
        return True
    if num[0:2] == "(0":
        return True


# Check the prefix
def addPrefix(num):
    if num[0:5] == "(022)":
        return "(022)"
    if num[0] in ("7","8","9"):
        return num[0:4]
    if num[0:2] == "140":
        return "140"
    if num[0:2] == "(0":
        slice = num.find(')')+1
        return num[0:slice]


def findNum(data):
    prefix_set = set()
    for row in data:
        call_num = row[0]
        take_num = row[1]
        if check(call_num) and checkPrefix(take_num):
            prefix_set.add(addPrefix(take_num))
    sorted_list = sorted(prefix_set)
    print("The numbers called by people in Bangalore have codes:")
    for x in sorted_list:
        print(x)

"""
Part B: Find percentage (080)->(080) / all from (080)  (2decimal digits)
"""
def findPercentage(data):
    all_count = 0
    only_count = 0
    for row in data:
        call_num = row[0]
        take_num = row[1]
        if check(call_num) and check(take_num):
            only_count += 1
        if check(call_num):
            all_count += 1
    if all_count == 0 or only_count == 0:
        no_call = "0"
        print(f'{no_call}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')
    else:
        percentage = only_count/all_count*100
        round_per = round(percentage,2)
        print(f'{round_per}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    findNum(calls)
    findPercentage(calls)


"""
with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    test = list(reader)
    findPercentage(test)
"""
