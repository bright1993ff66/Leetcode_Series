# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees_1(self, t1: TreeNode, t2: TreeNode) -> TreeNode: # Recursion
        if not t1 and not t2: return None
        if not t1: return t2
        if not t2: return t1
        root = TreeNode(val=t1.val+t2.val)
        root.left = self.mergeTrees_1(t1.left, t2.left)
        root.right = self.mergeTrees_1(t1.right, t2.right)
        return root

    def mergeTrees_2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        if not t1: return t2
        if not t2: return t1

        # new node val
        def nodeSum(node1, node2):
            if not node1:
                return node2.val
            if not node2:
                return node1.val
            return node1.val + node2.val

        root = TreeNode(t1.val + t2.val)
        queue = [[root, t1, t2]]

        while queue:
            t = queue.pop()
            if t[1] or t[2]:
                # left child
                n1 = t[1].left if t[1] else None
                n2 = t[2].left if t[2] else None
                if n1 or n2:
                    t[0].left = TreeNode(nodeSum(n1, n2))
                    queue.append([t[0].left, n1, n2])

                # right child
                n1 = t[1].right if t[1] else None
                n2 = t[2].right if t[2] else None
                if n1 or n2:
                    t[0].right = TreeNode(nodeSum(n1, n2))
                    queue.append([t[0].right, n1, n2])

        return root

