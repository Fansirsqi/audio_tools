# _*_coding:utf-8_*_
import json

# @PROJECT : audio_tools
# @Time : 2022/11/10 18:56
# @Author : Byseven
# @File : tools.py
# @SoftWare:

from pydub import AudioSegment
import ffmpeg


# 参数1：音频路径， 参数2：转换后的格式
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


def get_media_format_info(file_path: str):
    info = ffmpeg.probe(file_path)
    return info['format']['format_name']

# print(get_media_format_info(r'C:\Users\BYSEVEN\Desktop\Naruto\NarutoSenki\assets\Audio\Hiruzen\Hiruzen_dead.mp3'))