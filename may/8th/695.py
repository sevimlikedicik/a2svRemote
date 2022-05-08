from typing import List


class Solution:
    def dfs(self, grid, row, col, neighbors):
        grid[row][col] = 0
        total = 1
        for add_r, add_c in neighbors:
            new_r = row + add_r
            new_c = col + add_c
            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 1:
                total += self.dfs(grid, new_r, new_c, neighbors)

        return total

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
        neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for row, row_val in enumerate(grid):
            for col, col_val in enumerate(row_val):
                if col_val == 1:
                    max_island = max(max_island, self.dfs(grid, row, col, neighbors))

        return max_island
