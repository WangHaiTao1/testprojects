import xlrd
host = "C:\\Users\\Administrator\\PycharmProjects\\interface\\testFile\\case\\userCase.xlsx"
workpace = xlrd.open_workbook(host) # 打开xlsx文件

sheet = workpace.sheets()[0]#获取sheet列表
sheet1 = workpace.sheet_by_name("sendcode")#以sheet名获取sheet对象
print(sheet1)
print(sheet)

sheet2 = workpace.sheet_names()#sheet名字列表
print(sheet2)

nrows = sheet.nrows#获取sheet里的总行数
print(nrows)

ncols = sheet.ncols#获取sheet里的总列数
print(ncols)

name = sheet.name#获取sheet名称
print(name)

rows = sheet.row_values(2) #获取第几行内容
print(rows)

cols = sheet.col_values(1)#获取第几列内容
print(cols)

cell = sheet.cell(1,0).value.encode("utf-8")#获取第几列的第几行内容
print(sheet.cell_value(1,0).encode("utf-8"))
print(sheet.row(1)[0].value.encode("utf-8"))
print(cell)
