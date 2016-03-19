class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or strs[0] == '':
        	return ''
        elif len(strs) == 1:
        	return strs[0]
        length  = len(strs[0])
        res = strs[0]
        for i in xrange(len(strs)):
        	if strs[i] == '':
        		return ''
        	if len(strs[i])<length:
        		length = len(strs[i])
        		res = res[0:length]
        	for j in xrange(length):
        		if strs[i][j]!=strs[0][j]:
        			res = res[0:j]
        			break
        return res

test = Solution()
print test.longestCommonPrefix(['aa','a'])





