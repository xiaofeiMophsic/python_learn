# -*- coding: utf-8 -*-

import xdrlib, sys
import xlrd


def open_xls(file="a.xlsx"):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print("读取文件发生错误:{0}".format(e))


#根据索引获取表格中的数据
def excel_table_by_index(file="a.xlsx", column_index = 1, by_index = 0):
    data = open_xls(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    ncols = table.ncols

    colnames = table.row_values(column_index)

    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]

            list.append(app)
    return list


def excel_table_by_name(file="a.xlsx", column_index = 1, by_name = u"Sheet1"):
    data = open_xls(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows
    colnames = table.row_values(column_index)

    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]

            list.append(app)

    return list

def main():
    tables = excel_table_by_index("../a.xlsx")
    for row in tables:
        print(row)
    print("=========================分隔符===========================")
    tables2 = excel_table_by_name("../a.xlsx")
    for i in range(1, len(tables2)):
        print(tables2[i])

if __name__ == '__main__':
    main()