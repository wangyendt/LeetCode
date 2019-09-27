# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/27 16:44
# software: PyCharm


import matplotlib.pyplot as plt
import numpy as np
import seaborn

if __name__ == '__main__':
    plt.rcParams['font.family'] = 'FangSong'
    plt.rcParams['font.size'] = 20
    constellations = ['白羊', '金牛', '双子', '巨蟹',
                      '狮子', '处女', '天枰', '天蝎',
                      '射手', '摩羯', '水瓶', '双鱼']
    data = np.loadtxt('constellations pair matrix.txt', dtype=np.int)
    data = np.flipud(data)
    seaborn.heatmap(data, cmap=plt.cm.get_cmap('rainbow'))
    plt.xticks(np.arange(12) + 0.5, constellations)
    plt.yticks(np.arange(12)[::-1] + 0.5, constellations)
    for i in range(12):
        for j in range(12):
            plt.text(i + 0.5, j + 0.5, data[i, j], horizontalalignment='center', verticalalignment='center')
    # plt.axis('equal')
    plt.title('constellations pair matrix -- wangye')
    # plt.savefig('constellations.png')
    plt.show()
