#!/usr/bin/env bash
PROJECT_DIR="/home/galen/mac_addrs_vendor"
cd ${PROJECT_DIR}

date_now=`date +%Y%m%d`
echo ${date_now}

echo "loading wireshark"
# 老板地址变更了
#curl https://code.wireshark.org/review/gitweb\?p\=wireshark.git\;a\=blob_plain\;f\=manuf\;hb\=HEAD -o wireshark.txt
curl https://gitlab.com/wireshark/wireshark/raw/master/manuf -o wireshark.txt
if [[ ! -d "./resources/"${date_now} ]]; then
  mkdir ./resources/${date_now}
fi
echo "move wireshark"
# 移动文件
mv wireshark.txt resources/${date_now}
python mac_addr_split.py -d ${date_now}

cp ./resources/out_to_allmac.txt ./resources/${date_now}/out_to_allmac.txt

echo "generate latest step 1"
# 生成 latest
if [[ ! -d "./resources/latest" ]]; then
  mkdir ./resources/latest
fi
# 移动文件到 latest
mv ./resources/${date_now}/out* ./resources/latest

echo "generate latest  step 2"
# 生成
cp ./resources/latest/out_to_allmac.txt ./resources/latest/out_to_allmac_${date_now}.txt
cp ./resources/latest/out_to_oui.txt ./resources/latest/out_to_oui_${date_now}.txt
cp ./resources/latest/out_to_allmacX.txt ./resources/latest/out_to_allmacX_${date_now}.txt
# 生成 latest
mv ./resources/latest/out_to_allmac.txt ./resources/latest/out_to_allmac_latest.txt
mv ./resources/latest/out_to_oui.txt ./resources/latest/out_to_oui_latest.txt
mv ./resources/latest/out_to_allmacX.txt ./resources/latest/out_to_allmacX_latest.txt
# sh download.sh
# nohup sh download.sh >nohup.log 2>&1 &