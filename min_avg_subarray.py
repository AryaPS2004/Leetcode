class Solution(object):
    def findMaxAverage(self, nums, k):
        wind_sum=sum(nums[:k])
        max_sum=wind_sum
        for i in range(k,len(nums)):
            wind_sum+=nums[i]-nums[i-k]
            max_sum=max(max_sum,wind_sum)
        return float(max_sum)/k

        
