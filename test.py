from flatten import *
import unittest


class TestFunctions(unittest.TestCase):

    def test_add(self):  # 测试加法的方法
        self.assertEqual(flatten([7, [8, [9], 3]]), [7, 8, 9, 3])
        self.assertEqual(flatten([]), [])


if __name__ == '__main__':
    unittest.main()
