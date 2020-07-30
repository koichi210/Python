class English:

    def __init__(self):
        return

    @classmethod
    def setup_class(cls):
        print('setup_class')
        #cls.cal = keisan.Keisan()

    @classmethod
    def teardown_class(cls):
        print('teardown_class')
        #del cls.cal

    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        # self.cal = keisan.Keisan()

    def teardown_method(self, method):
        print('method={}:'.format(method.__name__))
        # del self.cal

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
