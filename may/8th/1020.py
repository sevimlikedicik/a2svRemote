from typing import List


class Solution:
    def surrounded(self, grid, row, col, neighbors, local_visited):
        # print(row, col)
        if 0 > row or row >= len(grid) or 0 > col or col >= len(grid[0]):
            return False

        if grid[row][col] != 1 or (row, col) in local_visited:
            return True

        local_visited.add((row, col))
        surr = True

        for add_r, add_c in neighbors:
            new_r = row + add_r
            new_c = col + add_c
            surr = surr and self.surrounded(grid, new_r, new_c, neighbors, local_visited)

        return surr

    def numEnclaves(self, grid: List[List[int]]) -> int:
        neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()
        total_area = 0
        for row, row_val in enumerate(grid):
            for col, col_val in enumerate(row_val):
                if (row, col) not in visited and col_val == 1:
                    local_visited = set()
                    if self.surrounded(grid, row, col, neighbors, local_visited):
                        total_area += len(local_visited)
                    for r, c in local_visited:
                        visited.add((r, c))

        return total_area
