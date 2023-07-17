#!/usr/bin/python
# -*- coding: utf-8 -*-

# run with pytest

import unittest
from py_test_pack import main

class Test(unittest.TestCase):
    def test_main_one(self):
        self.assertEqual(main.alphabet("cat"), True)

    def test_main_two(self):
        self.assertEqual(main.alphabet("what"), True)

    def test_main_three(self):
        self.assertEqual(main.alphabet("“hello”"), False)

    def test_main_four(self):
        self.assertEqual(main.alphabet("THAT"), False)

    def test_main_five(self):
        self.assertEqual(main.numbers("19%"), True)

    def test_main_six(self):
        self.assertEqual(main.numbers("300%"), True)

    def test_main_seven(self):
        self.assertEqual(main.numbers("%"), False)

    def test_main_eight(self):
        self.assertEqual(main.numbers("0%"), False)

if __name__ == '__main__':
    unittest.main()