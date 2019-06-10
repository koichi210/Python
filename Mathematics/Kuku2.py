# calculate
result = [[f'{num1 * num2:2}' for num2 in range(1, 10)] for num1 in range(1, 10)]

#print
for count, row in zip(range(1, 10), result):
    print(', '.join(row))
