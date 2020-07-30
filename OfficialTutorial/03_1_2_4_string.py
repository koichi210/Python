# -*- coding: utf-8 -*-

# 文字列にIndexを指定
introduction = 'my name is python'

# my
print(introduction[0:3])

# my name
print(introduction[:7])

# my my
print(introduction[0:3] + introduction[0:3])

# my name is python
print(introduction[:3] + introduction[3:])

# your name is python
print('your' + introduction[2:])
