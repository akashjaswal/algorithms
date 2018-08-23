# Uses python3
import unittest


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_efficient(n):
    if n <= 1:
        return n

    elif n <= 10 ^ 7:

        previous = 0
        current = 1

        for i in range(2, n+1):
            next = (previous + current) % 10
            previous = current
            current = next

        return next

    else:
        print("Value too large")
        return None


class FibTest(unittest.TestCase):

    def test_get_fibonacci_last_digit_naive(self):
        self.assertEqual(get_fibonacci_last_digit_naive(4), 3)
        self.assertEqual(get_fibonacci_last_digit_naive(5), 5)
        self.assertEqual(get_fibonacci_last_digit_naive(6), 8)

    def test_get_fibonacci_last_digit_efficient(self):
        self.assertEqual(get_fibonacci_last_digit_efficient(4), 3)
        self.assertEqual(get_fibonacci_last_digit_efficient(327305), 5)


if __name__ == '__main__':

    unittest.main()

    n = int(input())
    print(get_fibonacci_last_digit_efficient(n))
