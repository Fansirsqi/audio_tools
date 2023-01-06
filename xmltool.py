import os
import re
import xml
import xml.dom.minidom

import tools
from tools import get_filelist


# 使用正则表达式替换文件内容
def update_file(file, old_srt, new_str):
    new_file = '%s.bak' % file
    with open(file, 'r', encoding='utf-8') as f1, open(new_file, 'w', encoding='utf-8') as f2:
        for line in f1:
            f2.write(re.sub(old_srt, new_str, line))
    # 互换文件名称
    print(file, new_file)
    os.rename(file, "%s.abak" % file)
    print(file)
    os.rename(new_file, file)
    os.rename("%s.abak" % file, "%s.bak" % file)


# 检索后缀为 hz 的文件
def get_hz_file(Element_path, hz):
    ls = get_filelist(Element_path)
    xml_ls = []
    for i in ls:
        last_name = i[-1:-4:-1][::-1]
        if last_name == hz:
            if 'md5' not in i:
                xml_ls.append(i)
    return xml_ls


def del_file(ls: list):
    for i in ls:
        try:
            os.remove(i)
        except IOError as e:
            print(e)
            print("删除错误")


def find_code(file_path):
    Sounds = r'Sound">(.*?)</'
    Mons = r'setMon">(.*?)</'
    Bulls = r'setBullet">(.*?)</'
    path_ls = get_hz_file(file_path, 'xml')
    print('++++++')
    for p in path_ls:
        file_name = p.split("\\").pop()
        print(f'文件名:{file_name}')
        with open(p, 'r', encoding='utf-8') as f:
            res = f.read()
        Sounds_ls = re.findall(Sounds, res, re.S)
        print(Sounds_ls)
        Mons_ls = re.findall(Mons, res, re.S)
        Bulls_ls = re.findall(Bulls, res, re.S)
        print('-------声音资源-------')
        for i in Sounds_ls:
            print(i)
        print('-------通灵-------')
        for j in Mons_ls:
            print(j)
        print('-------飞行物-------')
        for k in Bulls_ls:
            print(k)


def clen_mod_sounds(xml_path, audio_path):
    Sounds = r'Sound">(.*?)</'
    path_ls = get_hz_file(xml_path, 'xml')
    for file_name_path in path_ls:

        file_name = file_name_path.split("\\").pop()
        with open(file_name_path, 'r', encoding='utf-8') as f:
            res = f.read()
        # xml中引用的声音列表
        Sounds_ls = re.findall(Sounds, res, re.S)
        x_l = []
        for yin in Sounds_ls:
            y = yin.split('/').pop().split('.')[0]
            x_l.append(y)
        true_sounds_ls = get_filelist(audio_path)
        # audio文件夹
        t_l = []
        for t in true_sounds_ls:
            yt = t.split('\\').pop().split('.')[0]
            t_l.append(yt)

        print(f'----------文件名:{file_name}')
        for check in x_l:
            if check not in t_l:
                print(f'{check} 在资源中不存在')
        for rechack in t_l:
            if rechack not  in x_l:
                print(f'{rechack} 未曾使用')
        # print(f'{x_l}')
        # print(f'{t_l}')




        # if y in x_l:
        #     pass
        #     # print(f'存在{y}')
        # else:
        #     pass
        # print(f"不存在{y}")
    # print(x_l)
    # print(t_l)
    # print(f'实际：{ture_sounds_ls}')
    # print(f'引用：{Sounds_ls}')


# 转换xml至117
def to_old(f, ):
    update_file(f, '<unit>', ' <animation>')
    update_file(f, 'type="cd', 'type="coldDown')
    update_file(f, '<data>', '<date>')
    update_file(f, '</data>', '</date>')
    update_file(f, '<p type', '<dateName type')
    update_file(f, '</p>', '</dateName>')
    update_file(f, '<f>', '<frameName>')
    update_file(f, '</f>', '</frameName>')
    update_file(f, '<e type', '<eventName type')
    update_file(f, '</e>', '</eventName>')
    update_file(f, '</unit>', '</animation>')


# 格式化代码，但是很拉
def pretty_xml(file):
    new_file = '%s.bak' % file
    with open(file, 'r', encoding='utf-8') as f1, open(new_file, 'w', encoding='utf-8') as f2:
        ugly_xml = f1.read()
        xml_c = xml.dom.minidom.parseString(ugly_xml)
        xml_pretty_str = xml_c.toprettyxml()
        f2.write(xml_pretty_str)
    os.remove(file)
    os.rename(new_file, file)


if __name__ == '__main__':
    # update_file('ts/ts.xml', 'ogg', 'mp3')
    # pass
    # (r'C:\Users\BYSEVEN\Desktop\Naruto\NarutoSenki\assets\Element', 'bak')
    pass
