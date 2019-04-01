# encoding: utf-8


class Solution:
    def check(self, s1, s2):
        return sum(map(lambda ch: s1.count(ch), s2))

    def isMatch(self, s: str, p: str) -> bool:
        if len(p) > 1 and len(s) > 1:
            if p[0] == '.' and p[1] != '*':
                s, p = s[1:], p[1:]
        return self.recursive(s, p)

    def recursive(self, s, p):
        print(s, p)
        if '.*' in p and self.check('*', p) >= len(p) / 2:
            return True
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
                        if p[-2] != s[-1]:
                            return self.recursive(s, p[:-2])
                        ind = 0
                        while ind < len(s):
                            if ind >= 1 and s[len(s) - 1 - ind] != s[len(s) - 1 - ind + 1]:
                                break
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
    # print(so.isMatch("cbbbaccbcacbcca", "b*.*b*a*.a*b*.a*"))
    print(so.isMatch('aababcacabccbacaaba', 'ab*c*c*b..*a*c*a*b*'))
    # print(so.isMatch("ccacbcbcccabbab",".c*a*aa*b*.*b*.*"))
