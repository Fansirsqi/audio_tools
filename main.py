# _*_coding:utf-8_*_

# @PROJECT : audio_tools
# @Time : 2022/11/10 18:41
# @Author : Byseven
# @File : main.py
# @SoftWare:
import os

path = r'C:\Users\admin\Desktop\naruto\assets\Audio'


def get_filelist(dir):
    Filelist = []

    for home, dirs, files in os.walk(path):

        for filename in files:
            # 文件名列表，包含完整路径

            Filelist.append(os.path.join(home, filename))

            # # 文件名列表，只包含文件名

            # Filelist.append( filename)

    return Filelist


if __name__ == "__main__":

    Filelist = get_filelist(dir)

    print(type(Filelist))

    for file in Filelist:
        print(file)
