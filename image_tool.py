# _*_coding:CP936 _*_

# @PROJECT : audio_tools
# @Time : 2022/11/16 13:19
# @Author : Byseven
# @File : image_tool.py
# @SoftWare:

import subprocess

cmd = "ping www.baidu.com"


# proc = subprocess.Popen(commend, shell=True, stdout=subprocess.PIPE, bufsize=1, encoding='gbk')

# ʵʱ��ӡcmd_log
def run_cmd(commend):
    """
    ��ȡ����CMD�ķ���
    Args:
        commend: Ҫִ�е�cmd����
    Returns:

    """
    proc = subprocess.Popen(commend, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, encoding='gbk')
    print(proc.stdout.read())
    proc.stdout.close()


run_cmd("ping www.baidu.com")
