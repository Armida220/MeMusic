# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:SeekingMini

# 功能：程序的入口文件

import os
from tools.Search import searcher
from tools.Play import player

PATH = r"C:\Users\l\Music"  # 音乐的默认下载路径
MUSIC_BOX = list([])  # 列表中的元素是player.Player类的实例，用于存储每一首正在播放或未并播放的歌曲
"""
特别说明：os.system("cls")只在命令行下有效！
"""


def display_total_info():
    os.system("cls")
    print("--------------------MeMusic--------------------")
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print("                 A.按歌名搜索")
    print("                 B.播放列表")
    print("                 S.设置")
    print("+++++++++++++++++++++++++++++++++++++++++++++++")

    choice = input("输入（字母：获取相关操作）：")
    if choice == "A" or choice == "a":
        os.system("cls")
        music_name = input("输入(单曲名称 | 回车：回到主菜单）：")
        if music_name == "":
            display_total_info()
        else:
            music_single_search(music_name)
    elif choice == "B" or choice == "b":
        play_list()
    elif choice == "S" or choice == 's':
        settings()
    else:
        # 无效操作一律重新调用主函数
        display_total_info()


def music_single_search(music_name):
    # 对应【A.按歌名搜索】
    searcher.search(music_name, 1)


def music_play(music_info, name, page):
    # 创建一个【player.Player】的示例，并将这个示例添加到【MUSIC_BOX】中
    if len(MUSIC_BOX) == 0:
        # 如果列表为空，则向列表中添加元素
        MUSIC_BOX.append(player.Player(music_info, name, page))
    else:
        # 判断元素是否已经存在，如果已经存在，则不向列表中重复添加
        flag = 1
        for each_music in MUSIC_BOX:
            if each_music.music_info == music_info:
                flag -= 1
        if flag:
            MUSIC_BOX.append(player.Player(music_info, name, page))

    # 进入特定的某一首音乐
    for n in range(len(MUSIC_BOX)):
        if MUSIC_BOX[n].music_info == music_info:
            MUSIC_BOX[n].function()
            break


def play_list():
    # 进入播放列表
    no = 1  # 序号
    if len(MUSIC_BOX):
        os.system("cls")
        print("--------------------播放列表--------------------")
        for n in range(len(MUSIC_BOX)):
            print("{0}.{1} -- {2} -- {3}".format(no, MUSIC_BOX[n].music_info[0], MUSIC_BOX[n].music_info[2],
                                                 MUSIC_BOX[n].music_info[3]))
            no += 1
        print("------------------------------------------------")
        _choice = (input("输入（0：返回主菜单 | 序号：进入歌曲 | D：删除歌曲）："))
        if _choice == "0":
            display_total_info()
        elif _choice == "D" or _choice == "d":
            _ch_num = input("输入（序号：删除歌曲 | 0：返回）：")
            try:
                if _ch_num == "0":
                    play_list()
                else:
                    del MUSIC_BOX[int(_ch_num)-1]
                    play_list()
            except IndexError:
                play_list()
            except ValueError:
                play_list()
        else:
            try:
                MUSIC_BOX[int(_choice) - 1].function()
            except IndexError:
                play_list()
            except ValueError:
                play_list()
    else:
        os.system("cls")
        input("★★提示：播放列表为空！")
        display_total_info()


def judge_music_mode():
    # 判断某一首音乐的播放状态，代码仍在开发中......
    pass


def settings():
    os.system("cls")
    print("1.下载路径")
    print("2.用户登录")

    _choice = input("请输入序号（输入0返回主菜单）：")
    if _choice == "1":
        _path = input(r"请输入下载路径（默认：C:\Users\l\Music）：")
        if os.path.exists(_path):
            input("设置成功！")
            global PATH
            PATH = _path
            settings()
        else:
            input("★★提示：路径不存在！")
            pass
        settings()
    elif _choice == "2":
        input("★★提示：功能暂未开放！")
        settings()
    elif _choice == "0":
        display_total_info()
    else:
        settings()


if __name__ == "__main__":
    display_total_info()