class Solution(object):
    def removeDuplicates(nums):
        for i in nums:
            d = nums.count(i)
            if d == 1:
                pass
            else:
                for x in range(d - 1):
                    nums.remove(i)
        return len(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        
Solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])