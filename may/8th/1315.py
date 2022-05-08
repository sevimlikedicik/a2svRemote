from helper.TreeNode import TreeNode


class Solution:
    def magic(self, grand_even, dad_even, myself):
        if myself is None:
            return 0

        sub_total = 0
        if grand_even:
            sub_total += myself.val

        return sub_total + self.magic(dad_even, myself.val % 2 == 0, myself.left) + self.magic(dad_even,
                                                                                               myself.val % 2 == 0,
                                                                                               myself.right)

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.magic(False, False, root)
