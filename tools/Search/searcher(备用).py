# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:SeekingMini
# Update:2018-08-27

# 功能：搜索单曲

import os
import menu
import requests

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
URL = "https://api.imjad.cn/cloudmusic/?type=search&search_type=1&s={0}&offset={1}"


def search(name, page):
    os.system('cls')
    page_num = 20 * (page - 1)
    url = URL.format(name, page_num)
    music_total_info = requests.get(url, headers=HEADERS).json()
    music_list = []
    for each in music_total_info['result']['songs']:
        music_name = each['name']
        music_id = each['id']
        music_artist = each['ar'][0]['name']
        music_album = each['al']['name']
        music_list.append([music_name, str(music_id), music_artist, music_album])

    print("搜索结果：")
    for n in range(len(music_list)):
        print("{0}.{1} | {2} | {3}".format(n+1, music_list[n][0], music_list[n][2], music_list[n][3]))
    print("当前页数：{}".format(page))

    print("\nA.上一页 B.下一页 C.返回主菜单")
    choice = input("请输入数字（字母）获取相关操作：")
    try:
        choice = int(choice)
        music_info = music_list[choice - 1]  # 获取音乐的ID
        menu.music_play(music_info, name, page)

    except ValueError:
        if choice == "A" or choice == "a":
            if page == 1:
                os.system('cls')
                search(name, page)
            else:
                page -= 1
                os.system("cls")
                search(name, page)
        elif choice == "B" or choice == "b":
            page += 1
            os.system("cls")
            search(name, page)
        elif choice == "C" or choice == 'c':
            menu.display_total_info()
        else:
            search(name, page)


if __name__ == "__main__":
    music_name = input("请输入单曲名称：")
    search(music_name, 1)
