with open('day 2 input.txt') as f:
    words = f.read().splitlines()
    a = False
    b = False
    c = 0
    d = 0
    for x in words:
        letters = list(x)
        for y in letters:
            if letters.count(y) == 2:
                a = True
            if letters.count(y) == 3:
                b = True
        if a:
            c += 1
        if b:
            d += 1
        a = False
        b = False
    print(c * d)