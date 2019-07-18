import sys
sys.path.append("C:\\Users\\Administrator\\PycharmProjects\\untitled1")
import unittest
from test_UItwo.aaa import *





class test_yy(unittest.TestCase):

    def test_add(self):
        self.assertEqual(3, temp().add(1,2))
        self.assertNotEqual(3,temp().add(2, 2))



    def test_minus(self):
        self.assertEqual(1,temp().minus(3, 2))




    def test_multi(self):
        self.assertEqual(6, temp().multi(2, 3))



    def test_divide(self):
        self.assertEqual(2, temp().divide(6, 3))
        self.assertEqual(2.5, temp().divide(5, 2))


if __name__ == '__main__':
        unittest.main()
