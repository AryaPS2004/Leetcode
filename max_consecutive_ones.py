class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt=0
        max_c=0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
                max_c=max(max_c,cnt)
            else:
                cnt=0
        return max_c
