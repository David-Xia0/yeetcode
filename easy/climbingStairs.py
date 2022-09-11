class Solution:
    def climbStairs(self, n: int, mem = {}) -> int:

        if n in mem:
            return mem[n]
        count = 0
        n1 = n - 1
        n2 = n - 2
        if n2 == 0:
            return 2
        elif n2 > 0:
            if n2 == 0:
                return 2
            else:
                count +=  self.climbStairs(n2)
            count += self.climbStairs(n1)
            mem[n] = count
            return count
        else:
            return 1