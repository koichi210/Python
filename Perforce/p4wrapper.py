# encoding:utf-8

import subprocess
import re


class P4Wrapper:

    def __init__(self):
        pass

    def create_changelist(self, comment):
        # 新規チェンジリスト作成
        # p4 change -o | sed -e "s/<enter description here>/\[New\]/g"
        # -e "s|//depot.*||g" | p4 change -i
        p4_cmd = "p4 change -o"
        p4_change_form = subprocess.check_output(p4_cmd.split())
        p4_change_form = re.sub(
            "<enter description here>",
            comment,
            p4_change_form)
        p4_change_form = re.sub("//depot.*", "", p4_change_form)

        p4_cmd = "p4 change -i"
        p4_change_p = subprocess.Popen(
            p4_cmd.split(),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE)
        p4_cl = p4_change_p.communicate(p4_change_form.encode())[0].decode()
        p4_cl = p4_cl.split()[1]
        return p4_cl

    def edit(self, chenge_list, depo_path):
        # 対象ファイルをチェックアウト
        p4_cmd = "p4 edit -c " + chenge_list + " " + depo_path
        p4_stdout = subprocess.check_output(p4_cmd.split())
        return p4_stdout

    def resotre(self, chenge_list):
        # 変更ないファイルを元に戻す
        p4_cmd = "p4 revert -a -c " + chenge_list
        p4_stdout = subprocess.check_output(p4_cmd.split())
        return p4_stdout

    def is_blank(self, chenge_list):
        # チェンジリストは空か？
        p4_cmd = "p4 opened -c " + chenge_list
        p4_stdout = subprocess.check_output(
            p4_cmd.split(), stderr=subprocess.STDOUT)
        if "File(s) not opened on this client." in p4_stdout:
            return True
        else:
            return False

    def delete(self, chenge_list):
        # チェンジリストを削除
        p4_cmd = "p4 change -d " + chenge_list
        p4_stdout = subprocess.check_output(
            p4_cmd.split(), stderr=subprocess.STDOUT)
        return p4_stdout
