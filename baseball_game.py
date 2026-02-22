class Solution(object):
    def calPoints(self, operations):
        res=[]
        for i in operations:
            if i=="+":
                a=res[-1]+res[-2]
                res.append(a)
            elif i=="C":
                res.pop()
            elif i=="D":
                b=2*res[-1]
                res.append(b)
            else:
                res.append(int(i))
        return sum(res)

            
        
