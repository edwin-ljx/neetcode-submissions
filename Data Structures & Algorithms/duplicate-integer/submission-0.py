class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_list = []
        for number in nums:
            if number not in unique_list:
                unique_list.append(number)
            else:
                return True
        return False