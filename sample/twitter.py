from __future__ import annotations


class Tweet:
    def __init__(
        self,
        owner: TwitterAccount,
        *,
        text: str = "",
        original_tweet: Tweet | None = None,
    ) -> None:
        if original_tweet:
            if text:
                raise ValueError(
                    "Cannot be both tweet and retweet at the same time."
                )
            if original_tweet.owner is self:
                raise ValueError("Cannot retweet own tweet.")

            original_tweet.retweets += 1

        self.retweets = 0
        self.owner = owner
        self.text = text
        self.original_tweet = original_tweet


class TwitterAccount:
    def __init__(self, name: str) -> None:
        self.tweets: list[Tweet] = []
        self.following: list[TwitterAccount] = []
        self.followers: list[TwitterAccount] = []
        self.name = name

    def follow(self, account: TwitterAccount) -> None:
        account.followers.append(self)
        self.following.append(self)

    def unfollow(self, account: TwitterAccount) -> None:
        account.followers.remove(self)
        self.following.remove(self)

    def is_following(self, account: TwitterAccount) -> bool:
        return account in self.following

    def is_followed_by(self, account: TwitterAccount) -> bool:
        return account.is_following(self)

    def tweet(self, text: str) -> None:
        self.tweets.append(Tweet(self, text=text))

    def retweet(self, original_tweet: Tweet) -> None:
        self.tweets.append(Tweet(self, original_tweet=original_tweet))

    def get_tweet(self, n: int) -> Tweet:
        if not 0 < n <= self.get_tweet_size():
            raise ValueError("Illegal index.")
        return self.tweets[n]

    def get_tweet_size(self) -> int:
        return len(self.tweets)

    def get_retweet_count(self) -> int:
        return sum(tweet.retweets for tweet in self.tweets)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
