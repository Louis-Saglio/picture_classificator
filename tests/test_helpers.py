from unittest import TestCase

from src.helpers import sample


class TestHelpers(TestCase):
    def test_sample(self):
        pop = sample([1, 2, 3, 5, 5])
        self.assertLess(len(pop), 6)
        self.assertGreater(len(pop), 0)
