# Uses python3
import sys
import unittest


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_efficient(a, b):
    """
    GCD Euclid Algorithm. GCD of two integers A and B is the largest integer that divides both A and B.
    """
    if a == 0:
        return b

    if b == 0:
        return a

    while b != 0:
        return gcd_efficient(b, a % b)
    return a


class GcdTest(unittest.TestCase):

    def test_gcd_naive(self):
        self.assertEqual(gcd_naive(18, 35), 1)
        self.assertEqual(gcd_naive(28851538, 1183019), 17657)

    def test_gcd_efficient(self):
        self.assertEqual(gcd_efficient(18, 35), 1)
        self.assertEqual(gcd_efficient(0, 12), 12)
        self.assertEqual(gcd_efficient(18, 0), 18)
        self.assertEqual(gcd_efficient(28851538, 1183019), 17657)


if __name__ == "__main__":
    unittest.main()
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_efficient(a, b))
