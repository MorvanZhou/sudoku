import unittest

import sudokum


class GenerateTest(unittest.TestCase):
    def test_wfc(self):
        for _ in range(20):
            m = sudokum.generate(method="wfc")
            ok, err_pos = sudokum.check(m)
            self.assertTrue(ok, msg=f"{err_pos}")

    def test_np_union(self):
        m = sudokum.generate(method="np_union")
        ok, err_pos = sudokum.check(m)
        self.assertTrue(ok, msg=f"{err_pos}")
