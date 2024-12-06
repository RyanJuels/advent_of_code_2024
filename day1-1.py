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

list1.sort()
list2.sort()

result = 0
for i in range(len(list1)):
    result += abs(int(list1[i]) - int(list2[i]))

print(result)