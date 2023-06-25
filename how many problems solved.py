# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: how many problems solved.py
@time: 2022/05/11
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

import collections
import re
import platform

from pywayne.tools import *

files = list_all_files(
    '.',
    keys_or=['.py', '.ipynb'],
    outliers=['checkpoint',
              '\\Tools\\', '/Tools/',
              '\\Interview\\', '/Interview/',
              '\\how many problems solved.py',
              '/how many problems solved.py',
              '\\search_contest_result.py',
              '/search_contest_result.py',
              '[not submitted]']
)
res = collections.defaultdict(list)
for i, file in enumerate(files):
    if platform.system().lower() == 'darwin':
        no = re.findall(r'/(\d+)\..*', file)[0]
    else:
        no = re.findall(r'\\(\d+)\..*', file)[0]
    res[no].append((i, no, file))
# tmp = sorted(res.values(),key=lambda x:len(x))
# [print(len(t),t) for t in tmp]
print(len(res))
# [print(r) for r in natsort.natsorted(res.keys())]
