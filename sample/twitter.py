from __future__ import annotations


class Tweet:
    def __init__(
        self,
        owner: TwitterAccount,
        *,
        text: str = "",
        original_tweet: Tweet | None = None,
    ) -> None:
        if original_tweet is not None:
            if text:
                raise ValueError(
                    "Cannot be both tweet and retweet at the same time."
                )
            if original_tweet.owner is owner:  # type: ignore
                raise ValueError("Cannot retweet own tweet.")

            if (
                temp_original_tweet := original_tweet.original_tweet  # type: ignore
            ) is not None:
                original_tweet = temp_original_tweet
            text = original_tweet.text  # type: ignore
            original_tweet.retweet_count += 1  # type: ignore

        self.retweet_count = 0
        self.owner = owner
        self.text = text
        self.original_tweet = original_tweet


class TwitterAccount:
    def __init__(self, username: str) -> None:
        self.tweets: list[Tweet] = []
        self.followers: list[TwitterAccount] = []
        self.username = username

    def follow(self, account: TwitterAccount) -> None:
        account.followers.append(self)

    def unfollow(self, account: TwitterAccount) -> None:
        account.followers.remove(self)

    def is_following(self, account: TwitterAccount) -> bool:
        return account.is_followed_by(self)

    def is_followed_by(self, account: TwitterAccount) -> bool:
        return account in self.followers

    def tweet(self, text: str) -> None:
        self.tweets.insert(0, Tweet(self, text=text))

    def retweet(self, original_tweet: Tweet) -> None:
        self.tweets.append(Tweet(self, original_tweet=original_tweet))

    def get_tweet(self, n: int) -> Tweet:
        if not 0 < n <= len(self.tweets):
            raise ValueError("Illegal index.")
        return self.tweets[n - 1]

    def get_retweet_count(self) -> int:
        return sum(tweet.retweet_count for tweet in self.tweets)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
