class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_list = sorted(list(set(nums)))
        best = 0
        temp = 0
        for i,value in enumerate(sorted_list):
            if i == 0:
                temp += 1
            elif value == sorted_list[i-1] + 1:
                temp += 1
            else:
                temp = 1

            if temp >= best:
                best = temp
        return best
