class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lines = ['']*numRows
        drt = 1 # 0 represents down, 1 represents up
        pos = 0
        if len(s)==0 or numRows<=1: return s
        for i in xrange(len(s)):
            if drt == 1:
                lines[pos]=lines[pos]+s[i]
                pos = pos+1
                if pos ==numRows-1:
                    drt = 0
            elif drt ==0:
                lines[pos] = lines[pos]+s[i]
                pos = pos -1
                if pos==0:
                    drt = 1
        	
        res = ''
        for i in xrange(numRows):
        	# print lines[i]
        	res = res+ lines[i]
        return res


test = Solution()
print test.convert("AB", 1)

