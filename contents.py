#!/usr/bin/python3
# AUTHOR: 陈科池
# DATE: 2022/09/02
# 此文件配置了程序使用的各种常量、配置、以及用于写入文件相对路径和数据，进一步规范了有关标识符的命名
# 路径的命名，一律用'PATH_路径名'的形式
# 文件的命名，一律用'FILENAME_文件名'的形式
# 文件的内容，一律用'CONTENT_文件名'的形式
# 同一个文件的信息，不间隔空行

import os

# 以下是引入自创的模块
import version

# 当前用户主目录
PATH_HOME = os.path.expandvars('$HOME') + '/'

# 键盘配置文件相对路径和文件名
PATH_XCOMPOSE = PATH_HOME
FILENAME_XCOMPOSE = ".XCompose"
# 键盘配置文件内容
CONTENT_XCOMPOSE = '''<Multi_key> <s> <s> : \"ŝ\"
<Multi_key> <g> <g> : \"ĝ\"
<Multi_key> <u> <u> : \"ŭ\"
<Multi_key> <c> <c> : \"ĉ\"
<Multi_key> <j> <j> : \"ĵ\"
<Multi_key> <h> <h> : \"ĥ\"
<Multi_key> <s> <v> : \"Ŝ\"
<Multi_key> <g> <v> : \"Ĝ\"
<Multi_key> <u> <v> : \"Ŭ\"
<Multi_key> <c> <v> : \"Ĉ\"
<Multi_key> <j> <v> : \"Ĵ\"
<Multi_key> <h> <v> : \"Ĥ\"
\n'''

# 程序开机自启动文件相对路径和文件名
PATH_AUTOSTART = PATH_HOME + ".config/autostart/"
FILENAME_AUTOSTART = 'Escaps.desktop'
# 程序开机自启动文件的内容
CONTENT_AUTOSTART = '''[Desktop Entry]
Name=Escaps
Exec=/opt/escaps/escaps
Icon=/opt/escaps/icon/escaps
Terminal=false
Type=Application
Categories=System
Coment=世界语帽子符输入辅助程序
Comment[zh_CN]=辅助输入世界语帽子字符
GenericName[zh_CN]=世帽符输入器
GenericName[zh_HK]=世帽符输入器
GenericName[zh_TW]=世帽符输入器
\n'''

# 程序自身配置文件相对路径和文件名
PATH_ESCONFIG = PATH_HOME + ".escaps/"
FILENAME_ESCONFIG = "esconfig"
# 程序自身配置文件的内容
CONTENT_ESCONFIG = '''
# 此文件暂空，功能待后续开发
# 联系作者：luorschen@163.com
'''

# 判断程序是否已经在运行的运行时标记文件，位于配置文件相同目录
PATH_RUNINGSTATE = PATH_ESCONFIG
FILENAME_RUNINGSTATE = "escaps_is_runing_now"
CONTENT_RUNINGSTARE = "Escaps" + version.VERSION + " is runing now!"


THANKS_TIP = '''感谢您使用Escaps for Linux'''

THANKS_TIP_ESPERANTO = '''Dankon pro uzi Escaps por Linux'''

START_TIPS = '''
使用说明：Escaps辅助您在计算机上输入世界语帽子字符（ĉ ŝ ĝ ŭ ĵ ĥ Ĉ Ŝ Ĝ Ŭ Ĵ Ĥ）。
为了方便您的使用，请允许程序开机启动。建议您设置系统的默认键盘布局为英语（美国），或其他与组合键直接对应的默认键盘布局。
程序使用了键盘监听，可能会被安全软件限制或误删除，并且可能需要您在安全软件上手动处理。

从5.0.1版本开始，Escaps可以同时提供两套独立机制来实现在Linux系统上输入帽子字符。
两套机制采用了不同的实现原理，使用时互补，可以在很大程度上解决您输入帽子符的难题。

机制一：程序默认设置右侧Alt键为组合键。
按右Alt键，松手，再按两次字母键,可输入小写帽子符；按右Alt键，松手，再按字母键和字母v键，可输入大写帽子符。
示例：按右Alt键，再按两次c键，可输入ĉ；按右Alt键，再按c键和v键，可输入Ĉ。

机制二：程序默认设置分号键为组合键。
按分号键，再按字母键，可输入小写帽子符；按两次分号键，再按字母键，可输入大写帽子符。
示例：按分号键，再按s键，可输入ŝ；按两次分号键，再按s键，可输入Ŝ。
如果在分号后输入空格、换行及其他无关字符，不再继续转换成帽子符。

祝您使用愉快！如有疑问或建议，可联系作者:陈科池(Pahelbro)， Email:luorschen@163.com
2022/09/05 中国四川省威远县（Gubernio Weiyuan ,Provinco Siĉuan , Ĉinio）'''

START_TIPS_ESPERANTO = '''
Escaps helpas vin enigi specialajn signojn de Esperanto en via komputilo.
(kaj eble specialaj signoj de iuj aliaj lingvoj estos subtenataj en posta versio)
Por via komforto, bonvolu permesi la programon komenci ĉe lanĉo.
Oni rekomendas, ke vi agordu la defaŭltan klavaran aranĝon de la sistemo al la angla (Usono),
aŭ aliaj klavararanĝoj kiuj rekte respondas al klavkombinaĵoj.
Ĉi tiu programo uzas klavaran monitoradon, povas esti limigita aŭ forigita erare,
kaj eble postulas, ke vi mane manipulu ĝin per via sekureca programaro.

Instrukcioj:
Defaŭlte, la programo fiksas la punktokomon-klavon kiel klavkombinon.
Premu la punktokomon klavon unufoje, tiam premu literklavon unufoje por enigi minusklan specialan literon;
Premu la punktokomon klavon dufoje, tiam premu literklavon unufoje por enigi majusklan specialan literon.
Se vi premas Spacon, Enigu kaj aliajn eksterajn signojn post punktokomo,ili ne daŭre konvertiĝos al specialaj signoj.
Fermu la fenestron, la programo funkcios en la fono,kaj ĝi ne plu aperos aŭtomate.
Premu Esc dufoje en 0.3 sekundoj por ĉesigi la programon.

Amuziĝu!
Se vi havas demandojn aŭ sugestojn, bonvolu kontakti la aŭtoron 
Chen Kechi (Pahelbro), Retpoŝto:luorschen@163.com
Gubernio Weiyuan, Provinco Siĉuano, Ĉinio
2022/09/05
'''
