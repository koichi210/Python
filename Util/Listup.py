import glob

grep_target_path = "d:\Source\**\*.h"

#相対パスを絶対パスへ変換
#os.path.abspath(path_name)

#ファイルリスト作成
list_up = glob.glob(grep_target_path, recursive=True)
print(list_up)

for path_name in list_up:
    with open(path_name) as f:
        # ファイル読み込み
        code = f.readlines()

        # 終端の改行削除
        code_cut_new_line = [line.strip() for line in code]

        # includeの行を抽出
        listup_include = [line for line in code_cut_new_line if "#include" in line]

        # Sampleの行を抽出
        listup_sample = [line for line in listup_include if "Sample" in line]

        # Originalが含まれない行を抽出
        listup_not_origin = [line for line in listup_sample if "Original" not in line]

        # 該当項目があれば、ファイル名出力
        if len(listup_not_origin) != 0:
            print("\r\n")
            print(path_name)

        # 該当行を出力
        for line in listup_not_origin:
            print(line)
