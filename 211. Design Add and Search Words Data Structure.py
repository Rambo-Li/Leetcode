class WordDictionary:

    def __init__(self):
        self.d = {}

    def addWord(self, word: str) -> None:
        currdict = self.d
        for w in word:
            if w not in currdict:
                currdict[w] = {}
            currdict = currdict[w]
        currdict["#"] = {}

    def search(self, word: str) -> bool:
        def bfs(dt, word):
            currdict = dt
            
            for i in range(len(word)):
                if word[i] != ".":
                    if word[i] in currdict:
                        currdict = currdict[word[i]]
                    else:
                        return False
                else:
                    for key in currdict:
                        if bfs(currdict[key], word[i+1:]):
                            return True
                    return False
            return "#" in currdict
        return bfs(self.d, word)

