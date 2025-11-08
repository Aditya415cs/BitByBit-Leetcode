class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst = []
        for i in range(len(nums)):
            prefix = set(nums[0:i+1])
            suffix = set(nums[i+1:len(nums)])
            diff = len(prefix) - len(suffix)
            lst.append(diff)
        return lst
