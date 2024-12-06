import sys
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

result = 0
result_list = []
num_dic = {}

for line in lines:
    if "|" in line:
        nums = line.split("|")
    
        if nums[0] in num_dic:
            num_dic[nums[0]].append(nums[1])
        else:
            new_list = []
            new_list.append(nums[1])
            num_dic[nums[0]] = new_list
    else:
        line_list = line.split(",")
        add_line = True
        for i in range(len(line_list)):
            if (i != 0) and (line_list[i] in num_dic):
                for j in range(i, -1, -1):
                    if (line_list[j] in num_dic[line_list[i]]):
                        add_line = False
        
        if (len(line_list) > 1) and not add_line:
            result_list.append(line_list)

            
for list in result_list:
    for i in range(len(list)):
        if (i != 0) and (list[i] in num_dic):
            for j in range(i, -1, -1):
                if (list[j] in num_dic[list[i]]):
                    temp_item = list[j]
                    list[j] = list[i]
                    list[i] = temp_item
                    i -= 1

    middle = len(list) // 2
    result += int(list[middle])

print(result)