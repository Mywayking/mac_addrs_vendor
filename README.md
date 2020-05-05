## mac地址解析出对应厂商
解析wireshark整理结果，制成所需文件。保证第二列简写的唯一性，先找出重复名称，然后取全称第一二单词组合成新名称。


### 工作流程
- 获取原始数据`curl https://code.wireshark.org/review/gitweb\?p\=wireshark.git\;a\=blob_plain\;f\=manuf\;hb\=HEAD -o wireshark.txt`
- 在原始数据中添加`resources/wireshark_not_in_list.txt`.
- 清洗数据。`mac_addr_split.py`
- 删除common包原有数据.`rm -rf /Users/wangchun/IdeaProjects/common/src/main/resources/macAddrs/out_*` 
- 将数据存入common包.`cp /Users/wangchun/PycharmProjects/mac_addrs_vendor/resources/20180413/ /Users/wangchun/IdeaProjects/common/src/main/resources/macAddrs/out_*` 


**mac地址原始资源：**
- 原始文件 `resources/terry_origin_20161215`,`oui.ieee.org`是最原始的资源,wireshark是整理后的文件。`mam.txt oui.txt oui36.txt`三个文件生成`OUI-wireshark.txt`.
- [根本文件1](http://standards-oui.ieee.org/oui36/oui36.txt)
- [根本文件2](http://standards-oui.ieee.org/oui.txt)
- [根据文件1、2整理结果](https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf)wireshark_not_in_list.txt要添加到下载文件末尾.
- https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf 变更为 https://gitlab.com/wireshark/wireshark/raw/master/manuf



## 部署
- 位置： /home/galen/mac_addrs_vendor`
- 运行：`sh download.sh`
- 存放：`/home/galen/mac_addrs_vendor/resources/latest`
- 运维会拉取到指定目录
- 更新频率：每周一次。周三6点
    - `37 15 * * 2 cd /home/galen/mac_addrs_vendor && source ~/.bash_profile && sh download.sh >/home/galen/mac_addrs_vendor/mac_addrs_vendor.log`
