# -*- coding: utf-8 -*-

import os
import glob
import codecs

default_pathname = ""
default_filename = "*.h"
default_ignore_filename = ""

class MySearch:
    EXCLUDE_TYPE_NORMAL = 0
    EXCLUDE_TYPE_REPLACE_OWN_NAME = 1

    __exclude_type = EXCLUDE_TYPE_NORMAL
    __root_pathname = default_pathname
    __filename = default_filename
    __ignore_filename = default_ignore_filename
    __include_list = []
    __exclude_list = []
    __exclude_replacename = ["src", "dest"]

    def init(self):
        self.__include_list = []
        self.__exclude_list = []
        self.__exclude_replacename = []

    def set_root_pathname(self, val):
        self.__root_pathname = val

    def set_filename(self, val):
        self.__filename = val

    def set_ignore_filename(self, val):
        self.__ignore_filename = val

    def set_include_codename(self, *args):
        for arg in args:
            self.__include_list.append(arg)

    def set_exclude_codename(self, *args):
        for arg in args:
            self.__exclude_list.append(arg)

    def set_exclude_codename_condition_replace_ownname(self, replace_src, replace_dest):
        self.__exclude_replacename.append(replace_src)
        self.__exclude_replacename.append(replace_dest)

    def set_exclude_type(self, val):
        self.__exclude_type = val

    def listup(self):
        result_str = ""
        file_list = self.__get_file_list()
        for file_name in file_list:
			
            if (len(self.__ignore_filename) != 0) and (self.__ignore_filename in file_name):
                #対象外ファイルであればスキップ
                continue

            with open(file_name, encoding="utf8", errors='ignore') as f:
                # ファイル読み込み
                code = f.readlines()

                # 改行削除し読み込む行数を縮小
                code = [line.strip() for line in code]

                # 対象の行を抽出
                code = self.__trim_include_code(code)
                code = self.__trim_exclude_code(code)

                #virtual部分
                if ( self.__exclude_type == self.EXCLUDE_TYPE_REPLACE_OWN_NAME ) :
                    code = self.__trim_exclude_replace_ownname(file_name, code)

                # 該当項目があれば、ファイル名出力
                if len(code) != 0:
                    result_str = self.__append_result(result_str, code, file_name)

        return result_str

    def __get_file_list(self):
        grep_file_name = self.__root_pathname + self.__filename

        #リスト作成
        file_list = glob.glob(grep_file_name, recursive=True)
        return file_list

    def __trim_include_code(self, code):
        for include_name in self.__include_list:
            code = [line for line in code if include_name in line]
        return code

    def __trim_exclude_code(self, code):
        for exclude_name in self.__exclude_list:
            code = [line for line in code if exclude_name not in line]
        return code

    def __trim_exclude_replace_ownname(self, file_name, code):
        fname = os.path.basename(file_name)
        fname = fname.replace(
            self.__exclude_replacename[0],
            self.__exclude_replacename[1])

        code = [line for line in code if fname not in line]
        return code

    def __append_result(self, result_str, code, __filename):
        result_str += __filename + "\r\n"

        # 該当行を出力
        for line in code:
            result_str += line + "\r\n"
        result_str += "\r\n"
        return result_str

class MyFileIO:
    def file_write(self, file_name, mode, data):
        result_open = codecs.open(file_name, mode, "utf-8")
        result_open.write(data)
        result_open.close()
