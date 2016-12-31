# -*- coding: utf-8 -*-

import hgapi
import xlwt
from datetime import *
from collections import Counter


class Log:

    changeset = ''
    user = ''
    date = date.today()
    branch = 'default'
    tag = 'tip'
    summary = ''

    def __init__(self, str = ''):
        # data = str.split('\n')
        # length = len(data)

        # if length == 6:
        #     self.changeset = data[0].split(': ')[1].lstrip()
        #     self.branch = data[1].split(': ')[1].lstrip()
        #     self.tag = data[2].split(': ')[1].lstrip()
        #     self.user = data[3].split(': ')[1].lstrip()
        #     self.date = data[4].split(': ')[1].lstrip()
        #     self.summary = data[5].split(': ')[1].lstrip()
        # elif length == 5:
        #     self.changeset = data[0].split(': ')[1].lstrip()
        #     self.branch = data[1].split(': ')[1].lstrip()
        #     self.user = data[2].split(': ')[1].lstrip()
        #     self.date = data[3].split(': ')[1].lstrip()
        #     self.summary = data[4].split(': ')[1].lstrip()
        self.user = '\'' + str[str.find('user:') + 5:len(str)].lstrip().split('\n')[0] + '\''

    def __del__(self):
        pass

    def __repr__(self):
        return self.user


if __name__ == '__main__':
    # repo_path = 'D:/work/com_pro/as-emp-5.3/ryt_android'
    # repo = hgapi.Repo(repo_path)
    # logs = repo.hg_log().split('\n\n')
    #
    # log_list = []
    # for i in range(len(logs)):
    #     log_list.append(Log(logs[i]))
    # along = list(set(log_list))
    # log_dict = {}
    # for i in range(len(along)):
    #     key = along[i]
    #     val = log_list.count(key)
    #     log_dict[key] = val

    # print(log_list)
    log_list = []
    values_count = Counter(log_list)
    comm = values_count.most_common()
    # print(str(comm[0][1]))
    # print(comm)

    # 创建工作簿
    f = xlwt.Workbook()
    # 添加jpg sheet
    sheet1 = f.add_sheet(u'jpg下载解压速度测试', cell_overwrite_ok=True)
    title = u'hg 提交记录统计'

    row0 = [u'name', u'count']
    # 生成标题，合并第一行6列
    sheet1.write_merge(0, 0, 0, 6, title)
    # 生成第一行
    for i in range(0, len(row0)):
        sheet1.write(1, i, row0[i])

    # 生成后续行
    for j in range(2, len(comm) + 2):
        sheet1.write(j, 0, comm[j-2][0])
        sheet1.write(j, 1, comm[j-2][1])

    file_name = 'hg 提交记录统计.xls'
    f.save(file_name)  # 保存文件