import sys
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

list1 = []
list2 = []

for line in lines:
    locations = line.split(' ')
    print(locations)
    list1.append(locations[0])
    list2.append(locations[3])

d = {}

result = 0
for i in range(len(list2)):
    if None == d.get(list2[i]):
        d[list2[i]] = 1
    else:
        d[list2[i]] = d[list2[i]] + 1

for num in list1:
    if None != d.get(num):
        result += int(num) * d[num]

print(result)