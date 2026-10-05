import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero_counter = 1,0
        for num in nums:
            if num:
                product *= num
            else:
                zero_counter +=1
        
        if zero_counter > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i,c in enumerate(nums):
            if zero_counter:
                if c:
                    res[i] = 0
                else:
                    res[i] = product
            else:
                res[i] = product//c
        return res
            
            
            