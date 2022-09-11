#!/usr/bin/python3
#!/usr/bin/python3
# AUTHOR: 陈科池
# DATE: 2022/09/02
# 这是escaps的主程序,用来启动程序
import os
# 以下是引入自创的模块
import alarm
import tips_window
import write_content
import contents
import check_compose
from keyboard_listen import start_listen


def main():
    try:
        start_escaps()

    except Exception:
        alarm.show_alarm("程序未成功启动")
        # try:
        #     os.remove(contents.PATH_RUNINGSTATE + contents.FILENAME_RUNINGSTATE)
        # except Exception:
        #     pass
        exit(-1)


def start_escaps():
    try:
        print("运行程序：\n")
        # 目录不存在时创建目录
        if not os.path.exists(contents.PATH_ESCONFIG):
            print("Escaps目录不存在，将创建" + contents.PATH_ESCONFIG)
            os.makedirs(contents.PATH_ESCONFIG, 0o755, False)

        # esconfig不存在时创建esconfig，此配置文件的格式和用途，将在后续版本中开发
        if not os.path.exists(contents.PATH_ESCONFIG + contents.FILENAME_ESCONFIG):
            # 创建esconfig
            write_content.write_file(contents.PATH_ESCONFIG, contents.FILENAME_ESCONFIG, contents.CONTENT_ESCONFIG)
            # 创建启动文件
            write_content.write_file(contents.PATH_AUTOSTART, contents.FILENAME_AUTOSTART,
                                     contents.CONTENT_AUTOSTART)
            # 初次使用，显示提示窗口
            tips_window.init_tips_window()

        # 检查程序是否在运行
        # 如果escaps在运行，ret == 0；没有运行则为256
        # ret = os.system("echo $(pgrep escaps) |grep -c \" \"")
        # # print("ret = "+str(ret))
        # if not ret:
        #     print("错误：不能重复运行escaps！")
        #     exit(-1)

        # 创建运行时标识文件RUNINGSTATE
        # if os.path.exists(contents.PATH_RUNINGSTATE + contents.FILENAME_RUNINGSTATE):
        #     os.remove(contents.PATH_RUNINGSTATE + contents.FILENAME_RUNINGSTATE)
        # else:
        #     write_content.write_file(contents.PATH_RUNINGSTATE, contents.FILENAME_RUNINGSTATE,
        #                              contents.CONTENT_RUNINGSTARE)

        # 确保各种配置生效
        check_compose.set_compose()
        # 调用键盘监听机制
        start_listen()

    except Exception:
        pass
        # os.remove(contents.PATH_RUNINGSTATE + contents.FILENAME_RUNINGSTATE)


if __name__ == "__main__":
    main()
