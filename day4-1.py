import sys
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')\

result = 0


def checkSUp(letter, i, j):
    global result
    if lines[i - 1][j] == letter:
        if letter != "S":
            if letter == "M":
                checkSUp("A", i-1, j)
            elif letter == "A":
                checkSUp("S", i-1, j)
        else:
            print("checkSUp " + str(i) + " " + str(j))
            result += 1

def checkRUp(letter, i, j):
    global result
    if lines[i - 1][j + 1] == letter:
        if letter != "S":
            if letter == "M":
                checkRUp("A", i-1, j+1)
            elif letter == "A":
                checkRUp("S", i-1, j+1)
        else:
            print("checkRUp " + str(i) + " " + str(j))
            result += 1

def checkLUp(letter, i, j):
    global result
    if lines[i - 1][j - 1] == letter:
        if letter != "S":
            if letter == "M":
                checkLUp("A", i-1, j-1)
            elif letter == "A":
                checkLUp("S", i-1, j-1)
        else:
            print("checkLUp " + str(i) + " " + str(j))
            result += 1

def checkSDown(letter, i, j):
    global result
    if lines[i + 1][j] == letter:
        if letter != "S":
            if letter == "M":
                checkSDown("A", i+1, j)
            elif letter == "A":
                checkSDown("S", i+1, j)
        else:
            print("checkSDown " + str(i) + " " + str(j))
            result += 1

def checkRDown(letter, i, j):
    global result
    if lines[i + 1][j + 1] == letter:
        if letter != "S":
            if letter == "M":
                checkRDown("A", i+1, j+1)
            elif letter == "A":
                checkRDown("S", i+1, j+1)
        else:
            print("checkSDown " + str(i) + " " + str(j))
            result += 1

def checkLDown(letter, i, j):
    global result
    if lines[i + 1][j - 1] == letter:
        if letter != "S":
            if letter == "M":
                checkLDown("A", i+1, j-1)
            elif letter == "A":
                checkLDown("S", i+1, j-1)
        else:
            print("checkSDown " + str(i) + " " + str(j))
            result += 1

def checkSLeft(letter, i, j):
    global result
    if lines[i][j - 1] == letter:
        if letter != "S":
            if letter == "M":
                checkSLeft("A", i, j-1)
            elif letter == "A":
                checkSLeft("S", i, j-1)
        else:
            print("checkSLeft " + str(i) + " " + str(j))
            result += 1

def checkSRight(letter, i, j):
    global result
    if lines[i][j + 1] == letter:
        if letter != "S":
            if letter == "M":
                checkSRight("A", i, j+1)
            elif letter == "A":
                checkSRight("S", i, j+1)
        else:
            print("checkSRight " + str(i) + " " + str(j))
            result += 1

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "X":
            if i >= 3:
                checkSUp("M", i, j)
                if j <= (len(lines[i]) - 4):
                    
                    checkRUp("M", i, j)
                if j >= 3:
                    checkLUp("M", i, j)
            if i <= (len(lines) - 4):
                checkSDown("M", i, j)
                if j <= (len(lines[i]) - 4):
                    checkRDown("M", i, j)
                if j >= 3:
                    checkLDown("M", i, j)
            if j >= 3:
                checkSLeft("M", i, j)
            if j <= (len(lines[i]) - 4):
                checkSRight("M", i, j)


print(result)
