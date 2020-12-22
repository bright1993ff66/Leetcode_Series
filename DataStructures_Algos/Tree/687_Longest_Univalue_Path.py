# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:

        answer = 0

        def caller(node):
            nonlocal answer

            if not node: return 0

            # divide and conquer
            leftLength = caller(node.left)
            rightLength = caller(node.right)

            leftSide, rightSide = 0, 0

            if node.left and node.val == node.left.val:
                leftSide = leftLength + 1
            if node.right and node.val == node.right.val:
                rightSide = rightLength + 1

            answer = max(answer, leftSide + rightSide)

            return max(0, max(rightSide, leftSide))

        caller(root)
        return answer