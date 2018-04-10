import re

f = open('datamining.log', 'r')
w = open('result', 'w')
patern = re.compile('2014:(\d\d).{0,}HTTP/1.1" (\d\d\d)')
myStr = str(f.read())
res = patern.findall(myStr)

a = set()
for i in range(len(res)):
    a.add(res[i][0])
b = a.copy()

for j in range(len(b)):
    countAll = 0
    countSucc = 0
    hou = a.pop()
    for i in range(len(res)):
        if(int(res[i][0]) == int(hou)):
            countAll += 1
        if(res[i][0] == hou) and (int(res[i][1]) == 200):
            countSucc += 1
    w.write('Hour: ' + str(hou) + ". All request: " + str(countAll) + ". Success request: " + str(countSucc) + ". Result = " + str(countSucc/countAll*100) + '%\n')
f.close()
w.close()