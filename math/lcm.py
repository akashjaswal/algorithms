# Uses python3
import sys
import unittest


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b


def gcd(a, b):
    if a == 0:
        return b

    if b == 0:
        return a

    while b != 0:
        return gcd(b, a % b)


def lcm_efficient(a, b):
    return (a*b) // gcd(a, b)


class TestLCM(unittest.TestCase):

    def test_lcm_naive(self):
        self.assertEqual(lcm_naive(2, 4), 4)
        self.assertEqual(lcm_naive(6, 8), 24)

    def test_lcm_efficient(self):
        self.assertEqual(lcm_efficient(2, 4), 4)
        self.assertEqual(lcm_efficient(6, 8), 24)
        self.assertEqual(lcm_efficient(28851538, 1183019), 1933053046)


if __name__ == '__main__':
    unittest.main()
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
