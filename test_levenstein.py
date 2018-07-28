import unittest
from levenstein import levenstein


class LevensteinTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(0, levenstein("", ""))
        self.assertEqual(0, levenstein("one", "one"))
        self.assertEqual(0, levenstein("one two", "one two"))
        self.assertEqual(0, levenstein("one two", "one     two"))

    def test_insertions(self):
        self.assertEqual(1, levenstein("", "one"))
        self.assertEqual(1, levenstein("one", "one two"))

    def test_substitutions(self):
        self.assertEqual(1, levenstein("one two", "one too"))
        self.assertEqual(1,levenstein("one two three", "one four three"))
        self.assertEqual(1, levenstein("one two three", "one two free"))
        self.assertEqual(1, levenstein("one two three four five", "one two free four five"))
        self.assertEqual(2, levenstein("one two three four five", "one two free for five"))

    def test_deletions(self):
        self.assertEqual(1, levenstein("one", ""))
        self.assertEqual(1, levenstein("one two three ", "one three"))
        self.assertEqual(1, levenstein("one two three four", "one three four"))
        self.assertEqual(1, levenstein("one two three", "two three"))

        # this could be interpreted as:
        # substitution + 5 insertions
        # 5 deletions
        # the second doesn't make any sense in the context of speech as the same word
        # could occur more than once so it's best to only evaluate the next token
        # for comparison
        self.assertEqual(6,levenstein("one two three four five six seven", "one seven"))


    def test_deletions_and_insertions(self):
        # there are two ways to interpret this, but both produce the same score:
        # substitution and subsitution
        # deletion and insertion
        self.assertEqual(2,levenstein("one two three", "one three four"))


if __name__ == "__main__":
    unittest.main()
