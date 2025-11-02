class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i in range(len(nums)):
            num=nums[i]
            diff=target-num
            if diff in dic:
                return [i,dic[diff]]
            dic[num]=i    
