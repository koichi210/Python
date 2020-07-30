
str = "hello,python"

# スライス
print(str)
print(str[2:5])
print(str[6:])
print(str[:5])
print(str[:])

# スライスした文字列は別オブジェクトになる
s1 = [0, 1, 2, 3, 4, 5]
s2 = s1[:]
print(id(s1), s1)
print(id(s2), s2)

# ステップ
s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = s[::2]  # 偶数
odd = s[1::2]  # 奇数
print(even)
print(odd)

# リバース
print(str[::-1])
