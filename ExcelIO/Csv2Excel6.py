# -*- coding: utf-8 -*-
#Csv2Excel_copy2

import os
import shutil
import pandas as pd     # Anaconda
import pathlib
import openpyxl
#import openpyxl as opx

import shutil

TemplateExcelName = './Sample/Template.xlsx'
ReadCsvName = './Sample/SourceData.csv'
WriteExcelName = './Sample/Template_new.xlsx'
WriteDataSheetName = 'SourceData'
WriteTemplateSheetName = 'Template'

#0.テンプレートファイルコピー
if os.path.isfile(TemplateExcelName):
	shutil.copyfile(TemplateExcelName, WriteExcelName)

#1.ペースト
#→Case1シート作成
df = pd.read_csv(ReadCsvName, index_col = 0)
df.to_excel(WriteExcelName, sheet_name='Test Sheet', startrow = 10, startcol = 10)

#3.
#Case1シートにpasteシートにデータをプロット。


##すでにファイルが存在していたら削除する
#WriteExcelAbsName = pathlib.Path(WriteExcelName).resolve()
#if os.path.isfile(WriteExcelAbsName) :
#	os.remove(WriteExcelAbsName)
#
##BookCopy
#TemplateExcelAbsName = pathlib.Path(TemplateExcelName).resolve()
#shutil.copy2(TemplateExcelAbsName, WriteExcelAbsName)
#
##CreateSheet
#WorkBookDest = openpyxl.load_workbook(WriteExcelAbsName)
#
#WorkSheet = WorkBookDest.create_sheet(index=1, title=WriteDataSheetName)
#
#WorkBookDest.save(WriteExcelAbsName)
