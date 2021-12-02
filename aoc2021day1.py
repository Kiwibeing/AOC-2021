with open('input.txt', 'r') as file:
    input = file.readlines()
input_int = [int(i) for i in input]
length = len(input_int)
counter = 0
for i in range(0, length - 1, 1):
    if input_int[i] < input_int[i + 1]:
        counter += 1
print(counter)

counter2 = 0
for j in range(length - 2):
    sliding_window1 = sum(input_int[j: j + 3])
    sliding_window2 = sum(input_int[j + 1: j + 4])
    if sliding_window2 > sliding_window1:
        counter2 += 1
print(counter2)