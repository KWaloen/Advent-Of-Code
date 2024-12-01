
with open("2024\Day_1\input","r") as file:
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

print(sum(listToSum))

