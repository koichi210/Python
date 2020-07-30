from calc import Calc

class CalcEx(Calc): 
    def __init__(self):
        pass

    def muldiv(self, a, b, c):
        mul = Calc(a, b).multiple()
        val = Calc(mul, c).divide()
        print ( "muldiv =", val )
    
def main():
    clc_ex = CalcEx()
    clc_ex.muldiv(7, 3, 4)

if __name__ == '__main__':
	main()
