import sys
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

def test_acend(thisline):
    for i in range(len(thisline) - 1):
        if (int(thisline[i]) <= int(thisline[i + 1])) or (abs(int(thisline[i]) - int(thisline[i + 1])) > 3):
            return False

    return True

def test_decend(thisline):
    for i in range(len(thisline) - 1):
        if (int(thisline[i]) >= int(thisline[i + 1])) or (abs(int(thisline[i]) - int(thisline[i + 1])) > 3):
            return False

    return True


result = 0
for line in lines:
    thisline = line.split(' ')

    if test_acend(thisline):
        result += 1
    elif test_decend(thisline):
        result += 1
    else:
        for i in range(len(thisline)):
            temp_arr = thisline.copy()
            thisline.pop(i)
            if test_acend(thisline):
                result += 1
                break
            if test_decend(thisline):
                result += 1
                break
            print(thisline)
            thisline = temp_arr
    

print(result)

