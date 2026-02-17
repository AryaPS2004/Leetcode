class Solution(object):
    def singleNumber(self, nums):  
        # for i in range(len(nums)):
        #     if nums.count(nums[i])==1:
        #         return nums[i]

        
        # for i in range(len(nums)):
        #     cnt=0
        #     for j in range(len(nums)):
        #         if nums[i]==nums[j]:
        #             cnt+=1
        #     if cnt==1:
        #         return nums[i]


        cnt=0
        for i in nums:
            cnt^=i
        return cnt


