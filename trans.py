# _*_coding:utf-8_*_
import os
import plistlib

from pathlib import Path


# @PROJECT : audio_tools
# @Time : 2023/1/6 19:29
# @Author : Byseven
# @File : trans.py
# @SoftWare:

def get_file_select(path, _format):
    """
    :param path:文件夹路径
    :param _format: 需要筛选的文件名后缀
    :return:
    """
    file_list = []
    n_f = []
    for home, dirs, files in os.walk(path):
        for filename in files:
            # 文件名列表，包含完整路径
            file_list.append(os.path.join(home, filename))
            # # 文件名列表，只包含文件名
            # Filelist.append( filename)
    for i in file_list:
        last_name = i.split('.').pop()
        if last_name == _format:
            n_f.append(i)
    return n_f


# 获取 frame 参数
def get_framev2(frame):
    base_result = {'rotated': frame['textureRotated'],
                   'xy': frame['textureRect'].replace('}', '').replace('{', '').split(','),
                   'size': frame['spriteSize'].replace('}', '').replace('{', '').replace(',', ', '),
                   'orig': frame['spriteSourceSize'].replace('}', '').replace('{', '').replace(',', ', '),
                   'offset': frame['spriteOffset'].replace('}', '').replace('{', '').replace(',', ', ')}
    return base_result


def plist_to_atlas(file_path):
    plist_conf = Path(file_path)
    if not os.path.exists(plist_conf):
        print("plist文件不存在！")
    else:
        print("读取plist..")
    print(file_path)
    file_name = file_path.replace('plist', 'atlas')
    print(file_name)

    # if os.path.exists(file_name):
    #     print('不存在-创建')
    #     with open(file_name, mode='r', encoding='utf-8') as ff:
    #         print(ff.readlines())
    # else:
    #     with open(file_name, mode='w', encoding='utf-8') as ff:
    #         print("文件创建成功！")

    # file_name = (file_path.split('\\').pop().split('.')[0])
    pl = plistlib.load(open(plist_conf, 'rb'))
    # 写入文件头部
    info = pl['metadata']
    print(info)
    data = ['textureFileName', 'size', 'pixelFormat']
    for key in data:
        if key not in info.keys():
            if key == 'pixelFormat':
                key = 'format'
                print(f"{key}在此plist中未定义,请手动修正")
            write_data = f'{key}: 未定义值，待修正'
            with open(f'{file_name}', mode='a', encoding='utf-8') as file:
                file.write(f"{write_data}\n")
        else:
            if key == 'size':
                write_data = f"{key}: {info[key].replace('}', '').replace('{', '')}"
            elif key == 'textureFileName':
                write_data = f'{info[key]}'
            else:
                write_data = f'{key}: {info[key]}'
            with open(f'{file_name}', mode='a', encoding='utf-8') as file:
                file.write(f"{write_data}\n")
    _filter = 'filter: Linear,Linear\n'
    img_repeat = 'repeat: none\n'
    with open(f'{file_name}', mode='a', encoding='utf-8') as file:
        file.write(f"{_filter}")
        file.write(f"{img_repeat}")
    # 处理文件主体
    frames = pl['frames']
    result = {}
    for key in frames:
        item = get_framev2(frames[key])
        result[key] = item
        key_name = key.split('.')[0]
        rotate = str(item['rotated']).lower()
        xy = item['xy']
        size = item['size']
        orig = item['orig']
        offset = item['offset']
        ind = '  index: -1'
        with open(f'{file_name}', mode='a', encoding='utf-8') as file:
            file.write(f"{key_name}\n")
            file.write(f"  rotate: {rotate}\n")
            file.write(f"  xy: {xy[0]}, {xy[1]}\n")
            file.write(f"  size: {size}\n")
            file.write(f"  orig: {orig}\n")
            file.write(f"  offset: {offset}\n")
            file.write(f"{ind}\n")
    print('写入完成')


def p_plist_to(path):
    pls = get_file_select(path, 'plist')
    for i in pls:
        print(i)
        plist_to_atlas(i)


# if __name__ == '__main__':
#     p_plist_to(r'.\ts')
