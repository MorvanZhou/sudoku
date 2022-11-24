import unittest

from sudokum.method.mask import mask


class MaskTest(unittest.TestCase):
    def test_mask(self):
        g = [
            [1, 2],
            [3, 4],
        ]
        rate = 0.5
        for _ in range(10):
            m = mask(g, rate)
            total = 0
            masked = 0
            for r in range(len(m)):
                for c in range(len(m[0])):
                    total += 1
                    if m[r][c] == 0:
                        masked += 1
            self.assertEqual(int(total * rate), masked)
