class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_list = sorted(nums)
        if sorted_list[0] >0:
            return []
        res = set()
        for i,val in enumerate(sorted_list):
            if i <= len(sorted_list) - 3:
                left = i+1
                right = len(sorted_list) - 1
                while left != right:
                    if val + sorted_list[left] + sorted_list[right] == 0:
                        res.add((val,sorted_list[left],sorted_list[right]))
                        left += 1
                    elif val + sorted_list[left] + sorted_list[right] > 0:
                        right -= 1
                    else:
                        left += 1    
        return [list(t) for t in res]

            