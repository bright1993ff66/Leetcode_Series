from typing import List
import heapq

class Solution:
    def longestConsecutive_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_count = 1
        max_count = 1
        if not nums: return 0
        heapq.heapify(nums)
        prev = heapq.heappop(nums)
        while nums:
            tmp = heapq.heappop(nums)
            if tmp - prev == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            elif tmp - prev > 0:
                current_count = 1
            prev = tmp
        return max_count

    def longestConsecutive_2(self, nums):
        longest_streak = 1
        nums_set = set(nums)

        if len(nums_set) == 0: return 0

        current_streak = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in nums_set:
                    current_streak += 1
                    current_num += 1

                longest_streak = max(current_streak, longest_streak)

        return max(current_streak, longest_streak)