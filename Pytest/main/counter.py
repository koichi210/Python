class Counter: 

    def __init__(self):
        print("init")
        self.counter = 0

    def Increment(self):
        print("inc=", self.counter)
        self.counter += 1
        return self.counter

    def Decrement(self):
        print("dec=", self.counter)
        self.counter -= 1
        return self.counter


def main():
	print ( "1. " , Counter().Increment() )
	print ( "2. " , Counter().Increment() )
	print ( "3. " , Counter().Decrement() )
	print ( "4. " , Counter().Decrement() )
	print ( "5. " , Counter().Decrement() )

if __name__ == '__main__':
	main()
