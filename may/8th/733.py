from typing import List


class Solution:
    def dfs(self, image, r, c, og_color, new_color, visited, neighbors):
        image[r][c] = new_color
        visited.add((r, c))
        for add_r, add_c in neighbors:
            new_r = r + add_r
            new_c = c + add_c
            if 0 <= new_c < len(image[0]) and 0 <= new_r < len(image) and (new_r, new_c) not in visited and \
                    image[new_r][new_c] == og_color:
                self.dfs(image, new_r, new_c, og_color, new_color, visited, neighbors)

        return

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()
        self.dfs(image, sr, sc, image[sr][sc], newColor, visited, neighbors)
        return image
