import unittest
from binary_gap import binary_gap

# filepath: /home/jain/Desktop/ws/gh/public/algorithms_design_and_analysis/1 - Binary Gap (Problem of Iterations)/test_binary_gap.py


class TestBinaryGap(unittest.TestCase):
    def test_no_gap(self):
        self.assertEqual(binary_gap(15), 0)  # Binary: 1111
        self.assertEqual(binary_gap(1), 0)   # Binary: 1

    def test_single_gap(self):
        self.assertEqual(binary_gap(9), 2)   # Binary: 1001
        self.assertEqual(binary_gap(20), 1) # Binary: 10100

    def test_multiple_gaps(self):
        self.assertEqual(binary_gap(529), 4) # Binary: 1000010001
        self.assertEqual(binary_gap(1041), 5) # Binary: 10000010001

    def test_edge_cases(self):
        self.assertEqual(binary_gap(0), 0)   # Binary: 0
        self.assertEqual(binary_gap(6), 0)  # Binary: 110

if __name__ == "__main__":
    unittest.main()