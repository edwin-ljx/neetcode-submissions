class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sum_dict = {}
        for number in nums:
            if number not in sum_dict:
                sum_dict[number] = 1
            else:
                sum_dict[number] = sum_dict[number] + 1
        
        output = heapq.nlargest(k, sum_dict.items(), key=lambda x: x[1])
        final = []
        for key,values in output:
            final.append(key)
        return final