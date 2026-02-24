class Solution(object):
    def dominantIndex(self, nums):
        largest=-1
        index=-1
        for i in range(len(nums)):
            if nums[i]>largest:
                largest=nums[i]
                index=i
        for i in range(len(nums)):
            if i!=index and largest<2*nums[i]:
                return -1
        return index


        
