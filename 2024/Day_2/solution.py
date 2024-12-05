
with open("2024\Day_2\input","r") as file:
    text = file.read()

row = text.rsplit("\n")

levelArrays = []
numLevelArray = []
differenceArray = []
numberSafe = 0

for elements in row: 
    levels = elements.split(" ")
    levelArrays.append(levels)
        
for level in levelArrays: 
    numLevelArray.append(list(map(int, level)))
    
# Process each row
for level in numLevelArray:
    safe = True

    increasing = None  
    for i in range(len(level) - 1):
        diff = level[i + 1] - level[i]

        if abs(diff) < 1 or abs(diff) > 3:
            safe = False
            break

        if increasing is None:
            if diff > 0:
                increasing = True
            elif diff < 0:
                increasing = False

        elif (increasing and diff < 0) or (not increasing and diff > 0):
            safe = False
            break

    if safe:
        numberSafe += 1
