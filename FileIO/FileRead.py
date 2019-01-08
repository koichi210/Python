#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# ファイルをオープンする
Data = open("Sample.txt", "r")

# 一行ずつ読み込んでは表示する
for line in Data:
  print(line)

# ファイルをクローズする
Data.close()

