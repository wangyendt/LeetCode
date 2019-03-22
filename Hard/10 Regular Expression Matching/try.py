# encoding: utf-8


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) > 1 and len(s) > 1:
            if p[0] == '.' and p[1] != '*':
                s, p = s[1:], p[1:]
        return self.recursive(s, p)

    def recursive(self, s, p):
        print(s, p)
        if s == 'ba' and p == 'c*..b*a*':
            print('ffff')
        if (not '.' in p) and (not '*' in p) and p != s:
            return False
        if len(p) == 2:
            if p == '.*':
                return True
        if s == p:
            return True
        if not s and p:
            if len(p) == 2:
                if p[1] == '*':
                    return True
            else:
                if all([t == '*' for t in p[1::2]]) and len(p) % 2 == 0:
                    return True
                return False
        if (not s and p) or (not p and s):
            return False
        if not (p or s):
            return True
        if s[-1] == p[-1]:
            return self.recursive(s[:-1], p[:-1])
        else:
            if p[-1] != '.' and p[-1] != '*':
                return False
            elif p[-1] == '.':
                return self.recursive(s[:-1], p[:-1])
            else:  # p[-1] == '*'
                if len(p) == 1:
                    return False
                else:
                    if p[-2] == '.':
                        ind = 0
                        while ind < len(s):
                            ret = self.recursive(s[:len(s) - ind], p[:-2])
                            if ret:
                                return ret
                            ind += 1
                        return False
                    else:
                        ind = 0
                        while ind < len(s):
                            if ind >= 1 and s[len(s) - 1 - ind] != s[len(s) - 1 - ind + 1]:
                                return False
                            if p[-2] != s[len(s) - 1 - ind]:
                                if (not '.' in p[:-2] and not '*' in p[:-2]) and s[:len(s) - ind] != p[:-2]:
                                    return False
                                ret = self.recursive(s[:len(s) - ind], p[:-2])
                                if ret:
                                    return ret
                            if p[-2] == s[len(s) - 1 - ind]:
                                ret1 = self.recursive(s[:len(s) - ind], p[:-1])
                                ret2 = self.recursive(s[:len(s) - ind], p[:-2])
                                if ret1 or ret2:
                                    return True
                            ind += 1
                        return False


if __name__ == '__main__':
    so = Solution()
    # print(so.isMatch('aa','a'))
    # print(so.isMatch('aa','a*'))
    # print(so.isMatch('ab','.*'))
    # print(so.isMatch('aab','c*a*b'))
    # print(so.isMatch('mississippi', 'mis*is*p*.'))
    # print(so.isMatch('aaa', 'ab*ac*a'))
    # print(so.isMatch('mississippi', 'mis*is*p*.'))
    # print(so.isMatch('mississippi', 'mis*is*ip*.'))
    # print(so.isMatch('aa', 'a*'))
    # print(so.isMatch('aaa', 'ab*a'))
    # print(so.isMatch('aaa', 'ab*ac*a'))
    # print(so.isMatch('aasdfasdfasdfasdfas', 'aasdf.*asdf.*asdf.*asdf.*s'))
    # print(so.isMatch('bbbba', '.*a*a'))
    # print(so.isMatch('a', 'ab*a'))
    # print(so.isMatch('a', '.*..'))
    # print(so.isMatch("baabbbaccbccacacc", "c*..b*a*a.*a..*c"))
    print(so.isMatch("cbbbaccbcacbcca", "b*.*b*a*.a*b*.a*"))
