import re, json, csv
from time import time
from weakref import ref
from dateutil.parser import parse
from datetime import datetime
import datetime

logData = re.compile(r'generated (\d+) bytes in (\d+) msecs')
# pattern_date = re.compile(r'\d{4}[-]\d{2}[-]\d{2}')

rftimelist = []
rft = []
eft = []

# with open("connections.log") as f:
with open("little.log") as f:
    for line in f:
        entry = json.loads(line)
        logs = logData.search(line)
        timestamp = parse(entry['time'])
        if logs:
            bytes = logs.group(1)
            sec = logs.group(2)

            timestamp_seconds = timestamp.second
            timestamp_minutes = timestamp.minute
            timestamp_hours = timestamp.hour

            logtime = datetime.timedelta(hours= timestamp_hours , minutes=timestamp_minutes, seconds=timestamp_seconds)
            rftimelist.append(logtime)
        
            rft.append(rftimelist[0])
            reftime = rftimelist[0]
            endtime = rftimelist[-1]
            delta = datetime.timedelta(minutes=10)


            # t1 = datetime.datetime.strptime(reftime, "%H:%M:%S")

           
            # print(type(reftime))
            while reftime < endtime:
                print(reftime.isoformat())
                reftime = reftime + delta

