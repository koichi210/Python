# -*- coding: utf-8 -*-
#Csv2Excel_copy2

import os
import shutil
import pandas as pd     # Anaconda
import pathlib
import openpyxl
#import openpyxl as opx

TemplateExcelName = './Sample/Template.xlsx'
ReadCsvName = './Sample/SourceData.csv'
WriteExcelName = './Sample/Template_new.xlsx'
WriteDataSheetName = 'SourceData'
WriteTemplateSheetName = 'Template'

#すでにファイルが存在していたら削除する
WriteExcelAbsName = pathlib.Path(WriteExcelName).resolve()
if os.path.isfile(WriteExcelAbsName) :
	os.remove(WriteExcelAbsName)

#BookCopy
TemplateExcelAbsName = pathlib.Path(TemplateExcelName).resolve()
shutil.copy2(TemplateExcelAbsName, WriteExcelAbsName)

#CreateSheet
WorkBookDest = openpyxl.load_workbook(WriteExcelAbsName)

WorkSheet = WorkBookDest.create_sheet(index=1, title=WriteDataSheetName)

WorkBookDest.save(WriteExcelAbsName)
