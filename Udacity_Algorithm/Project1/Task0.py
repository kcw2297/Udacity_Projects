"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

def first_text(texts):
    print('First record of texts, {0} texts {1} at time {2}'.format(*texts[0]))

def last_call(calls):
    print('Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds'.format(*calls[-1]))

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    first_text(texts)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    last_call(calls)

"""
Testing
with open('test.csv','r') as f:
    reader = csv.reader(f)
    call = list(reader)
    first_text(call)
    last_call(call)
"""
