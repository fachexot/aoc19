import math

input = open('input1.txt').readlines()
sum = 0

for i in range(len(input)):
    sum += (math.floor(float(input[i]) / 3) - 2)

print(sum)