# _*_coding:utf-8_*_

# @PROJECT : audio_tools
# @Time : 2022/11/10 18:41
# @Author : Byseven
# @File : main.py
# @SoftWare:
import os
import tools


def get_filelist(path: str) -> list:
    file_list = []

    for home, dirs, files in os.walk(path):

        for filename in files:
            # 文件名列表，包含完整路径

            file_list.append(os.path.join(home, filename))

            # # 文件名列表，只包含文件名

            # Filelist.append( filename)

    return file_list


if __name__ == "__main__":
    path = r'C:\Users\BYSEVEN\Desktop\Naruto\NarutoSenki\assets\Audio'
    # path2 = r'C:\Users\BYSEVEN\Desktop\Naruto\NarutoSenki\assets\Audio\Effect'
    # path = 'ts'
    file_list = get_filelist(path)
    # file_list2 = get_filelist(path2)
    # print(len(file_list), len(file_list2))

    for i in file_list:
        format_info = tools.get_media_format_info(i)
        file_name = i.split('\\').pop()
        file_name_last = file_name[-1:-4:-1][::-1]

        # print(i, i[-1:-4:-1][::-1], format_info)
        # if i[-1:-4:-1][::-1] == 'ogg':
        # print(len(i[-1:-4:-1][::-1]), len(format_info))
        if file_name_last != format_info:
            print(f'文件名后缀：{file_name_last},实际格式：{format_info}')
            new_file_name = i.replace(file_name_last, format_info)
            # print(i, new_file_name)
            os.rename(i, new_file_name)
            new_file_name_last = new_file_name.split('\\').pop()
            print(f'修正文件名{file_name}_to_{new_file_name_last}')
        if format_info == 'ogg':
            print(f'转换{new_file_name_last}')
            tools.trans_any_audio_types(new_file_name, "ogg", "mp3")
