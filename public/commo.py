"""
1,先考虑用例  考虑那些接口适合做自动化
2，封装通用方法
3，准备测试数据
4，编写测试用例
5，统一执行
"""
import xlrd

def get_xlsx(xls_name,sheet_name):

    cls=[]
    workBook=xlrd.open_workbook(xls_name)
    sheet = workBook.sheet_by_name(sheet_name)
    nrows = sheet.nrows

    for i  in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls

# get_xlsx("C:\\Users\\Administrator\\PycharmProjects\\interface\\testFile\\case\\userCase.xlsx","sendcode")