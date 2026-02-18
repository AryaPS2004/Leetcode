class Solution(object):
    def intersect(self, nums1, nums2):
        # res=[]
        # for i in nums1:
        #     if i in nums2:
        #         res.append(i)
        # return res
        fre={}
        res=[]
        for i in nums1:
            fre[i]=fre.get(i,0)+1
        for i in nums2:
            if i in fre and fre[i]>0:
                res.append(i)
                fre[i]-=1
        return res
