class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)
        out_len = max(a_len, b_len)

        carry = 0
        out = []
        for i in range(out_len):
            if i < a_len:
                carry += int(a[a_len - i - 1])
            if i < b_len:
                carry += int(b[b_len - i - 1])

            if carry == 3:
                carry = 1
                out.append("1")
            elif carry == 2:
                carry = 1
                out.append("0")
            elif carry == 1:
                out.append("1")
                carry = 0
            else:
                out.append("0")
                carry = 0

        if carry == 1:
            out.append("1")
        out.reverse()
        return ''.join(out)


print(__name__)
obj = Solution()
assert obj.addBinary("0101", "10") == "0111"
