# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:SeekingMini

# 功能：下载音乐

import os
import menu
import requests


URL = r"https://v1.hitokoto.cn/nm/url/{0}"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}


def download(music_info):
    url = URL.format(music_info[1])
    music_url = requests.get(url, headers=HEADERS).json()['data'][0]['url']
    music_content = requests.get(music_url, headers=HEADERS).content
    input("下载成功！")
    with open(os.path.join(menu.PATH, "{0}.mp3".format(music_info[0])), "wb") as file:
        file.write(music_content)




