# python3
import unittest


def max_pairwise_product(n, numbers):
    """
    :param n: length of list
    :param numbers: list of integers
    """

    max_index1 = -1
    for i in range(n):
        if max_index1 == -1 or numbers[i] > numbers[max_index1]:
            max_index1 = i

    max_index2 = -1
    for i in range(n):
        if i != max_index1 and (max_index2 == -1 or numbers[i] > numbers[max_index2]):
            max_index2 = i

    return numbers[max_index1] * numbers[max_index2]


class PPTest(unittest.TestCase):

    def test_max_pairwise_product(self):
        self.assertEqual(max_pairwise_product(4, [3, 1, 2, 5]), 15)
        self.assertEqual(max_pairwise_product(6, [10, 2, 4, 10, 3, 1]), 100)


if __name__ == '__main__':
    unittest.main()
    n = int(input())
    a = [int(x) for x in input().split()]
    print(max_pairwise_product(n, a))
