# -*- coding: utf-8 -*-
#Csv2Excel_append

import csv 
import openpyxl 

TemplateExcelName = './Sample/Template.xlsx'
ReadCsvName = './Sample/SourceData.csv'
WriteExcelName = './Sample/Template_new.xlsx'

# Bookを開く
WorkBook = openpyxl.load_workbook(TemplateExcelName)
WorkSheet = WorkBook.active

f = open(ReadCsvName) 
reader = csv.reader(f, delimiter=',') 
for row in reader: 
     WorkSheet.append(row) 

WorkBook.save(WriteExcelName)
WorkBook.close()
