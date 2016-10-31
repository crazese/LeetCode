class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = {}
        for i in magazine:
            count[i] = count[i] +1 if i in count else 1
        for i in ransomNote:
            if i in count:
                count[i] = count[i]-1
                if count[i]<0:
                    return False
            else:
                return False

        return True
    

        
        
sol = Solution()
print sol.canConstruct("a", "b")