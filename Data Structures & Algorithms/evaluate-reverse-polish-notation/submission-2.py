import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst = []
        ops = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : lambda x, y: int(x / y)
        }
        for c in tokens:
            if c not in ops:
                lst.append(int(c))
            else:
                poped1 = lst.pop()
                poped2 = lst.pop()
                res    = ops[c](poped2, poped1) 
                lst.append(res)  
        return lst.pop()