#!/usr/bin/python3
# AUTHOR: 陈科池
# DATE: 2022/09/02
# 此模块用于单独显示Escaps提示窗口，编译时应该单独编译成一个可执行文件，并在打包时单独创建一个用于启动此程序的.desktop文件


import tkinter as tk

# 以下是引入自创模块
import version
import contents

tips_window = tk.Tk()
# 获取屏幕长度、宽度
screen_width, screen_height = tips_window.maxsize()
# 窗口长、宽
window_width = screen_width / 1.2
window_height = screen_height / 1.2
# 窗口起始坐标
start_x = (screen_width - window_width) / 2
start_y = (screen_height - window_height) / 2


# 设置窗口显示在屏幕中心
def set_win_center(the_window):
    # 设置窗口初始大小和位置
    size_xy = '%dx%d+%d+%d' % (
        window_width, window_height, start_x, start_y)
    the_window.geometry(size_xy)


class MainFrame:
    def __init__(self, master):
        self.root = master
        set_win_center(self.root)
        InitFace(self.root)


class InitFace:
    def __init__(self, master):
        self.master = master
        # 基准界面initface
        self.InitFace = tk.Frame(self.master)
        self.InitFace.pack()
        # 设置窗口居中显示
        set_win_center(self.master)
        btn = tk.Button(self.InitFace, text='中文', command=self.change, width=30)
        btn.pack()
        # 设置窗口显示内容
        label_space = tk.Label(self.InitFace, text="", font=('Microsoft Yahei', 8, ''),
                               # 设置标签内容区大小
                               width=100, height=0)
        label_space.pack()
        label_title = tk.Label(self.InitFace, text=contents.THANKS_TIP_ESPERANTO,
                               font=('Microsoft Yahei', 16, 'bold'),
                               # 设置标签内容区大小
                               width=100, height=0)
        label_title.pack()
        label_instruction = tk.Message(self.InitFace, text=contents.START_TIPS_ESPERANTO,
                                       font=('Microsoft Yahei', 12, 'bold'), width=window_width)
        label_instruction.pack()

    def change(self):
        self.InitFace.destroy()
        SecondFace(self.master)


class SecondFace:
    def __init__(self, master):
        self.master = master
        self.Face1 = tk.Frame(self.master, )
        self.Face1.pack()
        # 设置窗口居中显示
        set_win_center(self.master)
        btn_back = tk.Button(self.Face1, text='Esperanto', command=self.back, width=30)
        btn_back.pack()
        # 获取屏幕长度、宽度
        screen_width, screen_height = tips_window.maxsize()
        # 窗口长、宽
        window_width = screen_width
        # 设置窗口显示内容
        label_space = tk.Label(self.Face1, text="", font=('Microsoft Yahei', 8, ''),
                               # 设置标签内容区大小
                               width=100, height=0)
        label_space.pack()
        label_title = tk.Label(self.Face1, text=contents.THANKS_TIP, font=('Microsoft Yahei', 18, 'bold'),
                               # 设置标签内容区大小
                               width=100, height=0)
        label_title.pack()
        label_instruction = tk.Message(self.Face1, text=contents.START_TIPS,
                                       font=('Microsoft Yahei', 14, 'bold'), width=window_width)
        label_instruction.pack()

    def back(self):
        self.Face1.destroy()
        InitFace(self.master)


def init_tips_window():
    tips_window.title(version.NAME + version.VERSION + '  ' + version.DATE)
    MainFrame(tips_window)
    tips_window.mainloop()


