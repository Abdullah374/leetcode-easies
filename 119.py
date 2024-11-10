from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1] * (i+1) for i in range(rowIndex+1)]

        for i in range(2, rowIndex+1):
            dp[i][1:len(dp[i-1])] = [dp[i-1][j-1] + dp[i-1][j] for j in range(1,i) ]

        return dp[rowIndex]