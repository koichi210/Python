class Duty(object):

    # コンストラクタ
    def __init__(self):

        # publicメンバ変数
        self.pub_val = 1

        # privateメンバ変数
        self.__pri_val = 2

    # class public変数
    class_pub_val = 30

    # class private変数
    __class_pri_val = 40

    # public method
    def PublicMethod(self):
        return self.pub_val + self.__pri_val

    # private method
    def __PrivateMethod(self):
        return self.pub_val * self.__pri_val


if __name__ == "__main__":
    d = Duty()

    print(d.pub_val)
    print(d.PublicMethod())
