import unittest

import msudoku


class SolveTest(unittest.TestCase):
    def test_np_union(self):
        method = "np_union"
        g = msudoku.generate(mask_rate=0.5, method=method)
        ok, s = msudoku.solve(g, max_try=1, method=method)
        self.assertTrue(ok)
        self.assertTrue(msudoku.check(s))

    def test_wfc(self):
        for _ in range(5):
            method = "wfc"
            g = msudoku.generate(mask_rate=0.95, method=method)
            ok, s = msudoku.solve(g, max_try=10, method=method)
            self.assertTrue(ok, msg=s)
            self.assertTrue(msudoku.check(s))

    def test_np_gene_wfc_sol(self):
        g = msudoku.generate(mask_rate=0.95, method="np_union")
        ok, s = msudoku.solve(g, max_try=10, method="wfc")
        self.assertTrue(ok, msg=s)
        self.assertTrue(msudoku.check(s))

    def test_wfc_gene_np_sol(self):
        g = msudoku.generate(mask_rate=0.95, method="wfc")
        ok, s = msudoku.solve(g, max_try=1, method="np_union")
        self.assertTrue(ok, msg=s)
        self.assertTrue(msudoku.check(s))
