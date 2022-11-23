# _*_coding:utf-8_*_

# @PROJECT : audio_tools
# @Time : 2022/11/10 18:41
# @Author : Byseven
# @File : main.py
# @SoftWare:
import sys

import tools
from xmltool import *


def fix_av_format(file_path: str):
    del_count = 0
    rename_count = 0
    file_list = tools.get_filelist(file_path)
    print('修正前------------------------------')
    for old_file_path_list_item in file_list:
        #  old_file_path_list_item 子目录完整路径
        # print(old_file_path_list_item)  # 输出未修正前的文件名列表
        format_info = tools.get_av_media_format_info(old_file_path_list_item)
        file_name = old_file_path_list_item.split('\\').pop()
        file_name_last = file_name[-1:-4:-1][::-1]
        if file_name_last != format_info:
            print(f'{file_name} 文件名后缀：{file_name_last}, 实际格式：{format_info}')
            new_file_path_list_item = old_file_path_list_item.replace(file_name_last, format_info)
            new_file_name = new_file_path_list_item.split('\\').pop()
            if os.path.exists(new_file_path_list_item):  # 如果新文件已经存在，则取消重命名，直接删除源文件,无需做转换处理
                os.remove(old_file_path_list_item)
                print(f'已存在{new_file_name}故,删除{file_name}')
                del_count += 1
            else:  # 否则就修正该文件的后缀
                os.rename(old_file_path_list_item, new_file_path_list_item)
                print(old_file_path_list_item, new_file_name)
                rename_count += 1
                new_file_name_last = new_file_name[-1:-4:-1][::-1]
                print(f'新文件名后缀{new_file_name_last}')
                print(f'修正文件名{file_name} -------> {new_file_name_last}')
    file_lis_new = tools.get_filelist(file_path)
    print('修正后------------------------------')
    for new_file_path_list_item in file_lis_new:
        print(new_file_path_list_item)
    print(f'-本次整理删除{del_count}个文件，重命名{rename_count}个文件-')


# im fix
def fix_im_forma(file_path: str):
    rename_count = 0
    other_res_ls = []
    file_list = tools.get_filelist(file_path)
    for old_file_path in file_list:
        old_file = tools.set_name_info(old_file_path)
        # print(f'读取到的文件名{old_file[0]},后缀{old_file[1]}')
        # 需要特殊处理，过滤掉plist,xml文件
        if old_file[1] not in ['xml', 'plist', 'ccz']:
            img_format_info = tools.get_im_media_format_info(old_file_path)
            new_file_path = old_file_path.replace(old_file[1], img_format_info)
            # new_file = tools.set_name_info(new_file_path)
            tools.b_rename(old_file_path, new_file_path)
            rename_count += 1
        else:
            other_res_ls.append(old_file[0])
    print(f'\n以下文件为非图像资源，本次不做处理\n---------------')
    for i in other_res_ls:
        print(i)
    print(f'---------------')
    return print(f'累计重命名{rename_count}个文件')


# 音频转换
def audio_conversion(file_path, set_format):  # 路径，格式
    file_list = tools.get_filelist(file_path)
    count = 0
    del_count = 0
    file_name_ls = []
    del_ls = []
    for old_file_path in file_list:
        # print(old_file_path)
        format_info = tools.get_av_media_format_info(old_file_path)  # 原格式
        if format_info != set_format:
            old_file = tools.set_name_info(old_file_path)
            new_file_path = old_file_path.replace(old_file[1], set_format)
            new_file = tools.set_name_info(new_file_path)
            # 判断欲转换文件是否已经存在，存在则删掉与他同名源文件,不存在，则执行转换，再删除
            if os.path.exists(new_file_path):
                print(f'{new_file[0]}已存在，删除源{old_file[0]}文件，不作转换')
                try:
                    os.remove(old_file_path)
                    del_ls.append(new_file[0])
                    del_count += 1
                except IOError as e:
                    print(e)
                    print(f'删除源{old_file[0]}文件出错')
            else:
                # 执行转换
                tools.trans_any_audio_types(old_file_path, format_info, set_format)
                file_name_ls.append(old_file[0])
                count += 1
                print(f'转换 {old_file[0]} to {new_file[0]} 完成，删除源{old_file[0]}文件')
                try:
                    os.remove(old_file_path)
                    del_ls.append(new_file[0])
                    del_count += 1
                except IOError as e:
                    print(e)
                    print(f'删除源{old_file[0]}文件出错')

    print(f'本次转换音频{count}个\n删除源文件{del_count}个')
    # for i in file_name_ls:
    #     print(i)


def image_conversion(file_path, set_format):
    file_list = tools.get_filelist(file_path)
    count = 0
    del_count = 0
    file_name_ls = []
    del_ls = []
    for old_file_path in file_list:
        old_file = tools.set_name_info(old_file_path)
        # 需要特殊处理，过滤掉plist,xml文件
        if old_file[1] not in ['xml', 'plist', 'ccz', 'png']:
            format_info = tools.get_im_media_format_info(old_file_path)  # 原格式
            if format_info != set_format:
                new_file_path = old_file_path.replace(old_file[1], set_format)
                new_file = tools.set_name_info(new_file_path)
                # 判断欲转换文件是否已经存在，存在则删掉与他同名源文件,不存在，则执行转换，再删除
                if os.path.exists(new_file_path):
                    print(f'{new_file[0]}存在，删除源{old_file[0]}文件，不作转换')
                    try:
                        os.remove(old_file_path)
                        del_ls.append(new_file[0])
                        del_count += 1
                    except IOError as e:
                        print(e)
                        print(f'删除源{old_file[0]}文件出错')
                else:  # 执行转换
                    try:
                        tools.run_cmd(f'ffmpeg -i {old_file_path} {new_file_path}')
                        print(f'转换 {old_file[0]} ------> {new_file[0]}')
                        if os.path.exists(new_file_path):
                            print(f'{new_file[0]}存在，删除源{old_file[0]}文件，不作转换')
                            try:
                                os.remove(old_file_path)
                                del_ls.append(new_file[0])
                                del_count += 1
                            except IOError as e:
                                print(e)
                                print(f'删除源{old_file[0]}文件出错')
                    except IOError as e:
                        print('转换错误！', e)


def to_xml(xml_path):
    for item in xml_path:
        update_file(item, 'ogg', 'mp3')
        update_file(item, 'wav', 'mp3')


# 删除列表文件
def del_list_file(ls: list):
    for i in ls:
        try:
            os.remove(i)
        except IOError as e:
            print(e)
            print("删除错误")


if __name__ == "__main__":
    select = sys.argv[1]
    path = sys.argv[2]
    if select == 'fixaudio':
        fix_av_format(path)
    elif select == 'fiximage':
        fix_im_forma(path)
    elif select == 'audio':
        for_mat = input("请输入欲转换的音频格式：eg 'mp3' ")
        audio_conversion(path, for_mat)
    elif select == 'image':
        image_conversion(path, "png")
    elif select == 'xml':
        xml_ls = get_hz_file(path, 'xml')
        bak_ls = get_hz_file(path, 'bak')
        to_xml(xml_ls)
        del_list_file(bak_ls)
    # path = r'D:\xxxx\assets\Element'
    # fix_im_forma(path)
    # 将一些不知名格式图片转换成png 有删除源文件风险
    # image_conversion(path, "png")
