# -*- coding: utf-8 -*-
#Csv2Excel_to_excel

import pandas as pd     # Anaconda
import openpyxl as opx

TemplateExcelName = './Sample/Template.xlsx'
ReadCsvName = './Sample/SourceData.csv'
WriteExcelName = './Sample/Template_new.xlsx'
WriteDataSheetName = 'SourceData'
WriteTemplateSheetName = 'Template'

writer = pd.ExcelWriter(WriteExcelName)

df_data = pd.read_csv(ReadCsvName, index_col=0)
df_data.to_excel(writer,sheet_name=WriteDataSheetName)

#グラフが持ってこれていない。。
df_template = pd.read_excel(TemplateExcelName, index_col=0)
df_template.to_excel(writer,sheet_name=WriteTemplateSheetName)

writer.save()
