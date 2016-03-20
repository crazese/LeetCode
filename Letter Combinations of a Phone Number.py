class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #       [2,     3,    4,    5,    6,    7,     8,    9]
        code = ['abc','def','ghi','jkl','mno','pgrs','tuv','wxyz']
        if len(digits) ==0:
            return []
        elif len(digits) == 1:
            return list(code[int(digits)-2])
        elif len(digits) == 2:
            list1 = list(code[int(digits[0])-2])
            list2 = list(code[int(digits[1])-2])
            print list1,list2
            return self.combination(list1,list2)
        else:
            list1 = list(code[int(digits[0])-2])
            list2 = self.letterCombinations(digits[1:])
            return self.combination(list1,list2)

    def combination(self,list1,list2):
        list3 = []
        for i in list1:
            for j in list2:
                list3.append(i+j)
        return list3
test = Solution()
print test.letterCombinations('234')