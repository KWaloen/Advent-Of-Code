# Part 1

with open("2024/Day_1/input","r") as file:
    text = file.read()

row = text.rsplit("\n")

leftList = [] 
rightList = []

for elements in row: 
    element = elements.split(",")
    
    for pairs in element:
        pair = pairs.split("  ")
        leftList.append(int(pair[0]))
        rightList.append(int(pair[1]))

leftList.sort()
rightList.sort()

listToSum = []

for i in range(len(leftList)):
    listToSum.append((abs(leftList[i]-rightList[i])))

sum(listToSum)

# --------------------------------------------------------- #

# Part 2

leftListSimilaritySum = 0

for leftElement in leftList:
    
    if leftElement in rightList:
        occurance = rightList.count(leftElement)
        if occurance != 0:
            leftListSimilaritySum += (leftElement * occurance)


    

