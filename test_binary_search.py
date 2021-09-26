import unittest
from dataclasses import dataclass
from typing import List

from binary_search import binary_search


@dataclass
class BinarySearchCase:
    description: str
    lst: List[int]
    target: int
    expected: int


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        cases = [
            BinarySearchCase(
                description="Even number of elements",
                lst=[0] + [1] * 9,
                target=0,
                expected=0,
            ),
            BinarySearchCase(
                description="Odd number of elements",
                lst=[0] + [1] * 8,
                target=0,
                expected=0,
            ),
            BinarySearchCase(description="Not present", lst=[], target=0, expected=-1),
        ]
        for case in cases:
            with self.subTest(msg=case.description):
                self.assertEqual(binary_search(case.lst, case.target), case.expected)
