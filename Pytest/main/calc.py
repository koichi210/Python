class Calc: 

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def multiple(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

def main():
	print ( "add =" , Calc(1, 2).add() )
	print ( "sub =" , Calc(1, 2).sub() )
	print ( "multiple =" , Calc(1, 2).multiple() )
	print ( "divide =" , Calc(1, 2).divide() )

if __name__ == '__main__':
	main()
