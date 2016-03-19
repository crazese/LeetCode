class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.resAll = []
        if len(nums)>=0 and len(nums)<3:
            return (self.resAll)
        nums.sort()

        l = len(nums)
        for i in xrange(l):
            if i>0 and nums[i] == nums[i-1]:
                continue
            self.twoSum(nums[i+1:], -1*nums[i])
        return self.resAll

    def twoSum(self, nums, target):
        left = 0
        right = len(nums)-1
        
        while left<right:
            res = []
            if nums[left]+nums[right] == target:
                res.append(-1*target)
                res.append(nums[left])
                res.append(nums[right])
                self.resAll.append(res)
                while left<right and nums[left]==nums[left+1]:
                    left = left + 1
                while left <right and nums[right] == nums[right-1]:
                    right = right -1
                right = right -1
                left = left +1
            elif nums[left]+nums[right]>target:
                right = right - 1
            elif nums[left]+nums[right]<target:
                left = left + 1

        return self.resAll

test = Solution()
print test.threeSum([0,0,0,0])
