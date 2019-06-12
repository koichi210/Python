import codecs

# -*- coding:utf-8 -*-

utf8_csv_path='utf8.csv'

sjis_csv_path='shift-jis.csv'

utf8_open = codecs.open(utf8_csv_path, "r", "utf-8")
sjis_open = codecs.open(sjis_csv_path, "w", "shift_jis")
for row in utf8_open:
    sjis_open.write(row)
sjis_open.close()
utf8_open.close()

# Memo
#ファイルオープン時に以下のようなエラーが出た場合
#  File "CheckInclude.py", line 18, in <module>
#    code = f.readlines()
#UnicodeDecodeError: 'cp932' codec can't decode byte 0xea in position 261: illegal multibyte sequence

#以下のようにopen処理を変えると良い
# before    with open(path_name) as f:
# after     with open(path_name, encoding="utf8", errors='ignore') as f:
