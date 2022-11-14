import main
import re, os


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


def get_xml_file(Element_path, hz):
    ls = main.get_filelist(Element_path)
    xml_ls = []
    for i in ls:
        last_name = i[-1:-4:-1][::-1]
        if last_name == hz:
            if 'md5' not in i:
                xml_ls.append(i)
    return xml_ls


def del_file(ls:list):
    for i in ls:
        try:
            os.remove(i)
        except IOError as e:
            print(e)
            print("删除错误")

if __name__ == '__main__':
    # update_file('ts/ts.xml', 'ogg', 'mp3')
    # pass
    print(get_xml_file(r'C:\Users\BYSEVEN\Desktop\Naruto\NarutoSenki\assets\Element', 'bak'))
