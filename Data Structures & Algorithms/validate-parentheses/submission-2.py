import collections

class Solution:
    def isValid(self, s: str) -> bool:

        mapping = { ")": "(", "]": "[", "}": "{" }
        stack = collections.deque()
        for i,c in enumerate(s) :
            if c in "[({":
                stack.append(c)
            else:
                if not stack or mapping[c] != stack.pop() :
                    return False

        return len(stack) == 0