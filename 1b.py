import math

input = open('input1.txt').readlines()
sum = 0

for i in range(len(input)):
    fuel = input[i]
    while True:
        fuel = (math.floor(float(fuel) / 3) - 2)
        if fuel > 0:
            sum += fuel
        else:
            break

print(sum)