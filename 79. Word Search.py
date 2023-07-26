class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, word, exclude):
            nonlocal m, n, board
            if not word:
                return True
            exclude += ((i,j),)
            
            for x,y in [(-1,0), (1,0), (0,1), (0,-1)]:
                if i+x<m and i+x>=0 and j+y<n and j+y>=0 and board[i+x][j+y]==word[0] and (i+x, j+y) not in exclude:
                    if dfs(i+x, j+y, word[1:], exclude):
                        return True
            return False
        
        # Count number of letters in board and store it in a dictionary
        boardDic = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                boardDic[board[i][j]] += 1

        # Count number of letters in word
        # Check if board has all the letters in the word and they are atleast same count from word
        wordDic = Counter(word)
        for c in wordDic:
            if c not in boardDic or boardDic[c] < wordDic[c]:
                return False
                
        m = len(board)
        n = len(board[0])
        res = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[1:], ()):
                        return True
        return False
    
# The dict check improves a lot in terms of time. This is a hack to test cases. The fastest solution also compares the end and start of the words, and start dfs
# on whichever less frequent on board.