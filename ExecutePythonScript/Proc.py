# -*- coding: utf-8 -*-

import sys
import glob
import codecs

args = sys.argv

#FilePath
product_path_name = args[1]

grep_file_name = product_path_name + "\**\*.txt"
result_file_name = "ResultGrep.txt"
hit_word = "TODO"

#サブディレクトリまで対象にする
list_up = glob.glob(grep_file_name, recursive=True)

result_open = codecs.open(result_file_name, "w", "utf-8")

return_code = 0;
for path_name in list_up:
    with open(path_name, encoding="utf8", errors='ignore') as f:
        # ファイル読み込み
        code = f.readlines()

        # 終端の改行削除
        code_cut_new_line = [line.strip() for line in code]

        # 検索ワードにヒットした行を抽出
        list_hit_line = [line for line in code_cut_new_line if hit_word in line]

        # 該当項目があれば、ファイル名出力
        if len(list_hit_line) != 0:
            result_open.write(path_name.join("\r\n"))
            return_code = 1

            # 該当行を出力
            for line in list_hit_line:
                result_open.writelines(line)
            result_open.writelines("\r\n")

result_open.close()
sys.exit(return_code)
