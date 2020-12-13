# encoding = utf-8
from sys import maxsize
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        """
        Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of
        any two different nodes in the tree.
        :param root:
        :return:
        """
        self.traverse_path = []
        self.inorder(root)
        min_result = maxsize
        for index in range(1, len(self.traverse_path)):
            if self.traverse_path[index] - self.traverse_path[index-1] <= min_result:
                min_result = self.traverse_path[index] - self.traverse_path[index-1]
        return min_result


    def minDiffInBST_Iteration(self, root: TreeNode) -> int:
        pass


    def minDiffInBST_Recursion(self, root: TreeNode) -> int:
        res = []
        def helper(node, prev, min_val):
            if min_val == 1:
                return True
            if not node:
                return False
            res.append(node.val)
            return helper(node.left, node.val, min(min_val, abs(node.val-prev))) or helper(
                node.right, node.val, min(min_val, abs(node.right-prev))
            )
        if helper(root, root.val, maxsize):
            return 1
        res.sort()
        return min(res[i+1] - res[i] for i in range(len(res) - 1))

    def minDiffInBST_heap(self, root: TreeNode) -> int:
        h = []
        cur = root
        q = []

        while cur or q:
            while cur:
                q.append(cur)
                cur = cur.left

            cur = q.pop()
            heapq.heappush(h, cur.val)
            cur = cur.right

        return min(y - x for x, y in zip(h, h[1:]))



    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.traverse_path.append(node.val)
            self.inorder(node.right)
