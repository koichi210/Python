import os

path_name="Sample.txt"

### withを使ったファイル読み込み
with open(path_name) as f:
    lines = f.readlines()

#linesの型を出力
print(type(lines))
print("\r\n")

#linesの中身を出力
print(lines)
print("\r\n")

#[strip]で終端の改行を削除
lines_strip = [line.strip() for line in lines]

for line in lines_strip:
    print(line)
