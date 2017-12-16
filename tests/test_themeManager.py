from unittest import TestCase

from src.theme_manager import ThemeManager


class TestThemeManager(TestCase):

    def test_add_keyword(self):
        tm = ThemeManager('test')
        tm.add_keyword("tree", 0)
        tm.add_keyword("arbre", 5)
        tm.add_keyword("branche", 5)
        self.assertListEqual(tm.keywords, [['test', 'tree'], [], [], [], [], ['arbre', 'branche']])

    def test_add_ranked_keywords(self):
        tm = ThemeManager('test')
        tm.add_ranked_keywords(2, "tree", "branche", "arbre", "root")
        self.assertListEqual(tm.keywords, [['test'], [], ['tree', 'branche', 'arbre', 'root']])

    def test_add_keywords(self):
        tm = ThemeManager('test')
        tm.add_keywords(("tree", 0), ("arbre", 0), ("branche", 2))
        self.assertListEqual(tm.keywords, [['test', 'tree', 'arbre'], [], ['branche']])

    def test_generate_query(self):
        tm = ThemeManager('test')
        tm.add_keywords(("1", 0), ("0", 1), ("2", 2))
        tm.generate_query()
