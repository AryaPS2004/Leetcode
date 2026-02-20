class Solution(object):
    def maximumProduct(self, nums):
        # nums.sort()
        # max_p=nums[0]*nums[1]*nums[2]
        # for i in range(len(nums)-2):
        #     p=nums[i]*nums[i+1]*nums[i+2]
        #     if p>max_p:
        #         max_p=p

        # return max_p


        # nums.sort()
        # max_p=nums[0]*nums[1]*nums[2]
        # for i in range(len(nums)-2):
        #     p=nums[i]*nums[i+1]*nums[i+2]
        #     max_p=max(p,max_p)
        # max_p=max(max_p,nums[0]*nums[1]*nums[-1])

        # return max_p

        max1=max2=max3=float('-inf')
        min1=min2=float('inf')

        for i in nums:
            if i>max1:
                max3=max2
                max2=max1
                max1=i
            elif i>max2:
                max3=max2
                max2=i
            elif i>max3:
                max3=i
            if i<min1:
                min2=min1
                min1=i
            elif i<min2:
                min2=i
        return max(max1*max2*max3,max1*min1*min2)


        
