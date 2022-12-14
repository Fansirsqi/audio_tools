# _*_coding:utf-8_*_

# @PROJECT : audio_tools
# @Time : 2022/11/10 18:41
# @Author : Byseven
# @File : main.py
# @SoftWare:
import sys

import trans
from xmltool import *


def fix_av_format(file_path: str):
    del_count = 0
    rename_count = 0
    file_list = tools.get_filelist(file_path)
    fix_li = []
    print('修正前------------------------------')
    for old_file_path in file_list:
        #  old_file_path 子目录完整路径
        # print(old_file_path)  # 输出未修正前的文件名列表
        format_info = tools.get_av_media_format_info(old_file_path)
        old_file = tools.set_name_info(old_file_path)
        print(old_file[0])
        if old_file[1] != format_info:
            log_1 = f'{old_file[0]} 文件名后缀：{old_file[1]}, 与实际格式：{format_info}不符合！！'
            tools.set_log('fix_audio', log_1)
            new_file_path = old_file_path.replace(old_file[1], format_info)
            new_file = tools.set_name_info(new_file_path)
            if os.path.exists(new_file_path):  # 如果新文件已经存在，则取消重命名，直接删除源文件,无需做转换处理
                os.remove(old_file_path)
                logs = f'已存在{new_file[1]}故,删除{old_file[1]}'
                tools.set_log('fix_audio', logs)
                del_count += 1
            else:  # 目标文件不存在，则就修正该文件的后缀
                tools.b_rename(old_file_path, new_file_path)
                logs = f'rename {old_file[0]} to {new_file[0]}'
                tools.set_log('fix_audio', logs)
                rename_count += 1
                fix_li.append(f'{old_file[0]}------>{new_file[0]}')

    file_lis_new = tools.get_filelist(file_path)
    print('修正后------------------------------')
    for new_file_path in file_lis_new:
        nfn = tools.set_name_info(new_file_path)
        print(nfn[0])
    print('修正列表------------------------------')
    for lg in fix_li:
        print(lg)
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
        # print(f'源格式-》{format_info}')
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
                print(f'参数1{old_file_path}\n'
                      f'参数2{format_info}\n'
                      f'参数3{set_format}\n'
                      f'删除的是{old_file_path}')
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


# 图像转换
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
    elif select == 'pltoat':
        trans.p_plist_to(path)
    # path = r'D:\xxxx\assets\Element'
    # fix_im_forma(path)
    # 将一些不知名格式图片转换成png 有删除源文件风险
    # image_conversion(path, "png")
