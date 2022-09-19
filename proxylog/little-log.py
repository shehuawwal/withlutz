import re, json, csv
from time import time
from dateutil.parser import parse
# from datetime import datetime
import datetime

logData = re.compile(r'generated (\d+) bytes in (\d+) msecs')
# pattern_date = re.compile(r'\d{4}[-]\d{2}[-]\d{2}')

lst = []

# with open("connections.log") as f:
with open("little.log") as f:
    for line in f:
        entry = json.loads(line)
        logs = logData.search(line)
        timestamp = parse(entry['time'])
        if logs:
            bytes = logs.group(1)
            sec = logs.group(2)
            # print(timestamp)

            #2022-09-01 13:03:21.661515+00:00

            # time_1 = datetime.strptime(timestamp,"%H:%M:%S")
            # time_2 = datetime.strptime(timestamp,"%H:%M:%S")

            # time_interval = time_2 - time_1
            # print(time_interval)


            timestamp_seconds = timestamp.second
            timestamp_minutes = timestamp.minute
            timestamp_hours = timestamp.hour

            time_1 = datetime.timedelta(hours= timestamp_hours , minutes=timestamp_minutes, seconds=timestamp_seconds)
            time_2 = datetime.timedelta(hours= timestamp_hours, minutes=5, seconds=0)
            print(time_2  - time_1)
            # time_1 = datetime.timedelta(minutese






            # print(timestamp_seconds, timestamp_minutes)



            # datax = f'{timestamp.second}:{timestamp.microsecond}'
            # print(datax)
