
def paired(f):
    file = open(f, "r")
    values = dict()

    for line in file:
        firstPair = line.rstrip("\n")
        values[firstPair] = int(firstPair)
        diff = 2020 - int(firstPair)
        pair = values.get(str(diff))
        if not pair is None:
            return pair*int(firstPair)

def triple(f):
    file = open(f, "r")
    values = dict()

    for line in file:
        firstPair = line.rstrip("\n")
        diff = 2020 - int(firstPair)
        for key in values:
            secondPair = int(key)
            rest = diff - int(key)
            if rest > 0:
                thirdPair = values.get(str(rest))
                if not thirdPair is None:
                    print(str(firstPair) + " " + str(secondPair) + " " + str(thirdPair))
                    return int(firstPair)*secondPair*thirdPair
        values[firstPair] = int(firstPair)

print(triple("input1.txt"))