# encoding = utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        """
        Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range
        [low, high].
        :param root: a TreeNode
        :param low: lower bound
        :param high: upper bound
        :return:
        """
        self.traverse_path = []
        self.inorder(root)
        return sum(filter(lambda x: low<=x<=high, self.traverse_path))

    def rangeSumBST_Recursion(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.ans += node.val
                if low < node.val:
                    dfs(node.left)
                if high > node.val:
                    dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans

    def rangeSumBST_Iteration(self, root: TreeNode, low: int, high: int) -> int:
        stack = [root] # Use stack to maintain the visits
        ans = 0
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if high > node.val:
                    stack.append(node.right)
        return ans

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.traverse_path.append(root.val)
            self.inorder(root.right)

