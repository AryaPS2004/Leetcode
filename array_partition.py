class Solution(object):
    def arrayPairSum(self, nums):
        # max_sum=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         min_sum=min(nums[i],nums[j])
        #         max_sum=max(max_sum,min_sum)
        # return max_sum
        nums.sort()
        total=0
        for i in range(0,len(nums),2):
            total+=nums[i]
        return total

        
