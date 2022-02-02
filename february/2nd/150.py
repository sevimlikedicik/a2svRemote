from typing import List


class Solution:
    def add(self, stack):
        stack.append(stack.pop() + stack.pop())

    def subs(self, stack):
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(num1 - num2)

    def mult(self, stack):
        stack.append(stack.pop() * stack.pop())

    def div(self, stack):
        num2 = stack.pop()
        num1 = stack.pop()
        if num1 // num2 < 0 and num1 % num2 != 0:
            stack.append(num1 // num2 + 1)
        else:
            stack.append(num1 // num2)

    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': self.add,
            '-': self.subs,
            '*': self.mult,
            '/': self.div
        }

        stack = []

        for token in tokens:
            if token in operations:
                operations[token](stack)
            else:
                stack.append(int(token))

        return stack.pop()


sln = Solution()
print(sln.evalRPN(["4", "13", "5", "/", "+"]))
