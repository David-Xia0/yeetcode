class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        letters = {}
        
        for letter in magazine:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

        for letter in ransomNote:
            if letter in letters:
                count = letters[letter] - 1
                if count == 0:
                    del letters[letter]
                else:
                    letters[letter] = count
            else:
                return False

        return True