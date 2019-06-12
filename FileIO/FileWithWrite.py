import os

path_name="Sample.txt"

### withを使ったファイル読み込み
with open(path_name) as f:
    print(f.read())
