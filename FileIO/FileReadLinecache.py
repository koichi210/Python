import os
import linecache

path_name = "Sample.txt"

user_name = linecache.getline(path_name, 1).rstrip('\n')
print(user_name)

data = linecache.getline(path_name, 2).rstrip('\n')
print(data)

linecache.clearcache() 