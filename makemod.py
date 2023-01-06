# _*_coding:utf-8_*_
import sys

# @PROJECT : audio_tools
# @Time : 2022/11/28 11:20
# @Author : Byseven
# @File : makemod.py
# @SoftWare:

from main import *

if __name__ == "__main__":
    path = sys.argv[1]
    # print('开始纠正音频文件')
    # fix_av_format(path)
    # print('开始转换音频文件至mp3')
    # audio_conversion(path, 'mp3')
    # xml_ls = get_hz_file(path, 'xml')
    bak_ls = get_hz_file(path, 'bak')
    # print('开始批量修改xml内ogg')
    # to_xml(xml_ls)
    print('开始删除备份bak')
    del_list_file(bak_ls)