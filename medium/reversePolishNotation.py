from socket import AI_PASSIVE
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second)) # truncate towards zero
            elif token == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            else:
                stack.append(int(token))

        return stack.pop()
        
        