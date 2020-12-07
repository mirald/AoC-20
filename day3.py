def traverse(f):
    file = open(f, "r")
    position = 0
    position2 = [0, 2, 4, 6, 0]
    counter = [0,0,0,0]
    odd = True
    
    tree = 0

    for line in file:
        # position = position % len(line.rstrip("\n"))
        position2 = [i % len(line.rstrip("\n")) for i in position]
        
        for index, elem in enumerate(position2):
            if index < (len(position2) - 1) or odd:
                square = line[elem]
                if square == "#":
                    counter[elem] = counter[elem]+1

                tree = tree + 1

                if index == len(position2) - 1:
                    odd = not odd
            position = position + 3

    return tree
print(traverse("input3.txt"))