from unittest import TestCase

import oeis

class TestChoose(TestCase):
    def test_equal(self):
        r = oeis.choose(9, 9)
        self.assertEqual(r, 1)
