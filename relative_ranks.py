class Solution(object):
    def findRelativeRanks(self, score):
        k=sorted(score,reverse=True)
        ranks={}
        for i in range(len(k)):
            if i==0:
                ranks[k[i]]="Gold Medal"
            elif i==1:
                ranks[k[i]]="Silver Medal"
            elif i==2:
                ranks[k[i]]="Bronze Medal"
            else:
                ranks[k[i]]=str(i+1)

        res=[]
        for s in score:
            res.append(ranks[s])
        return res



            

