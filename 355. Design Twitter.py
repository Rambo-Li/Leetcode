class Twitter:

    def __init__(self):
        self.tweets = {}
        self.id = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId] = self.tweets.get(userId, []) + [(self.time, tweetId)]
        self.time -= 1
        if userId not in self.id:
            self.id[userId] = [userId]

    def getNewsFeed(self, userId: int) -> List[int]:
        tts = []
        if userId in self.id:
            for uid in self.id[userId]:
                if uid in self.tweets:
                    tts += self.tweets[uid]
        heapify(tts)
        res = []
        while tts and len(res)<10:
            time, tid = heappop(tts)
            res.append(tid)
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.id:
            self.id[followerId] = [followerId]
        if followeeId not in self.id[followerId]:
            self.id[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.id[followerId]:
            self.id[followerId].remove(followeeId)
