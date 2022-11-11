# _*_coding:utf-8_*_

# @PROJECT : audio_tools
# @Time : 2022/11/10 18:56
# @Author : Byseven
# @File : tools.py
# @SoftWare:

from pydub import AudioSegment

import main


def trans_any_audio_types(filepath, input_audio_type, output_audio_type):
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


# 参数1：音频路径， 参数2：转换后的格式


file_list = main.get_filelist(main.path)
for i in file_list:
    trans_any_audio_types(i, "ogg", "mp3")
