class Solution(object):
    def searchInsert(self, nums, target):
        # for i in range(len(nums)):
        #     if nums[i]>=target:
        #         return i
        # return len(nums)
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return l

           

