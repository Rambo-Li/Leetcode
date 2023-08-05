class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wl = set(wordList)
        if endWord not in wl:
            return 0
        wordlen = len(beginWord)
        frontset = set((beginWord,))
        endset = set((endWord,))
        step = 1
        while frontset:
            wl -= frontset
            newset = set()
            step += 1
            for i in range(len(frontset)):
                word = frontset.pop()                
                for i in range(wordlen):
                    for letter in 'abcdefghijklmnopqrstuvwxyz':
                        if word[:i] + letter + word[i+1:] in wl:
                            w = word[:i] + letter + word[i+1:]
                            if w in endset:
                                return step
                            newset.add(w)

            frontset = newset
            if len(frontset) > len(endset):
                frontset, endset = endset, frontset
        return 0
    
# Two way BFS and always expand the narrow side. I'm amazed how succinct it is and how two directions use one set as visited.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        # wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        # visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord in wordList:
                            wordList.remove(neiWord)
                            q.append(neiWord)
            res += 1
        return 0
# This method designed a way to proprocess the word list so the distance 1 word is a O(1) dict operation.