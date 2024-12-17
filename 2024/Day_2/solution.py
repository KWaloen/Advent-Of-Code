
#part 1

#with open("2024\Day_2\input","r") as file:
#    text = file.read()
#
#row = text.rsplit("\n")
#
#levelArrays = []
#numLevelArray = []
#differenceArray = []
#numberSafe = 0
#
#for elements in row: 
#    levels = elements.split(" ")
#    levelArrays.append(levels)
#        
#for level in levelArrays: 
#    numLevelArray.append(list(map(int, level)))
#    
#for level in numLevelArray:
#    safe = True
#
#    increasing = None  
#    for i in range(len(level) - 1):
#        diff = level[i + 1] - level[i]
#
#        if abs(diff) < 1 or abs(diff) > 3:
#            safe = False
#            break
#
#        if increasing is None:
#            if diff > 0:
#                increasing = True
#            elif diff < 0:
#                increasing = False
#
#        elif (increasing and diff < 0) or (not increasing and diff > 0):
#            safe = False
#            break
#
#    if safe:
#        numberSafe += 1



#part 2

with open("2024/Day_2/input","r") as file:
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

for level in numLevelArray:
    flaws = 0
    increasing = None  
    new_level = []  # Collect valid elements here

    # Iterate over level without modifying it
    for i in range(len(level) - 1):
        diff = level[i + 1] - level[i]

        if abs(diff) < 1 or abs(diff) > 3:
            flaws += 1
            continue  # Skip adding this element to new_level

        new_level.append(level[i])  # Add valid elements

        if increasing is None:
            if diff > 0:
                increasing = True
            elif diff < 0:
                increasing = False

        elif (increasing and diff < 0) or (not increasing and diff > 0):
            flaws += 1

    # Add the last element (not included in the loop) to new_level
    new_level.append(level[-1])

    if flaws < 2:
        numberSafe += 1
    if flaws > 2:
        print(new_level)  # Print the cleaned level list

print(numberSafe)