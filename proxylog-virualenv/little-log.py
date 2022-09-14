import re, json
from dateutil.parser import parse
from matplotlib import pyplot as plt
import numpy as np



bytex = re.compile(r'generated (\d+) bytes in (\d+) msecs')

# pattern_date = re.compile(r'\d{4}[-]\d{2}[-]\d{2}')


bytes = []
msec = []
with open("little.log") as f:
    for line in f:
        entry = json.loads(line)
        bytesx = bytex.search(line)
        if bytesx:
            # byt = bytesx.group(1)
            # msec = bytesx.group(2)
            bytes.append(bytesx.group(1))
            msec.append(bytesx.group(2))
            # print(byt)
            # print(byt, msec)



plt.bar(bytes,msec)
plt.title('EMID Proxy Log')
plt.xlabel('Bytes')
plt.ylabel('Secs')
plt.show()




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