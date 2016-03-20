class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)>=0 and len(nums)<3:
        	return sum(nums)
    	res = []
        nums.sort()
        diff = nums[0]+nums[1]+nums[2]
    	for i in xrange(len(nums)):
            left = i+1
            right = len(nums)-1
            while left<right:
                sumNums = nums[i]+nums[left]+nums[right]
                if abs(sumNums-target)<abs(diff-target):
                    diff = sumNums
                if nums[left]+nums[right]+nums[i] == target:
                    return target
                elif nums[left]+nums[right]+nums[i]>target:
                    right = right -1
                elif nums[left]+nums[right]+nums[i]<target:
                    left = left+1
        return diff

test = Solution()
print test.threeSumClosest([-1,2],1)


