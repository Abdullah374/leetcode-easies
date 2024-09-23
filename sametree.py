from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        list1 = []
        def traversep(node):
            if node is None:
                list1.append('null')
                return
            list1.append(node.val)
            traversep(node.left)
            traversep(node.right)
        list2 = []
        def traverseq(node):
            if node is None:
                list2.append('null')
                return
            list2.append(node.val)
            traverseq(node.left)
            traverseq(node.right)
        traversep(p)
        traverseq(q)
        return list1 == list2   