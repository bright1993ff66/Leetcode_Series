from typing import List


class Solution:
    def nextGreaterElement_496(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 and not nums2: return []
        nums1_index_dict = {}
        for index, num in enumerate(nums1):
            nums1_index_dict[num] = index
        stack = []
        res = [-1 for _ in range(len(nums1))]
        for index, val in enumerate(nums2):
            while stack and val > stack[-1]:
                pop_val = stack.pop()
                res[nums1_index_dict[pop_val]] = val
            if val in nums1:
                stack.append(val)
        return res

    def nextGreaterElements_503(self, nums: List[int]) -> List[int]:
        pass