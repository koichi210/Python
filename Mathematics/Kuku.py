# calculate
def calc_kuku():
    result = []
    for num1 in range(1, 10):
        tmp = []
        for num2 in range(1, 10):
            tmp.append(f'{num1 * num2:2}')
        result.append(tmp)
    return result

# Main
result = calc_kuku()
for row in result:
    print(', '.join(row))

