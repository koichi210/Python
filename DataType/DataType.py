# () , を使用した型はタプル
# 値を変えることはできない
tuple_data = (1, 'Hokkaido', 47, 'Okinawa')
print(tuple_data)
print(type(tuple_data))


# [] , を使用した型はリスト
# 値を変えることができる
list_data = [1, 'Hokkaido', 47, 'Okinawa']
print(list_data)
print(type(list_data))

list_data[0] = 0
list_data[1] = 'Aomori'
print(list_data)

# {} : , を使用した型は辞書
dict_data = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5}
print(dict_data)
print(type(dict_data))

# {} , を使用した型はセット
# index参照できない
# 重複は削除
set_data = {1, 2, 3, 4, 5}
print(set_data)
print(type(set_data))

set_data = set([1, 2, 3])
print(set_data)
print(type(set_data))

set_data = set(list_data)
print(set_data)
print(type(set_data))

set_data = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5}
print(set_data)
