class Solution(object):
    def removeElement(self, nums, val):
        # k=0
        # for i in range(len(nums)):
        #     if nums[i]!=val:
        #         nums[k]=nums[i]
        #         k+=1
        # return k
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==val:
                nums.pop(i)
        return len(nums)
        
