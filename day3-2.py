import sys
import re
D = open(sys.argv[1]).read().strip()

x = re.findall(r"don't\(\)|do\(\)|mul[(]\d{1,3}[,]\d{1,3}[)]", D)



result = 0
add_it = True
for item in x:
    if item == "don't()":
        add_it = False
    elif item == "do()":
        add_it = True
    elif add_it == True:
        numbers = item[4:]
        numbers = numbers[:-1]
        new_nums = numbers.split(',')
        result += (int(new_nums[0]) * int(new_nums[1]))


print(result)