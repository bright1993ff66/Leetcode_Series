from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder_bfs(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        result, queue = [], [root]
        while queue:
            cur_size = len(queue)
            tmp = []
            for _ in range(cur_size):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(tmp)
        return result

    def levelOrder_dfs(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, node, cur_level):
        if not node: return
        if len(self.result) < cur_level + 1:
            self.result.append([])
        self.result[cur_level].append(node.val)
        self._dfs(node.left, cur_level+1)
        self._dfs(node.right, cur_level+1)
