class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1000-M, 500-D, 100-C, 50-L, 10-X, 5-V, 1-I
        romanDict = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        l = len(s)
        if l == 1:
        	return romanDict[s]
        res = 0
        for i in xrange(l-1):
        	if romanDict.get(s[i+1]) <= romanDict.get(s[i]):
        		res = res + romanDict.get(s[i])
        	else:
        		res = res - romanDict.get(s[i])
        res = res+romanDict.get(s[l-1])
        return res
