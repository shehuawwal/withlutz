import re
import json

pattern_time = re.compile(r'\d{2}[:]\d{2}[:]\d{2}')
pattern_date = re.compile(r'\d{4}[-]\d{2}[-]\d{2}')


with open("little.log") as f:
    for line in f:
        pattern_times = pattern_time.findall(line)
        pattern_days = pattern_date.findall(line)
        print(pattern_days[0], pattern_times[1])
