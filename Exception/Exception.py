# try~except
def devide(a, b):
    try:
        c = a / b
        print(c)
    except ZeroDivisionError as e:
        print('ZeroDiv')
        print(e)
        print(type(e))
    except TypeError as e:
        print('TypeErr')
        print(e)
        print(type(e))
    except:
        print('Other Error')

def devide2(a, b):
    try:
        c = a / b
        print(c)
    except (ZeroDivisionError, TypeError) as e:
        print(e)
        print(type(e))
    except:
        print('Other Error')


if __name__ == "__main__":
    devide(2, 1)
    devide(1, 0)
    devide('a', 'b')

    devide2(2, 1)
    devide2(1, 0)
    devide2('a', 'b')
