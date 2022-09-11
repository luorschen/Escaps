#!/usr/bin/python3
# AUTHOR: 陈科池
# DATE: 2022/09/02
# 此模块用来写入文件

import os

# 自定义函数用来写入文件内容
def write_file(filepath, filename, filecontent):
    # 判断该文件是否已经存在，不存在时创建并写入指定内容
    try:
        if not os.path.exists(filepath + filename):
            print(filepath + filename + "文件不存在，将写入：")
            fp = open(filepath + filename, "w")
            if fp is None:
                print(filepath + filename + " 文件打开或创建失败\n")
                return -1
            print("将写入以下内容：\n" + filepath + filename + "\n")
            fp.write(filecontent + os.linesep)
        else:
            print(filepath + filename + "\n文件已存在，未写入内容\n\n")

    except Exception:
        pass


# 实现删除文件的功能
def remove_file(filepath, filename):
    try:
        print("\n删除文件：" + filepath + filename + "\n")
        os.system('rm -rf  ' + filepath + filename)
    except Exception:
        pass
