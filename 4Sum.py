class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        l = len(nums)
        d = {}
        res = set()
        for i in xrange(l-1):
            for j in xrange(i+1,l):
                temp = nums[i]+nums[j]
                if temp not in d:
                    d[temp] = [(i,j)]
                else:
                    d[temp].append((i,j))
        
        for i in xrange(l):
            for j in xrange(i+1,l-2):
                temp2 = target - nums[i] - nums[j]
                if temp2 in d:
                    for k in d[temp2]:
                        if k[0]>j:
                            res.add((nums[i],nums[j],nums[k[0]],nums[k[1]]))

        return [i for i in res]




    
test = Solution()
print test.fourSum([1 ,0 ,-1 ,0 ,-2 ,2],0)
        