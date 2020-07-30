#クラス変数、インスタンス変数

class Hoge:
    # クラス変数
    cls_val = 123456
    cls_str = 'class member'

    # selfはインスタンスハンドラー
    def __init__(self, val, str):
        # インスタンス変数
        self.inst_val = val
        self.inst_str = str

if __name__ == "__main__":
    hoge = Hoge(100, 'instance')

    # クラスオブジェクトからクラス変数にアクセス
    print(Hoge.cls_val)
    print(Hoge.cls_str)

    # クラスオブジェクトからインスタンス変数にアクセス
    try:
        print(Hoge.inst_val)
    except:
        print('access denied')

    try:
        print(Hoge.inst_str)
    except:
        print('access denied')

    # インスタンスオブジェクトからクラス変数にアクセス
    print(hoge.cls_val)
    print(hoge.cls_str)

    # インスタンスオブジェクトからインスタンス変数にアクセス
    print(hoge.inst_val)
    print(hoge.inst_str)
