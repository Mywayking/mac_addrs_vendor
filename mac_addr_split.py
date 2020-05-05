from utils import *
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--date', '-d', type=str, default='')
args = parser.parse_args()
date_now = args.date
print(date_now)
origin_new = {}


def re_name(data_list):
    for d in data_list:
        words = d.split(" ")
        if len(words) < 2:
            continue
        if d in origin_new:
            continue
        origin_new[d] = words[0] + words[1].title()


def clean_vendor_name(vendor):
    # 清洗vendor字符串
    # if "#" in vendor:
    #     vendor = vendor.split("#")[0]
    return vendor.strip("-").strip(",").strip("?").strip().replace("Co.,Ltd", "").replace("[TR?]", "").replace(",Inc.",
                                                                                                               "")


def get_repeat_vendor(origin_data=None):
    # 获取重复数据
    if origin_data is None:
        origin_data_path = project_path + "/resources/20180413/wireshark.txt"
        origin_data = read_txt_all(origin_data_path)
    n = 1
    # k-缩写 v-[]
    vendor_names_dict = {}
    for line in origin_data:
        line = line.strip().strip("\n")
        vendor_name = ""
        vendor_values = ""
        n += 1
        if len(line) == 0:
            continue
        if line.startswith("#"):
            continue
        line = re.sub('\t+', '\t', line)
        data = line.split("\t")
        if len(data) == 2:
            vendor_name = data[1].strip()
            vendor_values = vendor_name
        elif len(data) > 2:
            vendor_name = data[1].strip()
            vendor_values = data[2].strip().replace("#", "")
        else:
            print("2异常的mac地址", line)
        if vendor_name is "":
            print("3异常的mac地址：", line)
            continue
        if vendor_name in vendor_names_dict:
            vendor_names_dict[vendor_name].append(vendor_values)
        else:
            vendor_names_dict[vendor_name] = [vendor_values]
    repeat_list = []
    repeat_path = project_path + "/resources/20180413/repeat.txt"
    for k, v in vendor_names_dict.items():
        v = list_deduplication(v)
        if len(v) > 5:
            re_name(v)
            repeat_list.append(k + "^" + "\t".join(v))
    delete_existed_file(repeat_path)
    save_to_datas_file(repeat_list, repeat_path)


def split_mac_data(date_str):
    # 拆分数据,过滤到不同文件夹
    origin_data_path = project_path + "/resources/{0}/wireshark.txt".format(date_str)
    out_to_oui_path = project_path + "/resources/{0}/out_to_oui.txt".format(date_str)
    out_to_allmac_path = project_path + "/resources/{0}/out_to_allmac.txt".format(date_str)
    out_to_allmacX_path = project_path + "/resources/{0}/out_to_allmacX.txt".format(date_str)
    out_to_oui = []
    out_to_allmac = []
    out_to_allmacX = []
    origin_data = read_txt_all(origin_data_path)
    n = 1
    get_repeat_vendor(origin_data)
    for line in origin_data:
        line = line.strip().strip("\n")
        line = re.sub('\t+', '\t', line)
        mac_adds_id = ""
        vendor_name = ""
        n += 1
        if len(line) == 0:
            continue
        if line.startswith("#"):
            continue
        data = line.split("\t")
        if len(data) == 2:
            mac_adds_id = data[0].replace('-', ':')
            vendor_name = data[1]
        elif len(data) > 2:
            mac_adds_id = data[0].replace('-', ':')
            vendor_name_all = data[2].strip().replace("#", "")
            if vendor_name_all in origin_new:
                vendor_name = origin_new[vendor_name_all]
            else:
                vendor_name = data[1]
            if len(vendor_name) < 3:
                # print(vendor_name, data)
                vendor_name = data[2]
        else:
            print("2异常的mac地址", line)
        # if mac_adds_id == "00:50:C2:46:20:00/36":
        #     print(data)
        vendor_name = clean_vendor_name(vendor_name)
        if len(vendor_name) == 0:
            print(vendor_name)
        if len(mac_adds_id) == 20 or "/" in mac_adds_id:
            # print(vendor_name)
            out_to_allmacX.append(mac_adds_id + "^" + vendor_name)
        elif len(mac_adds_id) == 17:
            out_to_allmac.append(mac_adds_id + "^" + vendor_name)
        elif len(mac_adds_id) == 8:
            out_to_oui.append(mac_adds_id + "^" + vendor_name)
        else:
            print("3异常的mac地址：", line)
    delete_existed_file(out_to_oui_path)
    delete_existed_file(out_to_allmac_path)
    delete_existed_file(out_to_allmacX_path)
    save_to_datas_file(out_to_oui, out_to_oui_path)
    save_to_datas_file(out_to_allmac, out_to_allmac_path)
    save_to_datas_file(out_to_allmacX, out_to_allmacX_path)


if __name__ == "__main__":
    # get_repeat_vendor()
    # date = '20191029'
    split_mac_data(date_now)
    # cp_oui_common(date)
