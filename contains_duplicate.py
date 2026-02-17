class Solution(object):
    def containsDuplicate(self, nums):
        # for i in range(len(nums)):
        #     if nums.count(nums[i])>=2:
        #         return True
        # return False

        # seen=set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.add(i)
        # return False

        # fre={}
        # for i in nums:
        #     fre[i]=fre.get(i,0)+1
        #     if fre[i]>=2:
        #         return True
        # return False

        fre={}
        for i in nums:
            if i in fre:
                return True
            else:
                fre[i]=1
        return False
        
