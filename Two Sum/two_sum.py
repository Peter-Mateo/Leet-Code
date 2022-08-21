class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for a in range(len(nums)):
                if i == a:
                    continue
                check = nums[i] + nums[a]
                if check == target:
                    return (i, a)
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        