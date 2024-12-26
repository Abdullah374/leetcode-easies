from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(image), len(image[0])
        q = deque([(sr, sc)])
        original = image[sr][sc]
        if original == color:
            return image
        image[sr][sc] = color
        

        while q:
            row, col = q.popleft()
            for dx, dy in directions:
                nx, ny = row + dx, col + dy
                
                if 0 <= nx < m and 0 <= ny < n and image[nx][ny] == original:
                    image[nx][ny] = color
                    q.append((nx,ny))
        return image