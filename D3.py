with open('day 3 input.txt') as f:
    words = f.read().splitlines()
    z = 0
    plots = [[0 for x in range(1000)] for y in range(1000)]
    for a in words:
        instruction = a.split(" ")
        num = instruction[0][1:]
        xCord = instruction[2].split(",")[0]
        yCord = instruction[2].split(",")[1][:-1]
        xInc = instruction[3].split("x")[0]
        yInc = instruction[3].split("x")[1]
        for i in range (int(xInc)):
            for j in range (int (yInc)):
                if plots[int(xCord) + i - 1][int(yCord) + j - 1] != 0:
                    if plots[int(xCord) + i - 1][int(yCord) + j - 1] != "x":
                        z = z + 1
                    plots[int(xCord) + i - 1][int(yCord) + j - 1] = "x"
                else: 
                    plots[int(xCord) + i - 1][int(yCord) + j - 1] = int(num)
    plotsAsArray = []
    for i in range(1000):
        for j in range(1000):
            plotsAsArray.append(plots[i][j])
    for a in words:
        instruction = a.split(" ")
        num = instruction[0][1:]
        print("searching: " + num + "     area is: " + str(int(instruction[3].split("x")[1]) * int(instruction[3].split("x")[0])) + "     count is " + str(plotsAsArray.count(int(num))))
        if plotsAsArray.count(int(num)) == (int(instruction[3].split("x")[1]) * int(instruction[3].split("x")[0])):
            q = num
print("Number of overlapped spots: " + str(z))
print("The one with no overlaps is: " + str(q))
