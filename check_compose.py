#!/usr/bin/python3
# AUTHOR: 陈科池
# DATE: 2022/09/02
# 此模块用于创建系统组合键
import os
# 以下是引入自创的模块
import version
import write_content
import contents
import alarm


# 设置组合键的函数
def set_compose():
    # 无限循环使程序始终运行,但是可能异常退出
    try:
        # 执行启用组合键的命令，默认用右侧Alt键
        os.system('setxkbmap -option compose:ralt')

        # 目录不存在时创建目录
        if not os.path.exists(contents.PATH_ESCONFIG):
            print("Escaps目录不存在，将创建" + contents.PATH_ESCONFIG)
            os.makedirs(contents.PATH_ESCONFIG, 0o755, False)

        # 创建并写入文件/.XCompose
        write_content.write_file(contents.PATH_XCOMPOSE, contents.FILENAME_XCOMPOSE, contents.CONTENT_XCOMPOSE)
        # 创建并写入文件/.config/autostart/Escaps.desktop
        write_content.write_file(contents.PATH_AUTOSTART, contents.FILENAME_AUTOSTART, contents.CONTENT_AUTOSTART)
        # 创建并写入文件/.escaps/.config
        write_content.write_file(contents.PATH_ESCONFIG, contents.FILENAME_ESCONFIG, contents.CONTENT_ESCONFIG)

    except:
        # write_content.remove_file(contents.PATH_RUNINGSTATE, contents.FILENAME_RUNINGSTATE)
        alarm.show_alarm("Escaps" + version.VERSION + "已结束运行!\n")
        # os.remove(contents.PATH_RUNINGSTATE + contents.FILENAME_RUNINGSTATE)
        # print("退出程序，删除运行标识文件")
        pass
