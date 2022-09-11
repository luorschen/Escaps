#!/usr/bin/python3
# 这是一个键盘监听控制模块
# AUTHOR: 陈科池
# DATE: 2022/08/31
# 提高运行效率：调试完成后应当注释掉所有print语句；
# 不要在if和循环的判定条件上，以及参数括号里写运算表达式，甚至在这些地方引用其他函数

from pynput.keyboard import Controller
from pynput.keyboard import Listener

import time

# 自定义的模块
import alarm
from capskeys import *

# 标记是否转换成帽子字符
is_CAP = False
# 标记是否是大写帽子字符
is_UPPER = False
# 标记是否输入了多余的分号
NOT_MORE_COMPOSE_KEY = False
# 标记是否输入了其他的键（不在normal_keys元组）
OTHER_KEY_PRESSED = False
# 标记是否允许输入backspace
BACKSPACE_ALLOWED = False
# 用户自定义的组合键，默认是分号
COMPOSE_KEY = ';'
# 按键对应的字符，初始为空
key_to_char = ''
# 字母对应的帽子字符，初始为空
caped_key = ''
# 保存大写消耗的时间
upper_time_gap = 0
# 保存小写消耗的时间
lower_time_gap = 0
# 标记是否退出程序
exit_escaps = False
# 标记按Esc的时间间隔
esc_gap = 0

# 实例化监听器
keyboard = Controller()

# 输入小写字母的方法
def type_lower(key_to_input):
    # print("输入小写字母，重新计数分号")
    global lower_time_gap
    global is_CAP
    global is_UPPER
    is_CAP = False
    is_UPPER = False

    # 输入小写字符需要删除两个字符
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    time.sleep(0.02)
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    # time.sleep(0.02)
    # 输入对应的帽子字符
    lower_time_gap = time.time()
    keyboard.press(key_to_input)
    time.sleep(0.02)
    keyboard.release(key_to_input)
    lower_time_gap = time.time() - lower_time_gap
    # print(key_to_input)
    # print(f"间隔时间:{lower_time_gap}秒")


# 输入大写字母的方法
def type_upper(key_to_input):
    # print("输入大写字母，重新计数分号")
    global is_CAP
    global is_UPPER
    is_CAP = False
    is_UPPER = False
    global upper_time_gap
    # 输入大写字符需要删除三个字符
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    time.sleep(0.05)
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    time.sleep(0.05)
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)

    # 输入对应的帽子字符
    upper_time_gap = time.time()
    with keyboard.pressed(
            Key.shift,
            key_to_input,
    ):
        pass

    # keyboard.press(Key.shift)
    # keyboard.type(key_to_input)
    # time.sleep(0.02)
    # keyboard.release(Key.shift)

    # keyboard.press(Key.shift)
    # keyboard.press(key_to_input)
    # keyboard.release(Key.shift)
    # keyboard.release(key_to_input)

    upper_time_gap = time.time() - upper_time_gap
    # print(key_to_input)
    # print(f"间隔时间:{upper_time_gap}秒")


