#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# �t�@�C�����I�[�v������
Data = open("Sample.txt", "r")

# ��s���ǂݍ���ł͕\������
for line in Data:
  print(line)

# �t�@�C�����N���[�Y����
Data.close()

