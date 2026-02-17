class Solution(object):
    def missingNumber(self, nums):
        total=0
        n=len(nums)
        sums=n*(n+1)//2
        for i in range(n):
            total+=nums[i]
            i+=1
        return sums-total
