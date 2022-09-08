import re
import json

pattern_time = re.compile(r'\d\d[:]\d\d[:]\d\d')
pattern_date = re.compile(r'\d\d\d\d[-]\d\d[-]\d\d')

with open('little.log', 'r') as f:
    logs = f.read()
    
    pattern_times = pattern_time.findall(logs)
    pattern_days = pattern_date.findall(logs)
    ls = zip(pattern_days, pattern_times)

    for patternt in zip(pattern_days, pattern_times):
            days = patternt[0]
            time = patternt[1]
            print(days, time)
