from typing import List


class Solution:
    def dfs(self, isConnected, i, visited):
        visited.add(i)
        for j, val in enumerate(isConnected[i]):
            if j not in visited and val == 1:
                self.dfs(isConnected, j, visited)

        return 1

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        province_count = 0

        for i in range(len(isConnected)):
            if i not in visited:
                self.dfs(isConnected, i, visited)
                province_count += 1

        return province_count
