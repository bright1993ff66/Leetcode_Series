from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_set = set(nums)
        if len(nums_set) == 1: return 0
        num_counter = Counter(nums)
        max_count = 0
        for val in nums_set:
            if val+1 in nums_set and num_counter[val] + num_counter[val + 1] >= max_count:
                max_count  = num_counter[val] + num_counter[val + 1]
            elif val-1 in nums_set and num_counter[val] + num_counter[val - 1] >= max_count:
                max_count = num_counter[val] + num_counter[val - 1]
        return max_count

