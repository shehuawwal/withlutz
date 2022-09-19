import re, json, csv
from time import time
from dateutil.parser import parse
from datetime import datetime



logData = re.compile(r'generated (\d+) bytes in (\d+) msecs')
# pattern_date = re.compile(r'\d{4}[-]\d{2}[-]\d{2}')

lst = []

# with open("connections.log") as f:
with open("little.log") as f:
    start_at = None
    end_at = None
    size = 0

    for line in f:
        entry = json.loads(line)
        logs = logData.search(line)
        timestamp = parse(entry['time'])
        
        if not start_at:
            start_at = timestamp
            end_at = start_at # + 5min

        if timestamp < end_at:
            if logs:
                bytes = logs.group(1)
                size += bytes
        else:
            print(f'size agg from {start_at} to {end_at} = {size}')
            size = 0
            start_at = timestamp
            end_at = start_at
            # end_at = start_at # + 5min
            continue