array = []
print("len=", len(array))

array.append("1a AAA")
array.append("2b")
array.append("3c AAA")
array.append("4d")
array.append("5e AAA")
array.append("6f")
array.append("7g")
print("len=", len(array))
print(array)


#[AAA]を含む行を抽出
print("\r\n")
lines_grep = [line for line in array if 'AAA' in line]
print(lines_grep)

#[AAA]を含む行を行ごとに出力
print("\r\n")
for line in lines_grep:
    print(line)

#[AAA]を含む行の、最初行と最後行を出力
print("\r\n")
print("first=" + lines_grep[0])
print("last =" + lines_grep[-1])
