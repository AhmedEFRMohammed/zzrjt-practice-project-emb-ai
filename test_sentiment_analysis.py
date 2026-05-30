import unittest
from SentimentAnalysis.sentiment_analyzer import sentiment_analyzer


class TestSentimentAnalysis(unittest.TestCase):
    def test_sentiment_analyzer(self):
        self.assertEqual(sentiment_analyzer("I love working with python")["label"], "SENT_POSITIVE")
        self.assertEqual(sentiment_analyzer("I hate working with python")["label"], "SENT_NEGATIVE")
        self.assertEqual(sentiment_analyzer("I am neutral on python")["label"], "SENT_NEUTRAL")
        

unittest.main()