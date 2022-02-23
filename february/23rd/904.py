from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        left, right, max_size = 0, 0, 0

        while right < len(fruits):
            if fruits[right] not in basket:
                basket[fruits[right]] = 0
            basket[fruits[right]] += 1

            if len(basket) > 2:
                while len(basket) > 2:
                    basket[fruits[left]] -= 1
                    if basket[fruits[left]] == 0:
                        del basket[fruits[left]]
                    left += 1

            max_size = max(max_size, right - left + 1)
            right += 1

        return max_size
