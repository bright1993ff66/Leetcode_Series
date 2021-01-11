# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool: # recursive
        if not root: return True
        return self.checkSymmetric(root.left, root.right)

    def isSymmetric_2(self, root: TreeNode) -> bool: # Iterative
        if not root: return True
        stack = [root]
        while len(stack):
            temp, comp = [], []
            size = len(stack)
            for _ in range(size):
                top = stack.pop()
                if top.left: temp.append(top.left)
                if top.right: temp.append(top.right)
                comp.append(top.left and top.left.val)
                comp.append(top.right and top.right.val)
            if not self.compare(comp): return False
            stack = temp
        return True

    def checkSymmetric(self, node1, node2):
        if not node1 and not node2: return True
        if (not node1 and node2) or (not node2 and node1): return False
        if node1.val != node2.val: return False
        return self.checkSymmetric(node1.left, node2.right) and self.checkSymmetric(node1.right, node2.left)

    def compare(self, node_list):
        start, end = 0, len(node_list) - 1
        while start < end:
            if node_list[start] != node_list[end]: return False
            start += 1
            end -= 1
        return True



