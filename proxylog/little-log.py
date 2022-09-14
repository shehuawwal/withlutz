import re, json, csv
from dateutil.parser import parse


bytex = re.compile(r'generated (\d+) bytes in (\d+) msecs')
# pattern_date = re.compile(r'\d{4}[-]\d{2}[-]\d{2}')

bytes = []
lst = []

# with open("connections.log") as f:
with open("little.log") as f:
    for line in f:
        entry = json.loads(line)
        bytesx = bytex.search(line)
        timestamp = parse(entry['time'])
        if bytesx:
            byt = bytesx.group(1)
            msec = bytesx.group(2)
            datax = f'{timestamp.hour}:{timestamp.minute}'
            lst.append(datax)
            bytes.append(byt)

w = open("logx.csv", "w")
rex = csv.writer(w)
rex.writerow(lst)
rex.writerow(bytes)