import re, json, csv
from dateutil.parser import parse


bytex = re.compile(r'generated (\d+) bytes in (\d+) msecs')

# pattern_date = re.compile(r'\d{4}[-]\d{2}[-]\d{2}')


bytes = []
lst = []

with open("little.log") as f:
# with open("connections.log") as f:
    for line in f:
        entry = json.loads(line)
        bytesx = bytex.search(line)
        timestamp = parse(entry['time'])
        if bytesx:
            byt = bytesx.group(1)
            msec = bytesx.group(2)
            # print(byt)
            # datax = f'{timestamp.hour}:{timestamp.minute}, {byt}'
            datax = f'{timestamp.hour}:{timestamp.minute}'
            # print(datax)
            lst.append(datax)
            bytes.append(byt)

x = dict(zip(lst, bytes))
print(x)
                # print(datax)


            # print(f'{timestamp.hour}:{timestamp.minute}')
            # print(timestamp.hour, timestamp.minute,entry['time'])
            # print(entry['time'])
            # print(timestamp)





        # timestamp = parse(entry['time'])
        # print(timestamp.hour)
        # print(entry['time'])

        # """
        # pattern_times = pattern_time.findall(line)
        # pattern_days = pattern_date.findall(line)
        # px = ''.join(pattern_times[0])
        # xs = px.split(':')[-1]
        # print(pattern_days[0], pattern_times[0], xs)
        # # print(pattern_times[0])
        # # print(pattern_days[0], pattern_times[1])
        # """