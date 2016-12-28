# -*- coding:utf-8 -*-

import xlwt
import json
import operator


def is_txt(str = ""):
    if 'txt' in str:
        return True
    return False


def is_download(dict):
    if 'download' in dict.keys():
        return True
    return False


def get_list(str):
    return str.get('name', '').split('_')


def read_jpg_download_data():
    """
    获取jpg下载数据列表
    """
    list = []
    for i in range(len(items)):
        item = items[i]
        if (not is_txt(item['name'])) and is_download(item):
            list.append(item)
    # 文件名称格式如：0_50_24K_jpg，对列表中的数据先按压缩比排序，压缩比一定的情况下按文件数量排序，前两个一定的情况下按文件大小排序
    # list.sort(key=lambda key: (int(key.get('name', '').split('_')[0])))
    list.sort(key=lambda key: (int(get_list(key)[0]),
                               int(get_list(key)[1]),
                               int(get_list(key)[2][0:len(get_list(key)[2])-1])))
    return list


def read_jpg_uncompress_data():
    """
    获取jpg解压数据列表
    """
    list = []
    for i in range(len(items)):
        item = items[i]
        if (not is_txt(item['name'])) and (not is_download(item)):
            list.append(item)
    list.sort(key=lambda key: (int(get_list(key)[0]),
                               int(get_list(key)[1]),
                               int(get_list(key)[2][0:len(get_list(key)[2])-1])))
    return list


def read_txt_download_data():
    """
    获取txt下载数据列表
    """
    list = []
    for i in range(len(items)):
        item = items[i]
        if is_txt(item['name']) and is_download(item):
            list.append(item)
    list.sort(key=lambda key: (int(get_list(key)[0]),
                               int(get_list(key)[1]),
                               int(get_list(key)[2][0:len(get_list(key)[2])-1])))
    return list


def read_txt_uncompress_data():
    """
    获取txt解压数据列表
    """
    list = []
    for i in range(len(items)):
        item = items[i]
        if is_txt(item['name']) and (not is_download(item)):
            list.append(item)
    list.sort(key=lambda key: (int(get_list(key)[0]),
                               int(get_list(key)[1]),
                               int(get_list(key)[2][0:len(get_list(key)[2])-1])))
    return list


def set_style(name, height=220, bold=False):
    """
    设置单元格样式
    """
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height

    # borders= xlwt.Borders()
    # borders.left= 6
    # borders.right= 6
    # borders.top= 6
    # borders.bottom= 6

    style.font = font
    # style.borders = borders

    return style


def get_uncomp_cost_by_name(list, name=''):
    for i in range(len(list)):
        item = list[i]
        if name == item['name']:
            return item['unzip']

    return 0


def gen_excel_table():
    """
    创建table
    """

    # 创建工作簿
    f = xlwt.Workbook()
    # 添加jpg sheet
    sheet1 = f.add_sheet(u'jpg下载解压速度测试', cell_overwrite_ok=True)
    jpg_title = u'jpg下载解压速度统计（单位：ms）'

    row0 = [u'序号', u'名称', u'压缩级别', u'文件数量', u'下载耗时', u'解压耗时', u'累计耗时']
    # 生成标题，合并第一行6列
    sheet1.write_merge(0, 0, 0, 6, jpg_title)
    # 生成第一行
    for i in range(0, len(row0)):
        sheet1.write(1, i, row0[i])

    # 写入下载和压缩数据
    jpg_down_list = read_jpg_download_data()
    jpg_uncomp_list = read_jpg_uncompress_data()

    for i in range(0, len(jpg_down_list)):

        name = str(jpg_down_list[i]['name'])
        download_cost = jpg_down_list[i]['download']
        uncomp_cost = get_uncomp_cost_by_name(jpg_uncomp_list, name)
        count = name.split('_')[1]

        sheet1.write(i + 2, 0, i + 1)                          # 序号
        sheet1.write(i + 2, 1, name)                                # 名称
        sheet1.write(i + 2, 2, name[0:1])                     # 压缩级别
        sheet1.write(i + 2, 3, count)                       # 文件数量
        sheet1.write(i + 2, 4, download_cost)                  # 下载耗时
        sheet1.write(i + 2, 5, uncomp_cost)                    # 解压耗时
        sheet1.write(i + 2, 6, download_cost + uncomp_cost)    # 总耗时

    # 添加txt sheet
    sheet2 = f.add_sheet(u'txt下载解压速度测试', cell_overwrite_ok=True)
    jpg_title = u'txt下载解压速度统计（单位：ms）'

    # 生成标题，合并第一行6列
    sheet2.write_merge(0, 0, 0, 6, jpg_title)
    # 生成第一行
    for i in range(0, len(row0)):
        sheet2.write(1, i, row0[i])

    # 写入下载和压缩数据
    txt_down_list = read_txt_download_data()
    txt_uncomp_list = read_txt_uncompress_data()

    for i in range(0, len(jpg_down_list)):
        name = txt_down_list[i]['name']
        download_cost = txt_down_list[i]['download']
        uncomp_cost = get_uncomp_cost_by_name(txt_uncomp_list, name)
        count = name.split('_')[1]

        sheet2.write(i + 2, 0, i + 1)                      # 序号
        sheet2.write(i + 2, 1, name)                            # 名称
        sheet2.write(i + 2, 2, name[0:1])                      # 压缩级别
        sheet2.write(i + 2, 3, count)  # 文件数量
        sheet2.write(i + 2, 4, download_cost)              # 下载耗时
        sheet2.write(i + 2, 5, uncomp_cost)                # 解压耗时
        sheet2.write(i + 2, 6, download_cost + uncomp_cost)  # 总耗时

    file_name = '压缩包性能测试.xls'
    f.save(file_name)  # 保存文件


def main():
    file = open('raw.txt')
    try:
        raw_data = file.read()
    finally:
        file.close()
    global items
    items = []
    temp = raw_data.split('\n')

    # 将文本文件内容按行转换成字典
    for i in range(len(temp)):
        if temp[i]:
            items.append(json.loads(temp[i]))
    print(items)

    gen_excel_table()

if __name__ == '__main__':
    main()