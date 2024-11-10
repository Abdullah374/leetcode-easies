from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return 0
            
            left_depth = height(root.left)
            right_depth = height(root.right)
            if left_depth == -1 or right_depth == -1:
                return -1
            
            if abs(left_depth - right_depth) > 1:
                return -1
            
            return 1 + max(left_depth, right_depth)
        return height(root) != -1