# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:SeekingMini

# 功能：播放音乐

import os
import menu
import minimu
import requests
from tools.Download import downloader
from tools.Search import searcher


URL = r"https://api.imjad.cn/cloudmusic/?type=song&id={0}&br=320000"
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}


class Player(object):
    def __init__(self, music_info, name, page):
        os.system("cls")

        self._ = [name, page]
        self.music_info = music_info

        self.music_id = self.music_info[1]
        self.url = URL.format(self.music_id)
        self.music_url = self.get_music_url()  # 对音乐的URL进行处理
        self.song = minimu.load(self.music_url)

    def get_music_url(self):
        music_url = requests.get(self.url, headers=HEADERS).json()['data'][0]['url']
        return music_url

    def function(self):
        self.display_music_info()
        choice = input("请输入操作：")
        if choice == "A" or choice == "a":
            for n in range(len(menu.MUSIC_BOX)):
                try:
                    if menu.MUSIC_BOX[n].song.isplaying() and menu.MUSIC_BOX[n].music_info != self.music_info:
                        menu.MUSIC_BOX[n].song.stop()
                except AttributeError:
                    continue
            self.song.play()
            return self.function()
        elif choice == "B" or choice == 'b':
            self.song.pause()
            return self.function()
        elif choice == 'C' or choice == 'c':
            self.song.stop()
            return self.function()
        elif choice == "D" or choice == "d":
            downloader.download(self.music_info)
            return self.function()
        elif choice == 'E' or choice == 'e':
            menu.play_list()
        elif choice == "F" or choice == "f":
            searcher.search(self._[0], self._[1])
        elif choice == "G" or choice == "g":
            menu.display_total_info()

    def display_music_info(self):
        os.system('cls')
        max_length = max(len(self.music_info[0]), len(self.music_info[2]), len(self.music_info[3]))
        line_total = (max_length + 10) * "-"
        print(line_total)
        print("歌名：{0}".format(self.music_info[0]))
        print("歌手：{0}".format(self.music_info[2]))
        print("专辑：{0}".format(self.music_info[3]))
        print(line_total)
        print("++++++++++++")
        print("A.播放\nB.暂停\nC.停止\nD.下载\nE.播放列表\nF.返回上层\nG.返回主菜单")
        print("++++++++++++")


if __name__ == "__main__":
    pass



