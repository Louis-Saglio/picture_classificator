from typing import Tuple
from src.helpers import sample


class ThemeManager:

    def __init__(self):
        self.keywords = []

    def add_keyword(self, word: str, rank: int):
        for i in range(rank+1):
            if i == len(self.keywords):
                self.keywords.append([])
        self.keywords[rank].append(word)

    def add_ranked_keywords(self, rank: int, *keywords: str):
        for keyword in keywords:
            self.add_keyword(keyword, rank)

    def add_keywords(self, *args: Tuple[str, int]):
        for arg in args:
            self.add_keyword(arg[0], arg[1])

    def generate_query(self):
        query = list()
        for keywords in self.keywords:
            query += sample(keywords)
        return '+'.join(query)
