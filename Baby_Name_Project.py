def readBabyNamesFile(year):
    file = open(f"yob{str(year)}.txt", "r")
    elements = []
    for line in file:
        ln = line.strip()
        ln = ln.split(",")
        for i in ln:
            elements.append(i)
    return elements

def findBabyName(aName, year):
    names = readBabyNamesFile(year)
    count = 0
    while True:
        try:
            ndx = names.index(aName)
            count += int(names[ndx+2])
            del names[ndx]
        except ValueError:
            break  
    return count

def seperateGender(year):
    names = readBabyNamesFile(year)
    mFile = open(f"yob{str(year)}M.txt", "w")
    fFile = open(f"yob{str(year)}F.txt", "w")
    while True:
        try:
            ndx = names.index("M")
            line = str(names[ndx-1:ndx+2]).replace("[", "").replace("]", "").replace("'", "").replace("'", "").replace("'", "").replace(" ", "")
            mFile.write(line + "\n")
            del names[ndx-1:ndx+2]
        except ValueError:
            break
    while True:
        try:
            ndx = names.index("F")
            line = str(names[ndx-1:ndx+2]).replace("[", "").replace("]", "").replace("'", "").replace("'", "").replace("'", "").replace(" ", "")
            fFile.write(line + "\n")
            del names[ndx-1:ndx+2]
        except ValueError:
            break
    mFile.close()
    fFile.close()