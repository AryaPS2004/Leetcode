class Solution(object):
    def pivotIndex(self, nums):
        total=sum(nums)
        sumleft=0
        for i in range(len(nums)):
            sumright=total-sumleft-nums[i]
            if sumleft==sumright:
                return i
            sumleft+=nums[i]
        return -1
        # n=len(nums)
        # leftsum=[0]*n
        # rightsum=[0]*n
        # for i in range(1,n):
        #     leftsum[i]=leftsum[i-1]+nums[i-1]
        # for i in range(n-2,-1,-1):
        #     rightsum[i]=rightsum[i+1]+nums[i+1]

        # for i in range(n):
        #     if leftsum[i]==rightsum[i]:
        #         return i
        # return -1
        
