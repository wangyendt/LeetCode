# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/26 16:59
# software: PyCharm


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        for _ in range(len(v2) - len(v1)):
            v1.append(0)
        for vi in range(len(v2)):
            if int(v1[vi]) > int(v2[vi]):
                return 1
            elif int(v1[vi]) < int(v2[vi]):
                return -1
        for i in range(len(v1) - len(v2)):
            if int(v1[len(v2) + i]) > 0:
                return 1
        return 0


so = Solution()
print(so.compareVersion(version1="0.1", version2="1.1"), -1)
print(so.compareVersion(version1="1.0.1", version2="1"), 1)
print(so.compareVersion(version1="7.5.2.4", version2="7.5.3"), -1)
print(so.compareVersion(version1="1.01", version2="1.001"), 0)
print(so.compareVersion(version1="1.0", version2="1.0.0"), 0)
