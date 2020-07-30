
path_name = "SampleWrite.txt"

### withを使ったファイル読み込み
with open(path_name, mode='w') as f:
    f.write('hello new world!!')

    # close不要
    # f.close()
