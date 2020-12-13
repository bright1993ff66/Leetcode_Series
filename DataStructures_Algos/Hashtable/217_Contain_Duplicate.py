from typing import List

class Solution:
    def containsDuplicate_217(self, nums: List[int]) -> bool:
        if not nums: return False
        return len(set(nums)) != len(nums)

    def containsDuplicate_219(self, nums: List[int], k: int) -> bool:
        """
        Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the
        array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
        :param nums:
        :return:
        """
        if not nums: return False
        val_dict = {}
        for index, num in enumerate(nums):
            if num in val_dict and abs(index - val_dict[num]) <= k:
                return True
            val_dict[num] = index
        return False
