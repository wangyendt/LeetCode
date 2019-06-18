# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
# 
# The length of both num1 and num2 is < 5100. 
# Both num1 and num2 contains only digits 0-9. 
# Both num1 and num2 does not contain any leading zero. 
# You must not use any built-in BigInteger library or convert the inputs to integer directly. 
# 
#

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = 0, 0
        ret = ''
        carry = 0
        if num1 == '0' and num2 == '0':
            return '0'
        while True:
            if p1 >= len(num1) and p2 >= len(num2):
                break
            d1, d2 = int(num1[-1 - p1]) if p1 < len(num1) else 0, int(num2[-1 - p2]) if p2 < len(num2) else 0
            res = carry + d1 + d2
            carry = res // 10
            ret = str(res % 10) + ret
            p1 += 1
            p2 += 1
        if carry:
            ret = '1' + ret
        return ret if ret[0] != '0' else ret[1:]


so = Solution()
print(so.addStrings('54', '45'))
print(so.addStrings('1', '9'))
