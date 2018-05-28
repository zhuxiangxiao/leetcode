# coding:utf-8
'''
    Example: Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict={}
        for x in xrange(len(nums)):
            if nums[x] in dict:
                return [dict[nums[x]],x]
            else:
                dict[(target-nums[x])]=x
        
nums = [2, 6, 1, 8, 11, 15]
target = 9
print Solution().twoSum(nums, target)