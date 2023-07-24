class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = {}
        d = {}
        for word in words:
            curr = d
            for w in word:
                if w not in curr:
                    curr[w] = {}
                curr = curr[w]
            curr["#"] = {}

        def remove(dt, word):
            curr = dt
            stack = []
            for letter in word:
                stack.append((curr, letter))
                curr = curr[letter]
            stack.append((curr, "#"))
            curr, key = stack.pop()
            while stack and (not curr[key]):
                curr.pop(key)
                curr, key = stack.pop()

        def dfs(i, j, dt, wd, exclude):
            nonlocal res, board, d
            currdict = dt[board[i][j]]
            wd += board[i][j]
            exclude += ((i, j),)
            if "#" in currdict and (wd not in res):
                res[wd] = 1
                remove(d, wd)
            for x,y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if i+x>=0 and i+x<m and j+y>=0 and j+y<n and (i+x,j+y) not in exclude and board[i+x][j+y] in currdict:
                    dfs(i+x, j+y, currdict, wd, exclude)

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in d:                    
                    wd = ""
                    exclude = tuple()
                    dfs(i, j, d, wd, exclude)

        return res.keys()