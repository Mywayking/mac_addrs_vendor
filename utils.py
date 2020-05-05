"""
-------------------------------------------------
   Author :       galen
   date：          2018/3/19
-------------------------------------------------
   Description:
-------------------------------------------------
"""
import os
import datetime
from functools import reduce

# 项目路径
project_path = os.path.dirname(os.path.abspath(__file__))


def read_txt(filename):
    """读取文件"""
    with open(filename, 'r') as f:
        while True:
            lines = f.readline().strip('\n')
            if not lines:
                break
            yield lines


def read_txt_all(filename):
    """读取整个文件"""
    with open(filename, 'r') as f:
        return f.readlines()


def save_to_data_file(data, filename, mode="a"):
    """保存文件"""
    with open(filename, mode)as f:
        f.write(data)


def save_to_datas_file(data_list, filename, mode="a"):
    """
    保存文件
    """
    with open(filename, mode)as f:
        for data in data_list:
            f.write(data + "\n")


def deduplication_data(data_path):
    # 数据shell命令去重
    command = "awk '!a[$0]++' {0}|sort -o {1}".format(data_path, data_path)
    print(command)
    os.system(command)


def file_consolidation(data_path, data_path_all):
    # 数据shell命令去重
    command = "cat {0} >> {1}".format(data_path, data_path_all)
    print(command)
    os.system(command)


def time():
    # 生成时间戳字符串
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d')


def list_deduplication(data_list):
    # 去重列表
    return reduce(lambda x, y: x if y in x else x + [y], [[], ] + data_list)


def delete_existed_file(path):
    # 删除已存在文件
    if os.path.exists(path):
        print("删除已存在文件夹:{}".format(path))
        os.remove(path)
    print("不存在文件夹:{}".format(path))


def cp_oui_common(file_v):
    common_path = "/Users/wangchun/IdeaProjects/common/src/main/resources/macAddrs"
    command_delete = "rm -rf {0}/out_*".format(common_path)
    command_cp = "cp {0}/resources/{1}/out_* {2}".format(project_path, file_v, common_path)
    print(command_delete)
    print(command_cp)
    os.system(command_delete)
    os.system(command_cp)


if __name__ == '__main__':
    # print(project_path)
    cp_oui_common("20180413")
