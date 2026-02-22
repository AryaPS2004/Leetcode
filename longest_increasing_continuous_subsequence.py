class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        l=0
        max_len=1
        for r in range(1,len(nums)):
            if nums[r]<=nums[r-1]:
                l=r
            max_len=max(max_len,r-l+1) 

        return max_len 
