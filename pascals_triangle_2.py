class Solution(object):
    def getRow(self, rowIndex):
        a=[[1]]
        for i in range(rowIndex):
            temp=[0]+a[-1]+[0]
            rows=[]
            for j in range(len(a[-1])+1):
                rows.append(temp[j]+temp[j+1])
            a.append(rows)
        return a[-1]
        
