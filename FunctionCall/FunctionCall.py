#Sub Method
def FuncPrint(str):
    print(str)

def FuncWithReturn(val):
    if ( val == 0):
        return val, '値は0です'
    else:
        return val, '値は0以外です'

#Main Method
print("START")

str = "Hello World!!"
FuncPrint(str)

FuncPrint(3+3)
FuncPrint(3-3)
FuncPrint(3*3)
FuncPrint(3/3)
FuncPrint(3%3)
print("\r\n")

ret = FuncWithReturn(0)
print(ret)
print(ret[0])
print(ret[1])
print("\n")

ret1, ret2 = FuncWithReturn(1)
print(ret1)
print(ret2)
print("\n")

print("END")
