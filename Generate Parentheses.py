class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.generateTemp(n,n,'',[])
        return self.res

    def generateTemp(self,left, right, s, res):
        if left == 0 and right ==0:
            res.append(s)
            self.res = res
            return 

        if left >0:
            self.generateTemp(left-1,right,s+'(',res)

        if left<right:
            self.generateTemp(left,right-1,s+')',res)
