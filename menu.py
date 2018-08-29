# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:SeekingMini
# Update:2018-08-27

import os
from tools.Search import searcher
from tools.Play import player

MUSIC_BOX = list([])  # 列表中的元素是player.Player类的实例，用于存储每一首正在播放或未并播放的歌曲
"""
特别说明：os.system("cls")只在命令行下有效！
"""


def display_total_info():
    os.system("cls")
    print("--------------------SuMusic--------------------")
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print("                 A.按歌名搜索")
    print("                 B.播放列表")
    print("+++++++++++++++++++++++++++++++++++++++++++++++")

    choice = input("请输入字母：")
    if choice == "A" or choice == "a":
        os.system("cls")
        music_name = input("请输入单曲名称：")
        music_single_search(music_name)
    elif choice == "B" or choice == "b":
        play_list()
    elif choice == "C" or choice == 'c':
        display_total_info()
    else:
        display_total_info()


def music_single_search(music_name):
    # 对应【A.按歌名搜索】
    searcher.search(music_name, 1)


def music_play(music_info, name, page):
    # 创建一个【player.Player】的示例，并将这个示例添加到【MUSIC_BOX】中
    if len(MUSIC_BOX) == 0:
        MUSIC_BOX.append(player.Player(music_info, name, page))
    else:
        flag = 1
        for each_music in MUSIC_BOX:
            if each_music.music_info == music_info:
                flag -= 1
        if flag:
            MUSIC_BOX.append(player.Player(music_info, name, page))

    for n in range(len(MUSIC_BOX)):
        if MUSIC_BOX[n].music_info == music_info:
            MUSIC_BOX[n].function()
            break


def play_list():
    no = 1  # 序号
    if len(MUSIC_BOX):
        os.system("cls")
        print("--------------------播放列表--------------------")
        for n in range(len(MUSIC_BOX)):
            print("{0}.{1} -- {2} -- {3}".format(no, MUSIC_BOX[n].music_info[0], MUSIC_BOX[n].music_info[2],
                                                 MUSIC_BOX[n].music_info[3]))
            no += 1
        print("------------------------------------------------")
        _ch_num = (input("请输入序号（输入0返回主菜单）："))
        if _ch_num == "0":
            display_total_info()
        else:
            MUSIC_BOX[int(_ch_num) - 1].function()
    else:
        os.system("cls")
        input("★★提示：播放列表为空！")
        display_total_info()


def judge_music_mode():
    pass

if __name__ == "__main__":
    display_total_info()
