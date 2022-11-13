# _*_coding:utf-8_*_

# @PROJECT : audio_tools
# @Time : 2022/11/10 18:41
# @Author : Byseven
# @File : main.py
# @SoftWare:
import os
import tools
import xmltool


def get_filelist(path: str) -> list:
    file_list = []

    for home, dirs, files in os.walk(path):

        for filename in files:
            # 文件名列表，包含完整路径
            file_list.append(os.path.join(home, filename))
            # # 文件名列表，只包含文件名
            # Filelist.append( filename)
    return file_list


def fix_format(file_path: str):
    del_count = 0
    rename_count = 0
    file_list = get_filelist(file_path)
    print('修正前------------------------------')
    for old_file_path_list_item in file_list:
        #  old_file_path_list_item 子目录完整路径
        # print(old_file_path_list_item)  # 输出未修正前的文件名列表
        format_info = tools.get_media_format_info(old_file_path_list_item)
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
    file_lis_new = get_filelist(file_path)
    print('修正后------------------------------')
    for new_file_path_list_item in file_lis_new:
        print(new_file_path_list_item)
    print(f'-本次整理删除{del_count}个文件，重命名{rename_count}个文件-')


# 音频转换
def audio_conversion(file_path: str, format):
    file_list = get_filelist(file_path)
    count = 0
    del_count = 0
    file_name_ls = []
    del_ls = []
    for old_file_name_all_path in file_list:
        # print(old_file_name_all_path)
        format_info = tools.get_media_format_info(old_file_name_all_path)
        if format_info != format:
            old_file_name = old_file_name_all_path.split('\\').pop()

            old_file_name_last = old_file_name[-1:-4:-1][::-1]
            new_file_name_all_path = old_file_name_all_path.replace(old_file_name_last, format)
            new_file_name = new_file_name_all_path.split('\\').pop()
            # 判断MP3是否已经存在，存在则删掉与他同名ogg,不存在，则执行转换，再删除
            if os.path.exists(new_file_name_all_path):
                print(f'{new_file_name}已存在，删除源ogg文件，不作转换')
                try:
                    os.remove(old_file_name_all_path)
                    del_ls.append(new_file_name)
                    del_count += 1
                except IOError as e:
                    print(e)
                    print('删除源ogg文件出错')
            else:
                # 执行转换
                tools.trans_any_audio_types(old_file_name_all_path, format_info, format)
                file_name_ls.append(old_file_name)
                count += 1
                print(f'转换 {old_file_name} to {new_file_name} 完成，删除源{old_file_name}文件')
                try:
                    os.remove(old_file_name_all_path)
                    del_ls.append(new_file_name)
                    del_count += 1
                except IOError as e:
                    print(e)
                    print('删除源ogg文件出错')

    print(f'本次转换音频{count}个\n删除ogg文件{del_count}个')
    # for i in file_name_ls:
    #     print(i)


def to_xml(pathxml):
    for item in pathxml:
        xmltool.update_file(item, 'ogg', 'mp3')


if __name__ == "__main__":
    # path = r'C:\Users\BYSEVEN\Desktop\Naruto\NarutoSenki\assets\Audio'
    # print('开始修复格式以及文件名')
    # fix_format(path)
    # print('开始转换')
    # audio_conversion(path, "mp3")
    # pathxml = xmltool.get_xml_file(r'C:\Users\BYSEVEN\Desktop\Naruto\NarutoSenki\assets\Element', 'xml')
    pathbak = xmltool.get_xml_file(r'C:\Users\BYSEVEN\Desktop\Naruto\NarutoSenki\assets\Element', 'bak')
    # print('开始重构')
    # to_xml(pathxml)
    print('开始删除')
    xmltool.del_file(pathbak)
