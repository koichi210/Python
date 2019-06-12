import os

path_name="Sample.txt"

### forを使ったファイル読み込み
# ファイルをオープンする
f = open(path_name, "r")

# 一行ずつ読み込んでは表示する
for line in f:
  print(line)

# ファイルをクローズする
f.close()
