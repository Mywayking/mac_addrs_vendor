import re
from radix_exchange import macaddrs2bin


def mac(addr):
    """
    Validates a mac address
    """
    valid = re.compile(r'''
                      (^([0-9A-F]{1,2}[-]){5}([0-9A-F]{1,2})$
                      |^([0-9A-F]{1,2}[:]){5}([0-9A-F]{1,2})$
                      |^([0-9A-F]{1,2}[.]){5}([0-9A-F]{1,2})$
                      |^([0-9A-F]{1,2}[\s]){5}([0-9A-F]{1,2})$
                      |^([0-9A-F]{1,2}){5}([0-9A-F]{1,2})$)
                      ''',
                       re.VERBOSE | re.IGNORECASE)
    return valid.match(addr) is not None


def format_MacAddrs(MacAddrs):
    # 格式化字符串
    if ':' in MacAddrs:
        MacAd = MacAddrs
    elif '.' in MacAddrs:
        MacAd = MacAddrs.replace('.', ':')
    elif ' ' in MacAddrs:
        MacAd = MacAddrs.replace(' ', ':')
    else:
        MacAd = MacAddrs[0:2] + ':' + MacAddrs[2:4] + ':' + MacAddrs[4:6] + \
                ':' + MacAddrs[6:8] + ':' + MacAddrs[8:10] + ':' + MacAddrs[10:12]
    return MacAd


def ouiMacaddrs_test(MacAddrs):
    filename = 'out_to_oui.txt'
    MacAddrs = MacAddrs[0:len(MacAddrs) / 2]
    oui_name = ''
    with open(filename, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()  # 整行读取数据
            if not lines:
                break
                pass
            datas_str = lines.strip().split('^')
            if datas_str[0] == MacAddrs:
                oui_name = datas_str[1]
                break
    return oui_name


def full_ouiMacaddrs_test(MacAddrs):
    filename = 'out_to_allmac.txt'
    oui_name = ''
    with open(filename, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()  # 整行读取数据
            if not lines:
                break
                pass
            datas_str = lines.strip().split('^')
            if datas_str[0] == MacAddrs:
                oui_name = datas_str[1]
                break
    return oui_name


def full_ouiMacaddrs_test_x(MacAddrs):
    filename = 'out_to_allmacX.txt'
    oui_name = ''
    with open(filename, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()  # 整行读取数据
            if not lines:
                break
                pass
            datas_str = lines.strip().split('^')
            data_str = datas_str[0].strip().split('/')
            step_Macaddrs = int(data_str[1])
            if step_Macaddrs % 4 == 0:
                MacAddrs_org = data_str[0].replace(':', '')[0:step_Macaddrs / 4]
                MacAddrs_put = MacAddrs.replace(':', '')[0:step_Macaddrs / 4]
                if MacAddrs_org == MacAddrs_put:
                    oui_name = datas_str[1]
                    break
            else:
                MacAddrs_org = macaddrs2bin(data_str[0])[0:step_Macaddrs]
                MacAddrs_put = macaddrs2bin(MacAddrs)[0:step_Macaddrs]
                if MacAddrs_org == MacAddrs_put:
                    oui_name = datas_str[1]
                    break
    return oui_name


def check_mac_addrs(MacAddrs):
    # 匹配mac地址
    test01 = full_ouiMacaddrs_test_x(MacAddrs)
    if test01 is '':
        test02 = full_ouiMacaddrs_test(MacAddrs)
        if test02 is '':
            test03 = ouiMacaddrs_test(MacAddrs)
            if test03 is '':
                print
                "没有匹配的Mac地址"
            else:
                return test03
        else:
            return test02
    else:
        return test01
        # return oui_names


def main():
    # MacAddrs = '28:cf:e9:20:bf:9f'
    # MacAddrs ='c8:3a:35:17:92:40'
    MacAddrs = '34:ce:00:07:b8:3a'
    # MacAddrs = 'b8:55:10:04:f3:d7'

    print
    MacAddrs
    MacAddrs = MacAddrs.upper()
    print
    MacAddrs
    if mac(MacAddrs):
        MacAddrs = format_MacAddrs(MacAddrs)
        print
        check_mac_addrs(MacAddrs)
    else:
        print
        "输入错误，请输入形如'00:00:04:00:A0:00'或者'00-00-04-00-A0-00'格式的mac地址"


if __name__ == "__main__":
    # 获取mac字符

    main()
    # full_ouiMacaddrs_test_x('5C:F2:86:E0:00:00')
    # full_ouiMacaddrs_test_x('01:80:C2:00:00:38')

    # MacAddrs = 'FF:FF:01:E0:00:04'
    # MacAddrs = '5C F8 A1 FF AA FF'
    # MacAddrs = 'AAFFAAFFAAFF'
    # MacAddrs = '5C:F2:86:E0:00:00'

    # MacAddrs = MacAddrs.upper()
    # print MacAddrs
    # if mac(MacAddrs):
    #     # get_mac_address(MacAddrs)
    #     MacAddrs = format_MacAddrs(MacAddrs)
    #     chack_MacAddrs(MacAddrs)
    # print MacAddrs.replace('.',':')
    # mac =EUI(MacAddrs)
    # print mac
    # MacAd=MacAddrs.replace('-','')
    # print MacAd,len(MacAd)
