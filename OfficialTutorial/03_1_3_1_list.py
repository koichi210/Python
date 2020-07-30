# -*- coding: utf-8 -*-

# リスト型
param = [1, 2, 4, 8, 16]
introduction = 'my name is python'

# すべての値
print(param)

# 先頭の値
print(param[0])

# 最後の値
print(param[-1])

# 指定Index以降の値
print(param[-3:])

# 要素追加
param.append(32)
print(param[:])

# リストの連結
print(param[:] + [64, 128])

