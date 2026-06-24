class Twitter:

    def __init__(self):
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet_map[userId].append([self.time, tweetId])


    def getNewsFeed(self, userId: int) -> List[int]:
        # get followed users and self
        users = set(self.follow_map[userId])
        users.add(userId)

        # get 1 latest tweets from self and followed users
        users_tweets = []
        for uid in users:
            tweets = self.tweet_map[uid]
            if tweets:
                idx = len(tweets) - 1           # find the idx of latest tweet
                t, tid = tweets[idx]            # grab the latest tweet
                heapq.heappush(users_tweets, (-t, uid, idx, tid))


        feed = []
        while users_tweets and len(feed) < 10:
            t, user_id, idx, tweet_id = heapq.heappop(users_tweets)
            feed.append(tweet_id)

            if idx - 1 >= 0:
                t2, tid2 = self.tweet_map[user_id][idx - 1]
                heapq.heappush(users_tweets, (-t2, user_id, idx - 1, tid2))
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)