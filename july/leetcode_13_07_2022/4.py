from typing import List


class Solution:
    def get_xor_vals(self, nums, adj_map, xor_vals, visited, node):
        xor_vals[node] = nums[node]
        visited.add(node)
        for child in adj_map[node]:
            if child not in visited:
                xor_vals[node] = xor_vals[node] ^ self.get_xor_vals(nums, adj_map, xor_vals, visited, child)

        return xor_vals[node]

    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        adj_map = {}
        for x, y in edges:
            if x not in adj_map:
                adj_map[x] = []
            adj_map[x].append(y)
            if y not in adj_map:
                adj_map[y] = []
            adj_map[y].append(x)

        xor_vals = {}
        visited = set()
        self.get_xor_vals(nums, adj_map, xor_vals, visited, 0)
        self.clean_map(adj_map, 0)
        visited = set()
        return self.get_min_xor_diff(xor_vals, adj_map, visited, 0)

    def get_min_xor_diff(self, xor_vals, adj_map, visited, node):
        visited.add(node)
        comp_1, comp_2, comp_3 = xor_vals[node], xor_vals[node], xor_vals[node]
        for child in adj_map[node]:
            comp_1 = comp_1 ^ xor_vals[child]
            visited.add(child)
            for gc in adj_map[child]:
                return 0

    def clean_map(self, adj_map, node):
        for child in adj_map[node]:
            adj_map[child].remove(node)
            self.clean_map(adj_map, child)


sol = Solution()
print(sol.minimumScore([5, 5, 2, 4, 4, 2], [[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]]))
print(sol.minimumScore([1, 5, 5, 4, 11], [[0, 1], [1, 2], [1, 3], [3, 4]]))
