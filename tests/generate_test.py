import unittest

import msudoku


class GenerateTest(unittest.TestCase):
    def test_wfc(self):
        for _ in range(20):
            m = msudoku.generate(method="wfc")
            ok, err_pos = msudoku.check(m)
            self.assertTrue(ok, msg=f"{err_pos}")

    def test_np_union(self):
        m = msudoku.generate(method="np_union")
        ok, err_pos = msudoku.check(m)
        self.assertTrue(ok, msg=f"{err_pos}")
