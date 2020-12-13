# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree_1(self, root: TreeNode) -> TreeNode: # Recursion
        if not root: return None
        root.left, root.right = self.invertTree_1(root.right), self.invertTree_1(root.left)
        return root

    def invertTree_2(self, root: TreeNode) -> TreeNode: # Iteration
        if not root: return None
        queue = []
        queue.append(root)
        while queue:
            current = queue.pop(0)
            current.left, current.right = current.right, current.left
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)
        return root
