class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = self.s2t(s)
        p = self.tranform(t)
        print p
        print t
        pmax = 0
        pindex = 0
        for i in xrange(len(p)):
            if p[i]>pmax:
                pmax = p[i]
                pindex = i
        return s[(pindex-pmax-1)/2:(pindex+pmax-1)/2]

    
    def s2t(self,s):
        t = ''
        for i in xrange(len(s)):
            t = t+"#"+s[i]
        t = '^'+t+"#$"
        # print t
        return t

    def tranform(self,t):
        p = [0]*len(t)
        C = 0
        R = 0
        for i in xrange(1,len(t)-1):
            i_mirror = 2*C-i
            p[i] = min(R-i,p[i_mirror]) if R>i else 0
            # print i+p[i]+1,i-p[i]-1,t
            while (t[i+1+p[i]]==t[i-1-p[i]]):
                p[i] = p[i]+1

            if (i+p[i]>R):
                R = i+p[i]
                C = i
        return p



# test = Solution()
# print test.longestPalindrome("bb")

