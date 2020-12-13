from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        val_dict = {}
        for index, val in enumerate(nums):
            other = target - val
            if other not in val_dict:
                val_dict[val] = index
            else:
                return [val_dict[other], index]
        return []

    def twoSum_167(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        # while the left pointer is not crossing the right pointer
        while (left < right):
            if (numbers[left] + numbers[right] == target):
                return [left + 1, right + 1]
            elif (numbers[left] + numbers[right] < target):
                left += 1
            else:
                right -= 1
        return []

    def twoSum_653(self, root: TreeNode, k: int) -> bool:
        self.inorder_list = []
        self.inorder(root)
        left, right = 0, len(self.inorder_list) - 1
        while (left < right):
            if (self.inorder_list[left] + self.inorder_list[right] == k):
                return True
            elif (self.inorder_list[left] + self.inorder_list[right] < k):
                left += 1
            else:
                right -= 1
        return False

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.inorder_list.append(node.val)
            self.inorder(node.right)


if __name__ == '__main__':
    check_solutions = Solution()
    result = check_solutions.twoSum_1(nums = [3,2,4], target = 6)
    print(result)


