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

    def max_level(self, node):
        if not node: return 0
        left_level = self.max_level(node.left)
        right_level = self.max_level(node.right)
        if abs(left_level - right_level) > 1:
            self.result = False
            return self.result
        # The question is asking the level of subtrees. Hence both left and right should be considered
        return 1 + max(left_level, right_level)


