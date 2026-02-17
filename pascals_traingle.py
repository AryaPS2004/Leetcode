class Solution(object):
    def generate(self, numRows):
        a=[[1]]
        for i in range(numRows-1):
            temp=[0]+a[-1]+[0]
            rows=[]
            for j in range(len(a[-1])+1):
                rows.append(temp[j]+temp[j+1])
            a.append(rows)
        return a


        
