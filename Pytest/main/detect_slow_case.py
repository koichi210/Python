import time

class Speed:

    def __init__(self):
        return

    def high(self):
        return 'high speed'

    def middle(self):
        time.sleep(1)
        return 'middle speed'

    def low(self):
        time.sleep(2)
        return 'low speed'

def main():
	print ( Speed().high() )
	print ( Speed().middle() )
	print ( Speed().low() )

if __name__ == '__main__':
	main()
