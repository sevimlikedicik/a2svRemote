from typing import Optional

from helper.TreeNode import TreeNode


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        paths = {root: [root]}
        queue = [root]

        while queue:
            copy_queue = list(queue)
            sub_queue = list(queue)
            queue = []
            while sub_queue:
                curr = sub_queue.pop(0)
                if curr.left is not None:
                    queue.append(curr.left)
                    paths[curr.left] = list(paths[curr] + [curr.left])
                if curr.right is not None:
                    queue.append(curr.right)
                    paths[curr.right] = list(paths[curr] + [curr.right])

        lca_paths = []
        for node in copy_queue:
            lca_paths.append(paths[node])

        for i in range(len(lca_paths[0]) - 1, -1, -1):
            curr_parents = set()
            for j in range(len(lca_paths)):
                curr_parents.add(lca_paths[j][i])
            if len(curr_parents) == 1:
                return list(curr_parents)[0]
