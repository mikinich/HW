import xlrd, xlwt
rb = xlrd.open_workbook('../ArticleScripts/ExcelPython/xl.xls',formatting_info=True)
sheet = rb.sheet_by_index(0)
val = sheet.row_values(0)[0]
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
wb = xlwt.Workbook()
ws = wb.add_sheet('Test')
