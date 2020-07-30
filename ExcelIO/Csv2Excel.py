# -*- coding: utf-8 -*-
#Csv2Excel_UnitCell

import win32com.client as win32
import pathlib

TemplateExcelName = './Sample/Template.xlsx'
ReadCsvName = './Sample/SourceData.csv'
WriteExcelName = './Sample/Template_new.xlsx'


#Excel使う準備
xlApp = win32.Dispatch('Excel.Application')
xlApp.Visible = 1

# Bookを開く
TemplateExcelAbsName = pathlib.Path(TemplateExcelName).resolve()
WorkBook = xlApp.Workbooks.Open(TemplateExcelAbsName)

# Sheetを選択する[1相対]
Sheet = xlApp.Workbooks(1).Sheets(1)

#Csvファイルを開く
ReadCsvFile=open(ReadCsvName,'r')

for i,line in enumerate(ReadCsvFile.readlines()):
	for n,label in enumerate(line.split(',')):
		cell = Sheet.Cells(i+1,n+1)		#[A1] = Cells(1,1)
		cell.Value = label.replace('\n','') # 終端の不要な改行削除

# pathlib.WindowsPath型
WriteExcelAbsName_Object = pathlib.Path(WriteExcelName).resolve()

#Str型
WriteExcelAbsName = str(WriteExcelAbsName_Object)

WorkBook.SaveAs(WriteExcelAbsName)
WorkBook.Close()
