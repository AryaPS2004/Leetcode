class Solution(object):
    def intersection(self, nums1, nums2):
        # res=[]
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i]==nums2[j] and nums1[i] not in res:
        #             res.append(nums1[i])

        # return res
        res=set()
        nums_2=set(nums2)

        for i in nums1:
            if i in nums_2:
                res.add(i)
        return list(res)
        
