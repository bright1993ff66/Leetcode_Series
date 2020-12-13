class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_val = 0
        self.Depth(root)
        return self.max_val

    def Depth(self, node: TreeNode):
        if not node: return 0
        left_depth = self.Depth(node.left)
        right_depth = self.Depth(node.right)
        self.max_val = max(self.max_val, left_depth + right_depth)
        return max(left_depth, right_depth) + 1
