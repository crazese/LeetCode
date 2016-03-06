class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        res = 0
        left = 0
        d = {}

        for i, ch in enumerate(s):
            if ch in d and d[ch] >= left:
                left = d[ch] + 1
            d[ch] = i
            print d,i,ch,left,i-left+1
            res = max(res, i - left + 1)
        return res

# test = Solution()
# print test.lengthOfLongestSubstring("aab")