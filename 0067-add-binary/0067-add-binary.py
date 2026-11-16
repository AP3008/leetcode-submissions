class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        # Will have to reverse string on return 
        res = []
        carry = 0
        while a and b:
            aBit = int(a.pop())
            bBit = int(b.pop())
            bitSum = aBit + bBit + carry
            carry = bitSum//2
            res.append(str(bitSum%2))
            
        while a:
            rest = int(a.pop()) + carry
            carry = rest//2
            res.append(str(rest%2))
        while b:
            rest = int(b.pop()) + carry
            carry = rest//2
            res.append(str(rest%2))
        if carry == 1:
            res.append("1")
        return "".join(reversed(res))

