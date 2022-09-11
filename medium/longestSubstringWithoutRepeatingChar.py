class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = {}
        maxLen = 0
        length = 0
        start = 0
        pointer = 0
        while pointer != len(s):
            if s[pointer] in char:
                length -= char[s[pointer]] - start
                newStart = char[s[pointer]] + 1
                for i in range(start, char[s[pointer]]):
                    del char[s[i]]
                start = newStart
                char[s[pointer]] = pointer
            else:
                length += 1
                maxLen = max(maxLen, length)
                char[s[pointer]] = pointer
            pointer += 1

        return maxLen


        # 1 2 2 3 4 5 6
        # 0 1 2 3 4
