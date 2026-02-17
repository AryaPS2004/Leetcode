class Solution(object):
    def majorityElement(self, nums):
        # n=len(nums)
        # for i in range(n):
        #     if nums.count(nums[i])>n//2:
        #         return nums[i]
        n=len(nums)
        fre={}
        for i in nums:
            fre[i]=fre.get(i,0)+1

            if fre[i]>n//2:
                return i
        
