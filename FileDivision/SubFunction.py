def func(str):
    print("this code is sub function str=" + str)

# 直接呼ばれた場合
if __name__ == '__main__':
    print("direct call !!")
else:
    print("indirect call !!")

print("call by {}".format(__name__))
