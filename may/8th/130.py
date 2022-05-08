from typing import List


class Solution:
    def surrounded(self, grid, row, col, neighbors, local_visited):
        if 0 > row or row >= len(grid) or 0 > col or col >= len(grid[0]):
            return False

        if grid[row][col] != 'O' or (row, col) in local_visited:
            return True

        local_visited.add((row, col))
        surr = True

        for add_r, add_c in neighbors:
            new_r = row + add_r
            new_c = col + add_c
            surr = surr and self.surrounded(grid, new_r, new_c, neighbors, local_visited)

        return surr

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()
        for row, row_val in enumerate(board):
            for col, col_val in enumerate(row_val):
                if (row, col) not in visited and col_val == 'O':
                    local_visited = set()
                    if self.surrounded(board, row, col, neighbors, local_visited):
                        for r, c in local_visited:
                            board[r][c] = 'X'
                    for r, c in local_visited:
                        visited.add((r, c))
