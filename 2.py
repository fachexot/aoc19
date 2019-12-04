input = [int(item) for item in open('input2.txt').readline().split(',')]

i = 0

input[1] = 12
input[2] = 2
#input[1] = 76
#input[2] = 10

while True:
    if input[i] == 1:
        input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
    elif input[i] == 2:
        input[input[i+3]] = input[input[i+1]] * input[input[i+2]]
    elif input[i] == 99:
        print("TERMINATED.")
        break
    else:
        print("HALT AND CATCH FIRE: " + input[i])
        break
    i += 4

print(input[0])