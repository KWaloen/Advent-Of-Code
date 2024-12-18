import re

products = []

with open("2024/Day_3/input","r") as file:
    text = file.read()

    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, text)

    for pair in matches:
        x, y = map(int, pair)
        product = x * y
        products.append(product)
        

print(sum(products))
