import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestSearchCategory(unittest.TestCase):
    def test_search_by_category(self):
        items = [
            DigitalVideoDisc("The Lion King", category="Animation"),
            DigitalVideoDisc("Star Wars", category="Science Fiction"),
        ]
        result = search_by_category(items, "Animation")
        self.assertEqual([d.title for d in result], ["The Lion King"])


if __name__ == "__main__":
    unittest.main()