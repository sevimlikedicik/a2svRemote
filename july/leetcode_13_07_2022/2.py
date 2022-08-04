import math


class Solution:
    def fibonacci(self, n):
        fib = [1, 1]
        for i in range(2, n):
            fib.append((fib[i - 2] + fib[i - 1]) % int(math.pow(10, 9) + 7))
        return (fib[n - 1] * fib[n - 1]) % int(math.pow(10, 9) + 7)

    def countHousePlacements(self, n: int) -> int:
        return self.fibonacci(n+2)


sol = Solution()
print(sol.countHousePlacements(1000))
