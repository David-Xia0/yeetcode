class Trie:
    def __init__(self):
        self.store = {}
        self.words = set()

    def insert(self, word: str) -> None:
        self.words.add(word)
        curr_store = self.store
        for letter in word:
            if letter in curr_store:
                curr_store = curr_store[letter]
            else:
                curr_store[letter] = {}
                curr_store = curr_store[letter]   

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        curr_store = self.store
        for letter in prefix:
            if letter in curr_store:
                curr_store = curr_store[letter]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)