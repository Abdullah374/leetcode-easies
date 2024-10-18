from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # list = []
        
        # list.append(float(root.val))

        # def average(root):
        #     if root.left and root.right:
        #         avg = (root.left.val + root.right.val)/2
        #         list.append(avg)
        #         average(root.left)
        #         average(root.right)
        #     elif root.left:
        #         list.append(float(root.left.val))
        #         average(root.left)
        #     elif root.right:
        #         list.append(float(root.right.val))
        #         average(root.right)
        #     else:
        #         return
        # average(root)
        # return list


        if not root:
            return []
        
        result = []
        queue = deque([root])  # Initialize the queue with the root node
        
        while queue:
            level_sum = 0
            level_size = len(queue)  # Number of nodes at the current level
            
            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()  # Dequeue the front node
                level_sum += node.val   # Add its value to the level sum
                
                # Enqueue the left and right children (if they exist)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Calculate the average for the current level
            result.append(level_sum / level_size)
        
        return result
