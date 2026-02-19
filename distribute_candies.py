class Solution(object):
    def distributeCandies(self, candyType):
        unique=len(set(candyType))
        max_eatable=len(candyType)//2
        return min(unique,max_eatable)

        
