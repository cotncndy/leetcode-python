# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see
#  the 10 most recent tweets in the user's news feed. Your design should support the following methods:
#
# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must
#  be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least
# recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
# Example:
#
# Twitter twitter = new Twitter();
#
# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
#
# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);
#
# // User 1 follows user 2.
# twitter.follow(1, 2);
#
# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
#
# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.getNewsFeed(1);
#
# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
#
# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);

from heapq import heappush, heappop
import collections


class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.twitte_id = 0
        self.followed_by = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        # heappush(self.tweets[userId], (-self.twitte_id, tweetId))  # there is no maxheap in python, so use min-heap to
        self.tweets[userId].append((-self.twitte_id, tweetId))
        self.twitte_id += 1


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        friends = self.followed_by[userId]  # got all followers of userId
        friends.add(userId)  # add itself as friend

        temp = []
        for id in friends:
            # bugfixed
            if self.tweets[id]:
                heappush(temp, [self.tweets[id][-1], len(self.tweets[id]) - 1, id])

        res = []
        while temp and len(res) < 10:
            a = heappop(temp)
            res.append(a[0][1])  # don't forget the negative
            if a[1] - 1 > 0:
                a[1] -= 1
                a[0] = self.tweets[a[2]][a[1]]
                heappush(temp, a)

        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followed_by[followerId].add(followeeId)
        # todo you need put all followeeID's tweet to folower

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followed_by[followerId].remove(followeeId)
        # todo , you need to remove all followeeid's tweets from followerid


if __name__ == '__main__':
    obj = Twitter()
    obj.postTweet(1, 1)
    print obj.getNewsFeed(1)
    obj.follow(2, 1)
    print obj.getNewsFeed(2)
    obj.unfollow(2, 1)
    print obj.getNewsFeed(2)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
