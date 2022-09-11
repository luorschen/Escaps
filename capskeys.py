#!/usr/bin/python3
# AUTHOR: 陈科池
# DATE: 2022/09/02
# 此文件定义各个帽子字符的变量名
# 从6.0版起，支持输入多种拉丁字母语言的特殊字符

from pynput.keyboard import KeyCode, Key

# Esperanto

# 响应键盘的组合键
COMPOSE_KEY = ';'

# lower case
caps_c = chr(265)
caps_g = chr(285)
caps_h = chr(293)
caps_j = chr(309)
caps_s = chr(349)
caps_u = chr(365)

# upper case
caps_C = chr(264)
caps_G = chr(284)
caps_H = chr(292)
caps_J = chr(308)
caps_S = chr(348)
caps_U = chr(364)

# 无帽字符的范围
NORMAL_CHARS = ('c', 's', 'g', 'j', 'h', 'u', 'C', 'S', 'G', 'J', 'H', 'U')

# 普通字符与帽子字符对应的字典
CAPS_KEYS = {'c': caps_c, 's': caps_s, 'g': caps_g,
             'j': caps_j, 'h': caps_h, 'u': caps_u,
             'C': caps_C, 'S': caps_S, 'G': caps_G,
             'J': caps_J, 'H': caps_H, 'U': caps_U}

# 监听响应的按键
NORMAL_KEYS = (KeyCode.from_char('c'),
               KeyCode.from_char('s'),
               KeyCode.from_char('g'),
               KeyCode.from_char('j'),
               KeyCode.from_char('h'),
               KeyCode.from_char('u'),
               KeyCode.from_char('C'),
               KeyCode.from_char('S'),
               KeyCode.from_char('G'),
               KeyCode.from_char('J'),
               KeyCode.from_char('H'),
               KeyCode.from_char('U'),
               KeyCode.from_char(COMPOSE_KEY),
               )
