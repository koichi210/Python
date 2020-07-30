# マングリング機構
class Mangling:
    private_value = "test"
    _private_value = "_test"
    __private_value = "__test"

if __name__ == "__main__":
    man = Mangling()

    # 丸見え
    print(man.private_value)
    print(man._private_value)

    # エラー
    try:
       print(man.__private_value)
    except:
        print('access denied')


    # 工夫すれば見える
    # __ をつけると、プリフィックスにクラス名が付与されているだけ
    print(man._Mangling__private_value)
