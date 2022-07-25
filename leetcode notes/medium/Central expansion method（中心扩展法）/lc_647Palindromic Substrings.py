#回文子串
class Solution:
    def countSubstrings(self, s: str) -> int:
        def zhaodao(l,r):
            nums = 0
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]: #字符串，取数用[]！！！
                nums += 1
                l -= 1
                r += 1
            return nums
        ans = 0                         #注意对齐！def函数和下面是平行关系！
        for i in range(0,len(s)):
            ans += zhaodao(i,i)
        for i in range(1,len(s)):
            ans += zhaodao(i-1,i)
        return ans
