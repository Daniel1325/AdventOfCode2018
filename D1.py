with open('day 1 input.txt') as f:
    words = f.read().splitlines()
    z = 0
    x = 0
    y = 0
    firstLoop = True
    finalLoop = False
    memory = set()
    t = 0
    while finalLoop == False:
        for a in words:
            if finalLoop == False:
                if a[0] == "-":
                    z = z - int(a[1:])
                else:
                    z = z + int(a[1:])
                if z in memory:
                    y = z 
                    finalLoop = True
                    break
                memory.add(z)
        t = t + 1
        print("Number of loops: " + str(t))
        if firstLoop:
            x = z
            firstLoop = False
    print("Frequency after single loop: " + str(x))
    print("First duplicate: " + str(y))