# 键盘按下的响应
def on_press(key):
    """
    :param key:
    on_press 方法运行机制：
    # （最外层判断）判断如果按键在指定范围内(NORMAL_KEYS)
    # （第二层判断）判断第一次按键，如果是分号，记录帽子状态(is_CAP)为真（初始状态为假）；如果帽子状态为真，输入小写字母，转换帽子状态为假；
    # （第三层判断）判断第二次按键，如果是分号，记录大写状态为真（初始状态为假）；如果是字母，输入转换后的小写帽子字符，转换帽子状态为假；
    # （并列第三层判断）判断第三次按键，如果分号和帽子均为真，三次删除键，输入大写帽子字符，转换帽子状态为假、大写状态为假
    """
    global is_CAP
    global is_UPPER
    global OTHER_KEY_PRESSED
    global NOT_MORE_COMPOSE_KEY
    global COMPOSE_KEY
    global key_to_char
    global caped_key

    try:

        # print("当前按下：" + str(key))
        # 仅响应指定的按键：有关字母及分号
        # 将按键从KeyCode转化成对应的字符类型
        key_to_char = eval(str(key))

        # 如果按下指定的键
        if key in NORMAL_KEYS:
            # print("响应，当前按下：" + str(key))

            # 如果需要转换成帽子字符
            if is_CAP:

                # 如果第三次输入时大写标记为真，并且输入的字符是字母，输入大写字母
                # 如果第三次输入的是空格
                if is_UPPER:
                    # if key == Key.space:
                    #     # print("空格，重新计数分号")
                    #     pass
                    # elif key == Key.enter:
                    #     # print("换行，重新计数分号")
                    #     pass

                    # 如果第三次输入的是字母
                    if key_to_char.isalpha():
                        # 键盘字符重赋值为大写字母
                        key_to_char = key_to_char.upper()
                        caped_key = CAPS_KEYS.get(key_to_char)
                        # print("is_CAP:" + str(is_CAP) + " is_UPPER:" + str(is_UPPER) + " key_to_char:" + key_to_char)
                        type_upper(caped_key)

                    # 如果第三次输入的是组合键
                    elif key_to_char == COMPOSE_KEY:
                        # 确定多输入了组合键
                        NOT_MORE_COMPOSE_KEY = False
                        keyboard.press(Key.backspace)
                        keyboard.release(Key.backspace)
                        keyboard.press(Key.backspace)
                        keyboard.release(Key.backspace)
                        keyboard.press(Key.backspace)
                        keyboard.release(Key.backspace)
                        time.sleep(0.02)
                        # print("多余的分号,重新计数分号")

                    is_CAP = False
                    is_UPPER = False

                else:
                    # # 如果第二次输入的是空格
                    # if key == Key.space:
                    #     is_CAP = False
                    #     is_UPPER = False
                    #     print("空格，重新计数分号")
                    # # 如果第二次输入的是backspace
                    # elif key == Key.backspace:
                    #     is_CAP = False
                    #     is_UPPER = False
                    #     print("退格，重新计数分号")
                    # # 如果第二次输入的是换行
                    # elif key == Key.enter:
                    #     is_CAP = False
                    #     is_UPPER = False
                    #     print("换行，重新计数分号")

                    # 如果第二次输入是字母，并且isupper是False，输入转换的帽子符；如果第二次输入是分号，大写标记改成True
                    if key_to_char.isalpha():  # and key_to_char.islower():
                        is_CAP = False
                        is_UPPER = False
                        # print(" key_to_char:" + key_to_char +
                        #       " is_CAP:" + str(is_CAP) +
                        #       " is_UPPER:" + str(is_UPPER) +
                        #       " NOT_MORE_COMPOSE_KEY:" + str(NOT_MORE_COMPOSE_KEY))
                        caped_key = CAPS_KEYS.get(key_to_char)
                        type_lower(caped_key)

                    # 如果第二次输入的是分号，大写标记改成True
                    elif NOT_MORE_COMPOSE_KEY and key_to_char == COMPOSE_KEY:
                        is_CAP = True
                        is_UPPER = True
                        # print("第二次分号")
                        # print(" key_to_char:" + key_to_char +
                        #       " is_CAP:" + str(is_CAP) +
                        #       " is_UPPER:" + str(is_UPPER) +
                        #       " NOT_MORE_COMPOSE_KEY:" + str(NOT_MORE_COMPOSE_KEY))

                    # 确定没有多输入组合键
                    elif not NOT_MORE_COMPOSE_KEY:
                        NOT_MORE_COMPOSE_KEY = True

            else:

                # 如果第一次输入的是分号，转换标记改成True
                if key_to_char == COMPOSE_KEY:
                    is_CAP = True
                    NOT_MORE_COMPOSE_KEY = True
                    # print("第一次分号")
                    # print(" key_to_char:" + key_to_char +
                    #       " is_CAP:" + str(is_CAP) +
                    #       " is_UPPER:" + str(is_UPPER) +
                    #       " NOT_MORE_COMPOSE_KEY:" + str(NOT_MORE_COMPOSE_KEY))
                else:
                    is_CAP = False

                # 每轮重新赋值按键字符
                is_UPPER = False
                OTHER_KEY_PRESSED = True
                NOT_MORE_COMPOSE_KEY = True
                key_to_char = ''
                caped_key = ''

        # 如果不是指定按键，重新计数
        else:
            is_CAP = False
            is_UPPER = False
            OTHER_KEY_PRESSED = True
            NOT_MORE_COMPOSE_KEY = True
            key_to_char = ''
            caped_key = ''
            # print("其他的键，重新计数分号")

    except Exception:
        pass


def on_release(key):
    global exit_escaps
    global esc_gap
    if key == Key.esc:
        if exit_escaps:
            # 记录两次按下Esc的时间间隔
            esc_gap = time.time() - esc_gap
            # 如果时间间隔小于1秒，退出程序,否则时间间隔归零
            if esc_gap < 0.3:
                # print("按下Esc，程序终止运行,间隔时间:" + str(esc_gap) + "秒\n")
                alarm.show_alarm("程序终止运行")
                exit(0)
                return False
            else:
                # print("按下Esc，程序未终止运行,间隔时间:" + str(esc_gap) + "秒\n")
                esc_gap = time.time()
        else:
            # 记录第一次按下Esc的时间
            esc_gap = time.time()
            exit_escaps = True


def start_listen():
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        print("Start listening......")
        listener.join()
