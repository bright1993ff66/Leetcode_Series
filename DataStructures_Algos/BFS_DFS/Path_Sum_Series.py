from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum_112(self, root: TreeNode, sum: int) -> bool:
        """
        Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the
        values along the path equals the given sum.
        Note: A leaf is a node with no children.
        :param root: a Tree Node
        :param sum: a specified sum value
        :return: whether a tree has a desired path or not
        """
        if not root: return False

        sum -= root.val

        # only check sum if it is a leaf node
        if (not root.left) and (not root.right):
            if sum == 0:
                return True
            return False

        return self.hasPathSum_112(root.left, sum) or self.hasPathSum_112(root.right, sum)

    def pathSum_113(self, root: TreeNode, sum: int):
        """
        Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
        Note: A leaf is a node with no children.
        :param root:
        :param sum:
        :return:
        """
        result, stack = [], []
        if root:
            stack.append((root, root.val, [root.val]))

        while stack:
            cur_node, running_sum, values = stack.pop()
            if not cur_node.left and not cur_node.right and running_sum == sum:
                result.append(values)
            if cur_node.left:
                stack.append((cur_node.left, running_sum + cur_node.left.val, values + [cur_node.left.val]))
            if cur_node.right:
                stack.append((cur_node.right, running_sum + cur_node.right.val, values + [cur_node.right.val]))

        return result

    def pathSum(self, root: TreeNode, sum: int) -> int:
        """
        You are given a binary tree in which each node contains an integer value.
        Find the number of paths that sum to a given value.
        The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent
        nodes to child nodes).
        The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
        :param root:
        :param sum:
        :return:
        """
        if root:
            c = self.help_sum(root, sum)  # start from the root
            l = self.pathSum(root.left, sum)  # inside the left subtree
            r = self.pathSum(root.right, sum)  # inside the right subtree
            return c + l + r
        return 0

    def help_sum(self, root, sum):
        if root:
            l = self.help_sum(root.left, sum - root.val)
            r = self.help_sum(root.right, sum - root.val)
            return l + r + (root.val == sum)
        return 0




