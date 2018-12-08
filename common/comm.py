import xlrd
import requests
import paramunittest
def get_xls(xls_name,sheetname):
    cls = []
    host = "C:\\Users\\Administrator\\PycharmProjects\\interface\\testFile\\case\\"
    openExcel = xlrd.open_workbook(host+xls_name)
    sheet = openExcel.sheet_by_name(sheetname)
    nrows = sheet.nrows
    print(nrows)

    for i in range(nrows):
        print(sheet.row_values(i)[0])
        if sheet.row_values(i)[0] != u'case_name':
            if sheet.row_values(i)[-1] != "":

                sheet.row_values(i).append(int(sheet.row_values(i)[-1]))
                del sheet.row_values(i)[-2]
            cls.append(sheet.row_values(i))
    return cls
print(get_xls("userCase.xlsx","login"))
# def get_data(name,row,cols):
#     sheet = get_xls(name)
#     data = int(sheet.cell_value(row,cols))
#     return str(data)
# import readConfig
# mobile = get_data("login",1,3)
# cf= readConfig.ReadConfig()
# url = cf.get_http("baseurl")+"/api/v1/cfuser/sendCode/"+mobile
# re = requests.post(url)
# print(re.json())