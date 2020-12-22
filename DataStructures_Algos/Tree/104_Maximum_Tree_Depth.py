# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int: # DFS with recursion
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth_bfs(self, root: TreeNode) -> int: # BFS
        if not root: return 0
        depth, level = 0, [root]
        while level:
            depth += 1
            queue = []
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level = queue
        return depth

    def maxDepth_dfs(self, root: TreeNode) -> int:
        if not root: return 0
        max_depth, stack = 1, [root]
        pass
        # while stack:
        #     for _ in range(len(stack)):
        #         node = stack.pop(-1)
        #         if self.isLeaf(node):
        #
        #         if node.left:
        #             stack.append(node.left)
        #         if node.right:
        #             stack.append(node.right)
        #     if cur_depth > max_depth:
        #         max_depth = cur_depth
        # return max_depth

    def children(self, node):
        if self.isLeaf(node): return []
        children_list = []
        if node.left:
            children_list.append(node.left)
        if node.right:
            children_list.append(node.right)
        return children_list

    def isLeaf(self, node):
        return not node.left and not node.right
