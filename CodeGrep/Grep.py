# -*- coding: utf-8 -*-

import sys
import Function

result_file_name = "output.txt"
result_str = ""

#instance
search = Function.MySearch()

#root path
#(ex)D:\Data\CS
args = sys.argv
if len(sys.argv) >= 2:
    search.set_path_name(args[1])
else:
    print("no argument specified!! default path set")
    search.set_path_name("..\..\CS")


### "//"コメントを検索
search.init()

#target file name
search.set_filename("\**\*.cs")

#抽出条件を設定
search.set_include_codename("TODO")
search.set_exclude_codename("TBD", "確認中")

#結果取得
result_rule_violation = search.listup()
if(len(result_rule_violation) != 0):
    result_str += "[Result]" + "\r\n"
result_str += result_rule_violation


#結果をファイル出力
fio = Function.MyFileIO()
fio.file_write(result_file_name, "w", result_str)

#戻り値設定
return_code = 0
if ( len(result_str) != 0):
    return_code = 1

if len(sys.argv) >= 2:
    sys.exit(return_code)
