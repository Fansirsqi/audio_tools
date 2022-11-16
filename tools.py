# _*_coding:utf-8_*_
import os
import subprocess

import ffmpeg
from pydub import AudioSegment


# @PROJECT : audio_tools
# @Time : 2022/11/10 18:56
# @Author : Byseven
# @File : tools.py
# @SoftWare: Tools_package


# 遍历返回子文件
def get_filelist(path: str) -> list:
    file_list = []
    for home, dirs, files in os.walk(path):
        for filename in files:
            # 文件名列表，包含完整路径
            file_list.append(os.path.join(home, filename))
            # # 文件名列表，只包含文件名
            # Filelist.append( filename)
    return file_list


# 参数1：音频路径， 参数2：转换后的格式
def trans_any_audio_types(filepath, input_audio_type, output_audio_type) -> any:
    """
    将任意音频文件格式转化为任意音频文件格式
    Args:
        filepath (str): 文件路径
        input_audio_type(str): 输入音频文件格式
        output_audio_type(str): 输出音频文件格式
    """
    song = AudioSegment.from_file(filepath, input_audio_type)
    filename = filepath.split(".")[0]
    song.export(f"{filename}.{output_audio_type}", format=f"{output_audio_type}")


# 获取音视频格式信息
def get_av_media_format_info(file_path: str) -> str:
    info = ffmpeg.probe(file_path)
    return info['format']['format_name']


# 获取图片格式
def get_im_media_format_info(file_path: str) -> any:
    info = ffmpeg.probe(file_path)
    i = info['format']['format_name']
    rs = i.split("_")
    return rs[0]


# 获取文件名，文件名后缀
def get_name_info(file_path: str) -> any:
    if os.path.isfile(file_path):
        file_name = file_path.split('\\').pop()
        file_name_last = file_name.split('.').pop()
    else:
        return '！！ERROR！！传入的路径并不是文件路径！！'
    return [file_name, file_name_last]


def set_name_info(file_path: str) -> list:
    file_name = file_path.split('\\').pop()
    file_name_last = file_name.split('.').pop()
    return [file_name, file_name_last]


def b_rename(old_path: str, new_path: str):
    on, onl = set_name_info(old_path)
    n, nl = set_name_info(new_path)
    if os.path.exists(new_path):
        print(f'{n}已存在， 无法重命名')
    else:
        try:
            os.rename(old_path, new_path)
            print(f'{on}已重命名为{n}')
        except IOError as e:
            print(e, ' 重命名失败')


# 实时打印cmd_log
def run_cmd(commend) -> any:
    proc = subprocess.Popen(commend, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, encoding='utf-8')
    print(proc.stdout.read())
    proc.stdout.close()

