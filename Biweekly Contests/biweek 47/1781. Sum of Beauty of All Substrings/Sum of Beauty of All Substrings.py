#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sum of Beauty of All Substrings.py 
@time: 2021/03/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
import bisect


class Solution:
    def beautySum(self, s: str) -> int:
        ret = 0
        for i in range(len(s)):
            sort = []
            res = collections.defaultdict(int)
            for j in range(i, len(s)):
                if not sort or res[s[j]] == 0:
                    res[s[j]] = 1
                    sort[0:0] = [1]
                    # sort.append(res[s[j]])
                else:
                    idx = bisect.bisect_left(sort, res[s[j]])
                    # sort.pop(idx)
                    sort[idx:idx + 1] = []
                    res[s[j]] += 1
                    # bisect.insort(sort, res[s[j]])
                    idx2 = bisect.bisect_left(sort, res[s[j]])
                    sort[idx2:idx2] = [res[s[j]]]
                if len(sort) > 1:
                    ret += sort[-1] - sort[0]
                # print(f'i={i},j={j},s[j]={s[j]},{sort},{res}')
        return ret


so = Solution()
print(so.beautySum('aabcb'))
print(so.beautySum('aabcbaa'))
print(so.beautySum('a' * 500))
print(so.beautySum("hqyadervmdrmdphdvaxumxqyfxpbcgdsoaldxjmgjwgoazyvbyghwcaoftqdezlkdjhmiqxyydzzfxxxzyamapuxvinmyhrlzxcdasvytkvgxxgpgrqrjntwlqjxd"))