# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.result = True
        self.max_level(root)
        return self.result

    def max_level(self, node) -> int:
        if not node: return 0
        left_level = self.max_level(node.left)
        right_level = self.max_level(node.right)
        if abs(left_level - right_level) > 1:
            self.result = False
            return self.result
        return 1 + max(left_level, right_level)

