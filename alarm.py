#!/usr/bin/python3
# AUTHOR: 陈科池
# DATE: 2022/09/02
# 此模块用于显示提示窗口
import tkinter as tk

# 以下是引入自创的模块
import version


# 显示报警窗口
def show_alarm(alarm_text):
    alarm_window = tk.Tk()
    alarm_window.title("Escaps" + version.VERSION + "提 示")
    alarm_window.resizable(False, False)
    alarm_window.attributes("-topmost", True)

    # 获取屏幕长度、宽度
    screen_width, screen_height = alarm_window.maxsize()
    # 窗口长、宽
    window_width = screen_width / 2
    window_height = screen_height / 6
    # 计算窗口的起始坐标
    start_x = screen_width / 3
    start_y = screen_height / 3
    # 设置窗口居中显示

    size_xy = '%dx%d+%d+%d' % (
        window_width, window_height, start_x, start_y)
    alarm_window.geometry(size_xy)

    alarm_text_label = tk.Label(alarm_window, text=alarm_text, font=('Microsoft YaHei', 14, 'bold'),
                                # 设置标签内容区大小
                                width=50, height=6)
    alarm_text_label.pack()

    alarm_window.mainloop()

