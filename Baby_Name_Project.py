def readBabyNamesFile(year):
    with open(f"yob{str(year)}.txt", "r") as file:
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

def createGenderNeutral(year):
    with open("gender_neutral_names.txt", "r") as file:
        neutralNames = []
        for line in file:
            ln = line.strip()
            ln = ln.split(",")
            for i in ln:
                neutralNames.append(i)
    chgNames = readBabyNamesFile(year)
    with open(f"yob{str(year)}GN.txt", "w") as file:
        for i in neutralNames:
                while True:
                    try:
                        ndx = chgNames.index(i)
                        chgNames[ndx+1] = "N"
                        line = f"{chgNames[ndx]},{chgNames[ndx + 1]},{chgNames[ndx + 2]}"
                        del chgNames[ndx:ndx+2]
                        file.write(line + "\n")
                    except ValueError:
                        break


def createRangeFile(year, beg_name, end_name):
    names = readBabyNamesFile(year)
    nameRange = names[names.index(beg_name):(names.index(end_name)+3)]
    with open(f"yob{year}R", "w") as file:
            for i in range(0, len(nameRange)+1, 3):
                if i + 2 < len(nameRange):
                    line = f"{nameRange[i]},{nameRange[i + 1]},{nameRange[i + 2]}"
                    file.write(line + "\n")

def numBabiesInRange(year, beg, end):
    names = readBabyNamesFile(year)
    aNames = names[0::3]
    print(aNames)
    aNames = sorted(aNames)
    sNdx = 0
    eNdx = 0
    for i in aNames:
        try:
            sNdx = names.index(beg)
            eNdx = names.index(end)
        except ValueError:
            print(f"{beg} or {end} do not exist")
            return
    count = sNdx - eNdx
    return count

def listInRange(year, min, max):
    names = readBabyNamesFile(year)
    sNames = []
    for i in names[2::3]:
        if int(i) < max and int(i) > min:
            ndx = names.index(i)
            sNames.append(names[ndx-2])
    return sNames