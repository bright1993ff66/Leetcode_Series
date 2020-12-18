# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        # Cope with the case: [2,null,3,null,4,null,5,null,6]
        if not left or not right: return left + right + 1

        return min(left, right) + 1
