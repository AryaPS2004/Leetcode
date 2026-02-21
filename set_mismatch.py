class Solution(object):
    def findErrorNums(self, nums):
        fre={}
        for i in nums:
            fre[i]=fre.get(i,0)+1
        dup=-1
        miss=-1
        for i in range(1,len(nums)+1):
            if i in fre:
                if fre[i]==2:
                    dup=i
            else:
                miss=i
        return [dup,miss]


        
