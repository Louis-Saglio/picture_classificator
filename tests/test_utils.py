from unittest import TestCase

from src.utils import sample


class TestUtils(TestCase):
    def test_sample(self):
        pop = sample([1, 2, 3, 4, 5], 4, 4)
        self.assertEqual(len(pop), 4)
        self.assertTrue(set(pop), [1, 2, 3, 4, 5])
        self.assertRaises(AssertionError, lambda: sample([1, 2, 3, 4], 1, 2))
