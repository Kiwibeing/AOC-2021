def mul(a, b):
    return a * b

with open('input2.txt', 'r') as file:
    input = file.readlines()
horizontal = []
vertical = []
input_length = len(input)
for i in range(input_length):
    number = int(input[i][-2])
    if "forward" in input[i]:
        horizontal.append(number)
    elif "down" in input[i]:
        vertical.append(number)
    elif "up" in input[i]:
        up = -number
        vertical.append(up)
horizontal_sum = sum(horizontal)
vertical_sum = sum(vertical)
final = mul(horizontal_sum, vertical_sum)
print(final)

aim = 0
horizontal2 = []
vertical2 = []
for i in range(input_length):
    number = int(input[i][-2])
    if "down" in input[i]:
        aim += number
    elif "up" in input[i]:
        aim -= number
    elif "forward" in input[i]:
        horizontal2.append(number)
        vertical2.append(mul(aim, number))
horizontal2_sum = sum(horizontal2)
vertical2_sum = sum(vertical2)
final2 = mul(horizontal2_sum, vertical2_sum)
print(final2)