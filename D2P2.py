with open('day 2 input.txt') as f:
    words = f.read().splitlines()
    one = ""
    two = ""
    for x in words:
        for j in words:
            xLetters = list(x)
            jLetters = list(j)
            z = 0
            for index, y in enumerate(xLetters):
                if xLetters[index] == jLetters[index]:
                    z = z + 1
            if z == 25:
                for index, y in enumerate(xLetters):
                    if xLetters[index] != jLetters[index]:
                        xLetters.pop(index)
                        jLetters.pop(index)
                
                print("answer is: "''.join(xLetters))
                exit()
            z = 0
