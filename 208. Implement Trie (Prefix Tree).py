class Trie:

    def __init__(self):
        self.d = {}
        
    def insert(self, word: str) -> None:
        currdict = self.d
        for w in word:
            if w not in currdict:
                currdict[w] = {}
            currdict = currdict[w]
        currdict["#"] = 'endWord'

    def search(self, word: str) -> bool:
        currdict = self.d
        for w in word:
            if w not in currdict:
                return False
            currdict = currdict[w]
        return "#" in currdict

    def startsWith(self, prefix: str) -> bool:
        currdict = self.d
        for w in prefix:
            if w not in currdict:
                return False
            currdict = currdict[w]
        return True