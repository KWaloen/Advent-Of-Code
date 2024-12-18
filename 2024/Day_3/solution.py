
#part 1

# import re

# products = []

# with open("2024/Day_3/input","r") as file:
#     text = file.read()

#     pattern = r"mul\((\d+),(\d+)\)"

#     matches = re.findall(pattern, text)

#     for pair in matches:
#         x, y = map(int, pair)
#         product = x * y
#         products.append(product)
        

# print(sum(products))

#part 2



import re

with open("2024/Day_3/input", "r") as file:
    text = file.read()

mul_pattern = r"mul\((\d+),(\d+)\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

activate = True
products = []

for pattern in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", text):
    instruction = pattern.group(0)

    if re.match(do_pattern, instruction):
        activate = True
    elif re.match(dont_pattern, instruction):
        activate = False
    elif re.match(mul_pattern, instruction):
        if activate:
            x,y = map(int, re.findall(r"\d+", instruction))
            product = x*y
            print(product)
            products.append(product)

print(sum(products))
