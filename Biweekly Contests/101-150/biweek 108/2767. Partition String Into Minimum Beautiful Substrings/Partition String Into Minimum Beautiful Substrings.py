# author: wangye(Wayne)
# license: Apache Licence
# file: Partition String Into Minimum Beautiful Substrings.py
# time: 2023-08-10-10:00:44
# contact: wang121ye@hotmail.com
# site:  wangyendt@github.com
# software: PyCharm
# code is far away from bugs.


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        inf = float('inf')
        dp = [0] + [inf] * n
        for i in range(n):
            if s[i] == '1':
                cur = 0
                for j in range(i, n):
                    cur = cur * 2 + int(s[j])
                    if 15625 % cur == 0:
                        dp[j + 1] = min(dp[j + 1], dp[i] + 1)
        return dp[n] if dp[n] < inf else -1


so = Solution()
print(so.minimumBeautifulSubstrings(s="1011"))
print(so.minimumBeautifulSubstrings(s="111"))
print(so.minimumBeautifulSubstrings(s="0"))
