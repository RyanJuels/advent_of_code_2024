import sys
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')\

result = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if (lines[i][j] == "A") and (i > 0) and (i < len(lines) - 1) and (j > 0) and (j < len(lines[i]) - 1):
            # print(str(i) + " " + str(j))
            numMAS = 0
            if lines[i - 1][ j - 1] == "S":
                if lines[i + 1] [j + 1] == "M":
                    numMAS += 1
            elif lines[i - 1][ j - 1] == "M":
                if lines[i + 1] [j + 1] == "S":
                    numMAS += 1
            
            if lines[i - 1][ j + 1] == "S":
                if lines[i + 1] [j - 1] == "M":
                    numMAS += 1
            elif lines[i - 1][ j + 1] == "M":
                if lines[i + 1] [j - 1] == "S":
                    numMAS += 1

            if numMAS > 1:
                result += 1

print(result)