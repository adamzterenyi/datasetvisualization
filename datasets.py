import json
import matplotlib.pyplot as plt

# JSON time
igdpfigs = []
paths = ['project_02/indiagdp.json']
for path in paths:
    with open(path, encoding = 'ascii') as f:
        text = f.read()
        igdpfigs += json.loads(text)
    iactualgdpfigs =  igdpfigs[1]

igdpyears = []
for set in iactualgdpfigs:
    gdpyear = int(set['date'])
    igdpyears.append(gdpyear)
igdpyears.sort()

igdpnumbers = []
for set in iactualgdpfigs:
    gdpnumber = int(set['value'])/1000000000
    igdpnumbers.append(gdpnumber)
igdpnumbers = igdpnumbers[::-1]

# to check for parity and accuracy
'''
print('india years=', igdpyears)
print('india gdp/year=', igdpnumbers)
print(len(str(igdpnumbers[-1])))
'''

# JSON continued, add in the US
ugdpfigs = []
paths = ['project_02/usagdp.json']
for path in paths:
    with open(path, encoding = 'ascii') as f:
        text = f.read()
        ugdpfigs += json.loads(text)
    uactualgdpfigs = ugdpfigs[1]

ugdpyears = []
for set in uactualgdpfigs:
    gdpyear = int(set['date'])
    ugdpyears.append(gdpyear)
ugdpyears.sort()

ugdpnumbers = []
for set in uactualgdpfigs:
    gdpnumber = int(set['value'])/1000000000
    ugdpnumbers.append(gdpnumber)
ugdpnumbers = ugdpnumbers[::-1]

# to check for parity and accuracy
'''
print('usa years=', ugdpyears)
print('usa gdp/year=', ugdpnumbers)
print(len(str(ugdpnumbers[-1])))
'''

# plotting time.
plt.plot(ugdpyears, ugdpnumbers, color = 'blue', label = 'USA')
plt.plot(igdpyears, igdpnumbers, color = 'orange', label = 'India')
'''plt.title('US and Indian GDP figures from 1960 to 2021')'''
plt.xlabel('Years')
plt.ylabel('GDP in USD$, billions')
plt.yticks(range(0, 24000, 2000))
plt.legend(loc='upper left')
plt.show()

# CSV time
import csv

nobellaureates = open('project_02/laureate.csv')
laureatesReader = csv.reader(nobellaureates)
laureates = list(laureatesReader)
print(laureates[940][6])

# European Coal and Steel Community (European Union) founding countries
be = 0
fr = 0
de = 0
it = 0
lu = 0
nl = 0

for laureate in laureates:
    if laureate[6] == 'BE':
        be += 1
    if laureate[6] == 'FR':
        fr += 1
    if laureate[6] == 'DE':
        de += 1
    if laureate[6] == 'IT':
        it += 1
    if laureate[6] == 'LU':
        lu += 1
    if laureate[6] == 'NL':
        nl += 1

# to check
'''
print(be, fr, de, it, lu, nl)
'''

# plotting time!
eufounders = ['Belgium', 'France', 'Germany', 'Luxembourg', 'Italy', 'Netherlands']
nolaureates = [be, fr, de, lu, it, nl]
plt.xlabel('European Union Founding Countries')
plt.ylabel('Nobel Laureates Born in Present Day Boundaries')
plt.bar(eufounders, nolaureates, color = 'orange', width = 0.4)
plt.show()