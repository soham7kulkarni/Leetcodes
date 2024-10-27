class Tweet:
    def __init__(self, tweet_id, time):
        # Initialize a tweet with its ID and timestamp
        self.tweet_id = tweet_id
        self.time = time


class Twitter:
    def __init__(self):
        # Map of user IDs to sets of followed user IDs
        self.usr_map = {}
        # Map of user IDs to lists of tweets
        self.tweet_map = {}
        # A timestamp counter for tweets
        self.t = 0

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        # Increment the timestamp
        self.t += 1
        # Create a new tweet
        tweet = Tweet(tweet_id, self.t)
        # If user has no tweets yet, initialize their tweet list
        if user_id not in self.tweet_map:
            self.tweet_map[user_id] = []
        # Add the tweet to the user's tweet list
        self.tweet_map[user_id].append(tweet)

    def getNewsFeed(self, user_id: int) -> List[int]:
        # Ensure user follows themselves to see their own tweets
        self.follow(user_id, user_id)
        # Get the set of users that the user follows
        users = self.usr_map.get(user_id, set())
        # Priority queue to sort tweets by time (newest first)
        pq = []
        
        # Add tweets from all followed users to the priority queue
        for user in users:
            tweet_list = self.tweet_map.get(user, [])
            for tweet in tweet_list:
                pq.append(tweet)
        
        # Sort tweets in descending order based on time
        pq.sort(key=lambda x: x.time, reverse=True)
        
        # Get the most recent 10 tweets
        result = []
        for i in range(min(10, len(pq))):
            result.append(pq[i].tweet_id)
        
        return result

    def follow(self, follower_id: int, followee_id: int) -> None:
        # If follower does not exist, initialize their set of followed users
        if follower_id not in self.usr_map:
            self.usr_map[follower_id] = set()
        # Add the followee to the follower's set of followed users
        self.usr_map[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        # If follower exists, is not unfollowing themselves, and is following the followee
        if (follower_id in self.usr_map and
                follower_id != followee_id and
                followee_id in self.usr_map[follower_id]):
            # Remove the followee from the follower's set
            self.usr_map[follower_id].remove(followee_id)

# Example of usage:
# twitter = Twitter()
# twitter.postTweet(user_id, tweet_id)
# feed = twitter.getNewsFeed(user_id)
# twitter.follow(follower_id, followee_id)
# twitter.unfollow(follower_id, followee_id)
