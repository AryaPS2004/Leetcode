class Solution(object):
    def findLHS(self, nums):
        fre={}
        for i in nums:
            fre[i]=fre.get(i,0)+1
        max_c=0
        for j in fre:
            if j+1 in fre:
                length=fre[j]+fre[j+1]
                max_c=max(max_c,length)
        return max_c
