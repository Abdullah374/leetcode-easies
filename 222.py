from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # node = []
        # def traverse(root):
        #     if root is None:
        #         return
        #     node.append(root.val)
        #     traverse(root.left)
        #     traverse(root.right)
        # traverse(root)
        # return len(node)
        def traverse(root):
            if root is None:
                return 0
            
            return 1 + traverse(root.left) + traverse(root.right)
        
        return traverse(root)
            
        
