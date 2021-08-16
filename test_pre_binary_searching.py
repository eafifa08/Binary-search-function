import unittest
from bin_search import pre_binary_searching

class BinarySearchingTestCase(unittest.TestCase):
    """
    Тесты для main.pre_binary_searching
    """
    def test_searching_num_in_array(self):
        """Поиск 4 в [-11..10]"""
        array = [x for x in range(-11, 11)]
        index = pre_binary_searching(array, 4)
        self.assertEqual(index, array.index(4))


if __name__ == '__main__':
    unittest.main()