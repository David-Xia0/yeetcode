class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mem = {}


        for letter in list(s):
            if letter in mem:
                mem[letter] = mem[letter] + 1
            else:
                mem[letter] = 1

        for letter in list(t):
            if letter in mem:
                count = mem[letter] - 1
                if count == 0:
                    del mem[letter]
            else:
                return False

        if len(mem) != 0:
            return False

        return True

