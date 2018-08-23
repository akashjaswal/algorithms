# Uses python3
import unittest


def calc_fib(n):

    if n <= 1:
        return n

    elif n <= 45:

        prev, curr = 0, 1
        for i in range(2, n+1):
            new = curr + prev
            prev = curr
            curr = new
        return new

    else:
        print("Value too large!")
        return None


class FibTest(unittest.TestCase):

    def test_calc_fib(self):
        self.assertEqual(calc_fib(10), 55)
        self.assertEqual(calc_fib(13), 233)


if __name__ == "__main__":

    unittest.main()

    n = int(input())
    print(calc_fib(n))
