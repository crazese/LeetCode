class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        return re.match('^' + p + '$', s) != None