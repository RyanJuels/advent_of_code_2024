import sys
import re
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

x = re.findall("mul[(][0-9]+[,][0-9]+[)]", D)
result = 0
for item in x:
    print(item)
    numbers = item[4:]
    numbers = numbers[:-1]
    new_nums = numbers.split(',')
    print(new_nums)
    result += (int(new_nums[0]) * int(new_nums[1]))


print(result)