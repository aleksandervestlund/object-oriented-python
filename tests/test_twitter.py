from unittest import TestCase

from sample.twitter import Tweet, TwitterAccount


class TweetTest(TestCase):
    def setUp(self) -> None:
        self.nils = TwitterAccount("Nils")
        self.ole = TwitterAccount("Ole")
        self.kari = TwitterAccount("Kari")

        self.tweet = Tweet(self.nils, text="Kvitre!")
        self.retweet1 = None
        self.retweet2 = None

    def test_constructor_new_tweet(self) -> None:
        self.assertEqual("Kvitre!", self.tweet.text)
        self.assertEqual(self.nils, self.tweet.owner)

    def test_constructor_retweet(self) -> None:
        retweet1 = Tweet(self.ole, original_tweet=self.tweet)
        self.assertEqual("Kvitre!", retweet1.text)
        self.assertEqual(self.ole, retweet1.owner)

        with self.assertRaises(ValueError):
            Tweet(self.nils, original_tweet=self.tweet)

    def test_get_original_tweet(self) -> None:
        self.assertIsNone(self.tweet.original_tweet)
        retweet1 = Tweet(self.ole, original_tweet=self.tweet)
        self.assertEqual(self.tweet, retweet1.original_tweet)
        self.assertEqual(retweet1.original_tweet.text, retweet1.text)  # type: ignore
        Tweet(self.kari, original_tweet=self.tweet)  # Dummy retweet
        self.assertEqual(self.tweet, retweet1.original_tweet)
        self.assertEqual(retweet1.original_tweet.text, retweet1.text)  # type: ignore

    def test_get_retweet_count(self) -> None:
        self.assertEqual(0, self.tweet.retweet_count)
        Tweet(self.ole, original_tweet=self.tweet)
        self.assertEqual(1, self.tweet.retweet_count)
        Tweet(self.kari, original_tweet=self.tweet)
        self.assertEqual(2, self.tweet.retweet_count)


class TwitterAccountTest(TestCase):
    def setUp(self) -> None:
        self.nils = TwitterAccount("Nils")
        self.ole = TwitterAccount("Ole")

    def _check_follow(
        self,
        account_a: TwitterAccount,
        account_b: TwitterAccount,
        a_follows_b: bool,
        b_follows_a: bool,
    ) -> None:
        if a_follows_b:
            self.assertTrue(account_a.is_following(account_b))
            self.assertTrue(account_b.is_followed_by(account_a))
        else:
            self.assertFalse(account_a.is_following(account_b))
            self.assertFalse(account_b.is_followed_by(account_a))

        if b_follows_a:
            self.assertTrue(account_b.is_following(account_a))
            self.assertTrue(account_a.is_followed_by(account_b))
        else:
            self.assertFalse(account_b.is_following(account_a))
            self.assertFalse(account_a.is_followed_by(account_b))

    def test_constructor(self) -> None:
        self.assertEqual("Nils", self.nils.username)
        self.assertEqual("Ole", self.ole.username)

    def test_follow(self) -> None:
        self.nils.follow(self.ole)
        self._check_follow(self.nils, self.ole, True, False)

        self.ole.follow(self.nils)
        self._check_follow(self.nils, self.ole, True, True)

    def test_unfollow(self) -> None:
        self._check_follow(self.nils, self.ole, False, False)

        self.nils.follow(self.ole)
        self._check_follow(self.nils, self.ole, True, False)

        self.nils.unfollow(self.ole)
        self._check_follow(self.nils, self.ole, False, False)

    def test_new_tweet(self) -> None:
        self.nils.tweet("Kvitre!")
        self.assertEqual("Kvitre!", self.nils.get_tweet(1).text)
        self.nils.tweet("Kvitre igjen!")
        self.assertEqual("Kvitre igjen!", self.nils.get_tweet(1).text)
        self.assertEqual("Kvitre!", self.nils.get_tweet(2).text)

    def test_illegal_tweet(self) -> None:
        with self.assertRaises(ValueError):
            self.nils.get_tweet(1)
        with self.assertRaises(ValueError):
            self.nils.get_tweet(-1)

        self.nils.tweet("Kvitre!")
        with self.assertRaises(ValueError):
            self.nils.get_tweet(2)
        with self.assertRaises(ValueError):
            self.nils.get_tweet(-1)

    def test_retweet(self) -> None:
        kari = TwitterAccount("Kari")

        self.nils.tweet("Kvitre!")
        self.assertEqual("Kvitre!", self.nils.get_tweet(1).text)

        self.ole.retweet(self.nils.get_tweet(1))
        self.assertEqual(1, self.nils.get_retweet_count())
        self.assertEqual(0, self.ole.get_retweet_count())
        self.assertEqual("Kvitre!", self.ole.get_tweet(1).text)
        self.assertEqual(
            self.nils.get_tweet(1), self.ole.get_tweet(1).original_tweet
        )

        kari.retweet(self.ole.get_tweet(1))
        self.assertEqual(2, self.nils.get_retweet_count())
        self.assertEqual(0, self.ole.get_retweet_count())
        self.assertEqual(0, kari.get_retweet_count())
        self.assertEqual("Kvitre!", kari.get_tweet(1).text)
        self.assertEqual(
            self.nils.get_tweet(1), kari.get_tweet(1).original_tweet
        )
