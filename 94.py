from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        list = []
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            list.append(root.val)
            traverse(root.right)
        traverse(root)
        return list
