def findPassword(f):
    file = open(f, "r")
    amtValid = 0

    for line in file:
        split = line.split()
        minmax = split[0].split("-")
        min = int(minmax[0])
        max = int(minmax[1])
        letter = split[1].rstrip(":")
        password = split[2]

        # numLetters = countChars(password, letter)
        if(max > len(password)):
            max = len(password)
        correct = (letter == password[min-1]) != (letter == password[max-1])

        # if (min <= numLetters) and (numLetters <= max):
        if (correct):
            amtValid = amtValid + 1
    return amtValid

def countChars(password, letter):
    numberofletters = 0
    for c in password:
        if c == letter:
            numberofletters = numberofletters + 1
    return numberofletters


print(findPassword("input2.txt"))