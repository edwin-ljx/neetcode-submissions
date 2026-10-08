class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index1,value1 in enumerate(numbers):
            value2 = target - value1

            if value2 in seen:
                return [seen[value2] + 1, index1 + 1]
            
            seen[value1] = index1