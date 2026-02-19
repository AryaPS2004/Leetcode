class Solution(object):
    def findRestaurant(self, list1, list2):
        min_index=float('inf')
        res=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    a=i+j
                    if a<min_index:
                        min_index=a
                        res=[list1[i]]
                    elif a==min_index:
                        res.append(list1[i])
        return res
                        
