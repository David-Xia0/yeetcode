class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}

        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

        length = 0
        odd = True
        for letter in letters:
            letter_count = letters[letter]
            if letter_count % 2 == 0:
                length +=  letter_count
            elif odd:
                length += letter_count
                odd = False
            else:
                length += letter_count - 1

        return length

# can do add and remove from set to check for duplicates