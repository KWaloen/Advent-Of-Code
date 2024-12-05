
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
    
for level in numLevelArray:
    safe = True
    
    print("new row")
    
    if ((level[0] - level[-1]) > 0):
        for i in range(len(level) - 1):
            if (level[i] >= level[i+1] and abs(level[i] - level[i+1]) < 3):
                print(level[i], "-", level[i+1], level[i] - level[i+1])
                
            else:
                safe = False
                print("unsafe")
                break
            
    if ((level[0] - level[-1] < 0)):
        for i in range(len(level) - 1):
            if (level[i] <= level[i+1] and abs(level[i] - level[i+1]) < 3):
                print(level[i], "-", level[i+1], level[i] - level[i+1])
                
            else:
                safe = False
                print("unsafe")
                break
            
    if safe == True:
        numberSafe += 1
            
print(numberSafe)
            

            
             
        
        
    
    