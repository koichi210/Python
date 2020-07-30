class English:

    def __init__(self):
        return

    def greeting1(self):
        return 'Hello'

    def greeting2(self):
        return 'Bye'

class Spanish:

    def __init__(self):
        return

    def greeting1(self):
        return 'Hola'

    def greeting2(self):
        return 'Chao'


def main():
	print ( "Eng1 =" , English().greeting1() )
	print ( "Eng2 =" , English().greeting2() )
	print ( "Spa1 =" , Spanish().greeting1() )
	print ( "Spa2 =" , Spanish().greeting2() )

if __name__ == '__main__':
	main()
