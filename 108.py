from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return nums
    
        def create(nums):
            root = TreeNode()
            if not nums:
                return 
            mid = len(nums)//2
            root.val = nums[mid]
            root.left = create(nums[:mid])
            root.right = create(nums[mid+1:])
            return root
        return create(nums)
