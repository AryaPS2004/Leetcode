class Solution(object):
    def thirdMax(self, nums):
        first=sec=third=None
        for i in nums:
            if i==first or i==sec or i==third:
                continue
            if first is None or i>first:
                third=sec
                sec=first
                first=i
            elif sec is None or i>sec:
                third=sec
                sec=i
            elif third is None or i>third:
                third=i
        if third is None:
            return first
        return third
